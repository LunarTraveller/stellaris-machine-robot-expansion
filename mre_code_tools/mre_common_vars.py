import os
from datetime import datetime

TRAIT_MODIFIER_KEYS = (
    "army_modifier",
    "councilor_modifier",
    "fleet_modifier",
    "modifier",
    "planet_modifier",
    "sector_modifier",
    "self_modifier",
    "triggered_army_modifier",
    "triggered_councilor_modifier",
    "triggered_fleet_modifier",
    "triggered_planet_modifier",
    "triggered_sector_modifier",
    "triggered_self_modifier",
)

AUTOGENERATED_HEADER = f"""
######################################
# AUTOGENERATED on {str(datetime.now())}                #
######################################
"""

MISSING = "MISSING_VALUE"
PLACEHOLDER = "PLACEHOLDER_VALUE"

BASE_TRAIT_FILES = (
    "00_generic_leader_traits.txt",
    "00_admiral_traits.txt",
    "00_general_traits.txt",
    "00_governor_traits.txt",
    "00_scientist_traits.txt",
    "00_starting_ruler_traits.txt"
)

BUILD_FOLDER = os.path.join(
    os.getcwd(),
    'build'
)

BUTTON_EFFECTS_FOLDER = os.path.join(
    os.getcwd(),
    'common', 'button_effects'
)

CODE_HEADER = "0xRetro Machine & Robot Expansion Mod Codegen Tools"

DEFAULT_UPPERCASE_MODIFIERS_MAP_FILES = [
    os.path.join(BUILD_FOLDER, 'modifiers_l_english_upper.json'),
    os.path.join(BUILD_FOLDER, 'megacorp_l_english_upper.json'),
    os.path.join(BUILD_FOLDER, 'paragon_2_l_english_upper.json')
]


DLC_REQUIREMENT_KEYS = {
    "has_overlord_dlc",
    "has_ancrel",
}


# These subclasses can't be added to the ruler because of a NAND with gestalt consciousness
# Or they just don't work (ruler can't be admiral/general)
EXCLUDE_SUBCLASSES_FROM_CORE_MODIFYING = {
    "subclass_official_governor": 1,
    "subclass_official_delegate":1,
    "subclass_scientist_explorer":1,
    "subclass_scientist_governor":1,
    "subclass_scientist_scholar":1,
    "subclass_commander_general": 1,
    "subclass_commander_governor": 1,
    "subclass_commander_admiral": 1,
}


# The game won't let us add these traits to the ruler. I even tried using console commands.
# All of the expertise traits don't have any effect when applied to a ruler.
EXCLUDE_TRAITS_FROM_CORE_MODIFYING = {
    "leader_trait_adaptable_2":1,
    "trait_ruler_eye_for_talent_2":1,
    "leader_trait_resilient_2":1,
    "leader_trait_gifted_2":1,
    "leader_trait_adventurous_spirit_3":1,
    "leader_trait_expertise_archaeostudies_3":1,
    "leader_trait_expertise_biology_3":1,
    "leader_trait_expertise_computing_3":1,
    "leader_trait_expertise_field_manipulation_3":1,
    "leader_trait_expertise_industry_3":1,
    "leader_trait_expertise_materials_3":1,
    "leader_trait_expertise_military_theory_3":1,
    "leader_trait_expertise_new_worlds_3":1,
    "leader_trait_expertise_particles_3":1,
    "leader_trait_expertise_propulsion_3":1,
    "leader_trait_expertise_psionics_3":1,
    "leader_trait_expertise_statecraft_3":1,
    "leader_trait_expertise_voidcraft_3":1,
    "trait_ruler_destroyer_focus":1,  # ship focuses are blocked in Paragons DLC
    "trait_ruler_cruiser_focus":1,    # and leader builder isnt enabled without Paragons
    "trait_ruler_corvette_focus":1,   # no reason to add these to the mod
    "trait_ruler_battleship_focus":1,
    "leader_trait_fleet_logistician":1,
}

EXCLUDE_TRAITS_FROM_PARAGON_DLC = {
    "trait_ruler_destroyer_focus":1,  # ship focuses are blocked in Paragons DLC
    "trait_ruler_cruiser_focus":1,    # and leader builder isnt enabled without Paragons
    "trait_ruler_corvette_focus":1,   # no reason to add these to the mod
    "trait_ruler_battleship_focus":1,
    "leader_trait_fleet_logistician":1,
}
EXCLUDE_TRAITS_FROM_COUNCILOR_EDITOR = {
    "leader_trait_adaptable_2":1,
    "trait_ruler_eye_for_talent_2":1,
    "leader_trait_resilient_2":1,
    "leader_trait_gifted_2":1,
}

