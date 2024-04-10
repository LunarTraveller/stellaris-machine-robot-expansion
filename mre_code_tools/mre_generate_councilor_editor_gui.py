import argparse
from datetime import datetime
import os
import time
import sys
from json import load as json_load

from mre_common_vars import (
    AUTOGENERATED_HEADER,
    BUILD_FOLDER,
    CORE_MODIFYING,
    EXCLUDE_SUBCLASSES_FROM_CORE_MODIFYING,
    EXCLUDE_TRAITS_FROM_CORE_MODIFYING,
    GESTALT_COUNCILOR_CLASS_MAP,
    GESTALT_COUNCILOR_SUBCLASS_MAP,
    GESTALT_COUNCILOR_TYPES,
    GUI_FOOTER_TEXT,
    GUI_HEADER_TEXT,
    OUTPUT_FILES_DESTINATIONS,
    TRAITS_REQUIRING_DLC,
    RARITIES,
    COUNCILOR_EDITOR,
    FILE_NUM_PREFIXES,
    GESTALT_COUNCILOR_SOURCE_TRAITS_FILES,
    CODE_HEADER,
    EXCLUDE_TRAITS_FROM_PARAGON_DLC,
)

"""
   _____ _    _ _____ 
  / ____| |  | |_   _|
 | |  __| |  | | | |  
 | | |_ | |  | | | |  
 | |__| | |__| |_| |_ 
  \_____|\____/|_____|
                      
                      
"""



def iterate_traits_generate_councilor_gui_code_for_regulatory():
    pass

def iterate_traits_generate_councilor_gui_code_for_cognitive():
    pass

def iterate_traits_generate_councilor_gui_code_for_growth():
    pass

def iterate_traits_generate_councilor_gui_code_for_legion():
    pass

def iterate_traits_generate_gui_code_for_councilor(
        organized_traits_dict: dict,
        councilor_type: str
) -> str:
    # TODO: Don't generate traits that require subclasses other than the councilor's subclass

    # Setup
    councilor_leader_class = GESTALT_COUNCILOR_CLASS_MAP[councilor_type]
    councilor_subclass = GESTALT_COUNCILOR_SUBCLASS_MAP[councilor_type]

    header_classname_spaced = ' '.join([char for char in councilor_leader_class])
    header = GUI_HEADER_TEXT.format(
        classname=header_classname_spaced,
        now=str(datetime.now())
    )
    footer = GUI_FOOTER_TEXT.format(
        classname=header_classname_spaced
    )
    gui_code_bloblist = [header,]
    trait_column_num = 1
    trait_row_num = 1
    trait_row_length = 9

    # Iterate leader_making and core_modifying traits
    # check for "councilor" traits and exclude "ruler" traits
    for rarity_level in RARITIES:
        for leader_trait in organized_traits_dict["councilor_editor_traits"][rarity_level]:
            trait_name = [*leader_trait][0]
            root = leader_trait[trait_name]
            if EXCLUDE_TRAITS_FROM_PARAGON_DLC.get(trait_name):
                print(f"Skipping {trait_name}...")
                continue

            if trait_req_subclass := root.get('required_subclass'):
                if trait_req_subclass != councilor_subclass:
                    print(
                        f"Skipping {trait_name}, req subclass is {trait_req_subclass}"
                        f" and this councilor is {councilor_subclass}"
                    )
                    continue

            trait_gui_code = gen_councilor_editor_traits_gui_code(
                councilor_type=councilor_type,
                gfx_sprite_name=root['gfx'],
                trait_name=trait_name,
                column_num=trait_column_num,
                row_num=trait_row_num,
                trait_type=root['rarity']
            )

            # Advance the x / y coordinates
            trait_column_num = trait_column_num + 1
            if trait_column_num > trait_row_length:
                trait_column_num = 1
                trait_row_num = trait_row_num + 1
            gui_code_bloblist.append(trait_gui_code)
    gui_code_bloblist.append(footer)
    return ''.join(gui_code_bloblist)