FILE_NUM_PREFIXES = {
    "yaml_to_json": "00",
    "json_to_simple_traits_list": "10",
    "filtered_traits": "20",
    "gui": "30",
    "triggers": "40",
    "effects": "50",
    "localisation": "60",
    "maps": "70",  # traits w machine localisation, uppercase map
}

""" On a bad yaml merge there will be other random stuff in the modifier dict
on occasion. so make a list of what should get kicked out of modifiers """
GARBAGE_MODIFIERS = (
    "inline_script",
    "script",
    "FIELD",
    "TIER",
    "mult",
)

GENERATED_CODE_TYPES = (
  "effects",
  "gui",
  "tooltips",
)

GESTALT_COUNCILOR_TYPES = (
    "regulatory", "cognitive", "growth", "legion"
)
GESTALT_COUNCILOR_CLASS_MAP = {
    "regulatory": "official",
    "cognitive": "scientist",
    "growth": "official",
    "legion": "commander"
}
GESTALT_COUNCILOR_SUBCLASS_MAP = {
    # These are fixed at game start
    "regulatory": "subclass_official_diplomacy_councilor",
    "cognitive": "subclass_scientist_councilor",
    "growth": "subclass_official_economy_councilor",
    "legion": "subclass_commander_councilor"
}

GESTALT_COUNCILOR_SOURCE_TRAITS_FILES = {
    "regulatory": os.path.join(BUILD_FOLDER, "99_mre_official_traits_for_codegen.json"),
    "growth": os.path.join(BUILD_FOLDER, "99_mre_official_traits_for_codegen.json"),
    "legion": os.path.join(BUILD_FOLDER, "99_mre_commander_traits_for_codegen.json"),
    "cognitive": os.path.join(BUILD_FOLDER,  "99_mre_scientist_traits_for_codegen.json"),
}

GUI_HEADER_TEXT = """
##########################################################
#       START COPY/PASTE GENERATED GUI TRAITS CODE FOR:  #
#					{classname}						 #
#   generated on {now}
##########################################################
"""
GUI_FOOTER_TEXT = """
##########################################################
#       END COPY/PASTE GENERATED GUI TRAITS CODE FOR:  #
#					{classname}						 #
##########################################################
"""

# Files created by mre_process_traits_for_codegen
INPUT_FILES_FOR_CODEGEN = (
    "99_mre_commander_traits_for_codegen.json",
    "99_mre_official_traits_for_codegen.json",
    "99_mre_scientist_traits_for_codegen.json"
)

LOCALISATION_HEADER = "l_english:\n"

# TODO: Write all the English localisations to all the other language folders!!
LOCALISATION_FOLDER = os.path.join(
    os.getcwd(),
    'localisation',
    'english'
)

LEADER_CLASSES = (
    "commander", "official", "scientist"
)

LEADER_SUBCLASSES = (
    "subclass_commander_general",
    "subclass_commander_councilor",
    "subclass_commander_governor",
    "subclass_commander_admiral",
    "subclass_scientist_explorer",
    "subclass_scientist_councilor",
    "subclass_scientist_governor",
    "subclass_scientist_scholar",
    "subclass_official_economy_councilor",
    "subclass_official_diplomacy_councilor",
    "subclass_official_governor",
    "subclass_official_delegate",
)

# Used to add a comment in code to refer to the in-game name for the subclass
LEADER_SUBCLASSES_NAMES = {
    "subclass_commander_general": "general",
    "subclass_commander_councilor": "strategist",
    "subclass_commander_governor": "commissioner",
    "subclass_commander_admiral": "admiral",
    "subclass_scientist_explorer": "explorer",
    "subclass_scientist_councilor": "statistician",
    "subclass_scientist_governor": "analyst",
    "subclass_scientist_scholar": "scholar",
    "subclass_official_economy_councilor": "advisor",
    "subclass_official_diplomacy_councilor": "ambassador",
    "subclass_official_governor": "industrialist",
    "subclass_official_delegate": "delegate"
}

MACHINE_LOCALISATIONS_MAPFILE = "98_traits_with_machine_localisations.json"


# Files created by sort_merge_traits_files
PIPELINE_OUTPUT_FILES = [
    f"00_mre_{leader_class}_traits.json" for leader_class in LEADER_CLASSES
]

LEADER_MAKING = "leader_making"
CORE_MODIFYING = "core_modifying"
COUNCILOR_EDITOR = "councilor_editor"

""" These traits are set up in some way as to break the expectation that the tier 3 requirements
are locked in by tier 1 and 2. These traits are serious exceptions and shouldnt be added to
the GUI. For example maniacal_3 is fine as a scientist trait but NOT as a commander trait. """
SKIP_TRAIT_FOR_SUBCLASS_LIST = {
    "leader_trait_maniacal_3": "commander",
}

""" These traits are skipped entirely during the logic that decides whether a trait
should go to leader-making or core-modifying """
TRAITS_TO_EXCLUDE = {
    # commander
    "leader_trait_clone_army_commander":1,  # Cant have clone origin with machines
    "leader_trait_clone_army_fertile_commander":1,
    "leader_trait_clone_army_full_commander":1,
    "leader_trait_dragonslayer":1,  # Given via event
    "leader_trait_eager_2":1, # Cant effect leader-building/core-mod
    "leader_trait_entrepreneur":1, # consumer goods-related trait,
    "trait_imperial_heir":1, # Gestalt isnt an imperial form of government (but they can form the Imperium)
    "leader_trait_academia_recruiter":1,  # requires materialist ethic,
    "leader_trait_shroud_preacher":1,  # requires spiritualist ethic,
    "leader_trait_tzrynn_tithe":1, # given via event
    "leader_trait_emotional_support_pet":1,
    "leader_trait_towel":1,  # given via event,
    "leader_trait_percussive_maintainer":1,  #given via event ancrel.12005
    "leader_trait_intemporal":1,  #given via event,
    "leader_trait_robotist":1,  # just annoying to deal with code-wise
}

""" Our trick to prepend mre_ to modifier names doesn't always work automatically.
Some of these modifiers weren't in the default files,
so these are special exceptions. Or they just have different tooltip names
than what the modifier is.
TODO: hook these into tooltip code gen """
TOOLTIP_LOOKUP_MAP = {
    "mod_leader_lifespan_add": "MOD_LEADER_LIFESPAN_ADD",
    "mod_spy_network_daily_value_mult": "MOD_SPY_NETWORK_DAILY_VALUE_MULT",
    "mod_terraform_speed_mult": "MOD_COUNTRY_TERRAFORM_SPEED_MULT",
    "mod_monthly_loyalty_from_subjects": "MOD_MONTHLY_LOYALTY_GAIN_FROM_SUBJECTS",
    "mod_intel_decryption_add": "MOD_INTEL_DECRYPTION_ADD",
    "mod_intel_encryption_add": "MOD_INTEL_ENCRYPTION_ADD",
    "mod_envoys_add": "MOD_COUNTRY_ENVOYS_ADD",
    "mod_ship_archaeological_site_excavation_speed_mult": "MOD_SHIP_ARCHAEOLOGICAL_SITE_EXCAVATION_SPEED_MULT",
    "mod_all_technology_research_speed": "MOD_COUNTRY_ALL_TECH_RESEARCH_SPEED",
    "mod_num_tech_alternatives_add": "MOD_COUNTRY_NUM_TECH_ALTERNATIVES_ADD",  # leader_trait_inquisitive_3
    "mod_ship_archaeological_site_clues_add": "MOD_SHIP_ARCHAEOLOGICAL_SITE_CLUES_ADD",
    "mod_ship_hyperlane_range_add": "MOD_SHIP_HYPERLANE_RANGE_ADD",
    "mod_fleet_mia_time_mult": "MOD_FLEET_MIA_TIME_MULT",
    "mod_ship_friendly_territory_evasion_mult": "MOD_SHIP_FRIENDLY_TERRITORY_EVASION_MULT",
    "mod_ship_friendly_territory_fire_rate_mult": "MOD_SHIP_FRIENDLY_TERRITORY_FIRE_RATE_MULT",
    "mod_ship_friendly_territory_shield_add": "MOD_SHIP_FRIENDLY_TERRITORY_SHIELD_ADD",
    "mod_damage_vs_rival_mult": "MOD_DAMAGE_VS_RIVAL_MULT",
    "mod_empire_size_districts_mult": "MOD_EMPIRE_SIZE_DISTRICTS_MULT", #official #leader_trait_urbanist
    "mod_ship_emergency_ftl_mult": "MOD_SHIP_EMERGENCY_FTL_MIN_DAYS_ADD",
}