def determine_trait_background_sprite(rarity: str):
    root_gfx_name = "GFX_xvcv_mdlc_leader_trait_background"
    trait_background_add = f"{root_gfx_name}_green"
    trait_background_remove = f"{root_gfx_name}_red"
    if rarity == "veteran":
        trait_background_add = "GFX_xvcv_mdlc_leader_trait_background_veteran"
        trait_background_remove = f"{trait_background_add}_red"
    elif rarity == "paragon":
        trait_background_add = "GFX_xvcv_mdlc_leader_trait_background_destiny"
        trait_background_remove = f"{trait_background_add}_red"
    return trait_background_add, trait_background_remove

def gen_councilor_editor_traits_gui_code(
        councilor_type: str, trait_name: str, column_num: int, row_num: int,
        gfx_sprite_name: str, trait_type: str,
):
    trait_background_add, trait_background_remove = determine_trait_background_sprite(trait_type)

    return f"""
#{councilor_type} #{trait_name} #{trait_type}
containerWindowType = {{
    name = "oxr_mdlc_councilor_editor_{councilor_type}_traits_{trait_name}"
    position = {{ x = @oxr_mdlc_councilor_editor_trait_position_column_{column_num} y = @oxr_mdlc_councilor_editor_trait_position_row_{row_num} }}
    effectbuttonType = {{
        name = "oxr_mdlc_councilor_editor_{councilor_type}_traits_{trait_name}_add_bg"
        position = {{ x = @oxr_mdlc_councilor_editor_traits_background_offset_width y = @oxr_mdlc_councilor_editor_traits_background_offset_height }}
        spriteType = "{trait_background_add}"
        effect = "oxr_mdlc_councilor_editor_{councilor_type}_{trait_name}_add_button_effect"
    }}
    effectbuttonType = {{
        name = "oxr_mdlc_councilor_editor_{councilor_type}_traits_{trait_name}_add"
        spriteType = "{gfx_sprite_name}"
        effect = "oxr_mdlc_councilor_editor_{councilor_type}_{trait_name}_add_button_effect"
    }}
    effectbuttonType = {{
        name = "oxr_mdlc_councilor_editor_{councilor_type}_traits_{trait_name}_remove_bg"
        position = {{ x = @oxr_mdlc_councilor_editor_traits_background_offset_width y = @oxr_mdlc_councilor_editor_traits_background_offset_height }}
        spriteType = "{trait_background_remove}"
        effect = "oxr_mdlc_councilor_editor_{councilor_type}_{trait_name}_remove_button_effect"
    }}
    effectbuttonType = {{
        name = "oxr_mdlc_councilor_editor_{councilor_type}_traits_{trait_name}_remove"
        spriteType = "{gfx_sprite_name}"
        effect = "oxr_mdlc_councilor_editor_{councilor_type}_{trait_name}_remove_button_effect"
    }}
}}
"""

if __name__ == "__main__":
    print(CODE_HEADER)
    print("Generate Councilor Editor button effects code")
    
    for councilor in GESTALT_COUNCILOR_TYPES:
        source_file = GESTALT_COUNCILOR_SOURCE_TRAITS_FILES[councilor]
        gui_outfile = OUTPUT_FILES_DESTINATIONS[COUNCILOR_EDITOR]["gui"][councilor]

        traits_json_blob = ""
        with open(source_file, "r") as source_codegen_data:
            traits_json_blob = json_load(source_codegen_data)
        
        sys.stdout.write(f"Going to make {councilor} GUI code, writing to {gui_outfile}...")
        councilor_gui_blob = iterate_traits_generate_gui_code_for_councilor(
            councilor_type=councilor, organized_traits_dict=traits_json_blob
        )
        with open(gui_outfile, "wb") as councilor_gui_output_file:
            councilor_gui_output_file.write(
                councilor_gui_blob.encode('utf-8')
            )
        sys.stdout.write("Done."); print("")
    print("Done writing GUI code.")