""" Some tooltips have localisation keys only in the yml for that DLC, and arent in 
base stellaris. So they show up empty in the leadermaking UI because the game can't find
them because that DLC is not enabled. And there is no DLC-required flag in the trait itself

Use this information when building button effects for a trait, somehow"""
HIDDEN_DLC_REQUIREMENTS = {
    "mod_planet_jobs_food_produces_mult": "Megacorp",  # implement in potential: host_has_dlc = "Megacorp"
    "mod_planet_administrators_unity_produces_mult": "Megacorp",
    "mod_planet_technician_energy_produces_mult": "Megacorp",
    "mod_weapon_archaeotech_weapon_damage_mult": "Ancient Realms",  # has_ancrel
    "mod_weapon_role_artillery_weapon_damage_mult": "Paragons",
    "mod_weapon_type_strike_craft_weapon_damage_mult": "Paragons",
    "mod_ships_upkeep_mult": "Megacorp",
    "mod_spy_network_daily_value_mult": "Nemesis",  # leader_trait_spycraft_2
    "mod_intel_decryption_add": "Nemesis",  # leader_trait_shadow_broker_3
    "mod_intel_encryption_add": "Nemesis",  # leader_trait_shadow_broker_3
    "mod_ship_archaeological_site_clues_add": "Ancient Realms",
    "mod_ship_friendly_territory_evasion_mult": "Overlord",
    "mod_ship_friendly_territory_fire_rate_mult": "Overlord",
    "mod_ship_friendly_territory_shield_add": "Overlord",
}
# Can make special cases this way
TRAITS_REQUIRING_DLC = {
    "leader_trait_expertise_archaeostudies_3": "has_ancrel",
    "leader_trait_archaeo_specialization_3": "has_ancrel",
    "leader_trait_explorer_cloaking_focus_3": "has_first_contact_dlc",
}

# The descriptions for some traits isn't obvious, like the trait which adds
# +2 picks, some people thought it meant 2 more traits total
SPECIAL_HELP_TEXT = {
    "leader_trait_gifted_2": "This trait increases the number of trait pick options at level up. It does not raise the maximum number of traits that can be stacked on a leader."
}

OUTPUT_FILE_BUTTON_FX_NAME = "xvcv_mdlc_button_effects_{feature}_{leader_class}_customgui.txt"
OUTPUT_FILE_LOCALISATION_NAME = "xvcv_mdlc_l_english_{feature}_{leader_class}_customgui.yml"
COUNCILOR_EDITOR_BUTTON_FX_FILENAME = "oxr_mdlc_button_effects_councilor_editor_{councilor_type}_customgui.txt"
COUNCILOR_EDITOR_GUI_FILENAME = "{prefix}_oxr_mdlc_councilor_editor_{councilor_type}_gui_code.txt"


""" We will write directly to these files during the code generation workflow """
OUTPUT_FILES_DESTINATIONS = {
    "core_modifying": {
        "effects": {
            "commander": os.path.join(
                BUTTON_EFFECTS_FOLDER,
                OUTPUT_FILE_BUTTON_FX_NAME.format(
                    feature="core_modifying", leader_class="commander"
                )
            ),
            "official": os.path.join(
                BUTTON_EFFECTS_FOLDER,
                OUTPUT_FILE_BUTTON_FX_NAME.format(
                    feature="core_modifying", leader_class="official"
                )
            ),
            "scientist": os.path.join(
                BUTTON_EFFECTS_FOLDER,
                OUTPUT_FILE_BUTTON_FX_NAME.format(
                    feature="core_modifying", leader_class="scientist"
                )
            ),
        },
        "tooltips": {
            "commander": os.path.join(
                LOCALISATION_FOLDER,
                OUTPUT_FILE_LOCALISATION_NAME.format(
                    feature="core_modifying", leader_class="commander"
                )
            ),
            "official": os.path.join(
                LOCALISATION_FOLDER,
                OUTPUT_FILE_LOCALISATION_NAME.format(
                    feature="core_modifying", leader_class="official"
                )
            ),
            "scientist": os.path.join(
                LOCALISATION_FOLDER,
                OUTPUT_FILE_LOCALISATION_NAME.format(
                    feature="core_modifying", leader_class="scientist"
                )
            ),
        },
    },
    "leader_making": {
        "effects": {
            "commander": os.path.join(
                BUTTON_EFFECTS_FOLDER,
                OUTPUT_FILE_BUTTON_FX_NAME.format(
                    feature="leader_making", leader_class="commander"
                )
            ),
            "official": os.path.join(
                BUTTON_EFFECTS_FOLDER,
                OUTPUT_FILE_BUTTON_FX_NAME.format(
                    feature="leader_making", leader_class="official"
                )
            ),
            "scientist": os.path.join(
                BUTTON_EFFECTS_FOLDER,
                OUTPUT_FILE_BUTTON_FX_NAME.format(
                    feature="leader_making", leader_class="scientist"
                )
            ),
        },
        "tooltips": {
            "commander": os.path.join(
                LOCALISATION_FOLDER,
                OUTPUT_FILE_LOCALISATION_NAME.format(
                    feature="leader_making", leader_class="commander"
                )
            ),
            "official": os.path.join(
                LOCALISATION_FOLDER,
                OUTPUT_FILE_LOCALISATION_NAME.format(
                    feature="leader_making", leader_class="official"
                )
            ),
            "scientist": os.path.join(
                LOCALISATION_FOLDER,
                OUTPUT_FILE_LOCALISATION_NAME.format(
                    feature="leader_making", leader_class="scientist"
                )
            ),
        },
    },
    "councilor_editor": {
        "effects": {
            "regulatory": os.path.join(
                BUTTON_EFFECTS_FOLDER,
                COUNCILOR_EDITOR_BUTTON_FX_FILENAME.format(
                    councilor_type="regulatory"
                )
            ),
            "cognitive": os.path.join(
                BUTTON_EFFECTS_FOLDER,
                COUNCILOR_EDITOR_BUTTON_FX_FILENAME.format(
                    councilor_type="cognitive"
                )
            ),
            "growth": os.path.join(
                BUTTON_EFFECTS_FOLDER,
                COUNCILOR_EDITOR_BUTTON_FX_FILENAME.format(
                    councilor_type="growth"
                )
            ),
            "legion": os.path.join(
                BUTTON_EFFECTS_FOLDER,
                COUNCILOR_EDITOR_BUTTON_FX_FILENAME.format(
                    councilor_type="legion"
                )
            ),
        },
        "gui": {
            "regulatory": os.path.join(
                BUILD_FOLDER,
                COUNCILOR_EDITOR_GUI_FILENAME.format(
                    councilor_type="regulatory",
                    prefix=FILE_NUM_PREFIXES["gui"]
                )
            ),
            "cognitive": os.path.join(
                BUILD_FOLDER,
                COUNCILOR_EDITOR_GUI_FILENAME.format(
                    councilor_type="cognitive",
                    prefix=FILE_NUM_PREFIXES["gui"]
                )
            ),
            "growth": os.path.join(
                BUILD_FOLDER,
                COUNCILOR_EDITOR_GUI_FILENAME.format(
                    councilor_type="growth",
                    prefix=FILE_NUM_PREFIXES["gui"]
                )
            ),
            "legion": os.path.join(
                BUILD_FOLDER,
                COUNCILOR_EDITOR_GUI_FILENAME.format(
                    councilor_type="legion",
                    prefix=FILE_NUM_PREFIXES["gui"]
                )
            ),
        },
    }
}


RARITIES = ("common", "veteran", "paragon")


""" These traits are known to have garbage in the modifiers
I don't mean the traits are terrible, I mean they have GARBAGE_MODIFIERS """
TRAITS_WITH_GARBAGE_MODIFIERS = {
    "leader_trait_expertise_new_worlds_3":1,
}

UNICORN = '''
                \\
                 \%,     ,'     , ,.
                  \%\,';/J,";";";;,,.
     ~.------------\%;((`);)));`;;,.,-----------,~
    ~~:           ,`;@)((;`,`((;(;;);;,`         :~~
   ~~ :           ;`(@```))`~ ``; );(;));;,      : ~~
  ~~  :            `X `(( `),    (;;);;;;`       :  ~~
 ~~~~ :            / `) `` /;~   `;;;;;;;);,     :  ~~~~
~~~~  :           / , ` ,/` /     (`;;(;;;;,     : ~~~~
  ~~~ :          (o  /]_/` /     ,);;;`;;;;;`,,  : ~~~
   ~~ :           `~` `~`  `      ``;,  ``;" ';, : ~~
    ~~:                             `'   `'  `'  :~~
     ~`-----------------------------------------`~
'''