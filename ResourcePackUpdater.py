import glob
import os
from json import load, dumps
import ctypes
from PIL import Image
import sys

changes = \
    {
        "door_acacia_upper": "acacia_door_top",
        "door_acacia_lower": "acacia_door_bottom",
        "leaves_acacia": "acacia_leaves",
        "log_acacia": "acacia_log",
        "log_acacia_top": "acacia_log_top",
        "planks_acacia": "acacia_planks",
        "sapling_acacia": "acacia_sapling",
        "rail_activator": "activator_rail",
        "rail_activator_powered": "activator_rail_on",
        "flower_allium": "allium",
        "stone_andesite": "andesite",
        "anvil_base": "anvil",
        "anvil_top_damaged_0": "anvil_top",
        "melon_stem_connected": "attached_melon_stem",
        "pumpkin_stem_connected": "attached_pumpkin_stem",
        "flower_houstonia": "azure_bluet",
        "beetroots_stage_0": "beetroots_stage0",
        "beetroots_stage_1": "beetroots_stage1",
        "beetroots_stage_2": "beetroots_stage2",
        "beetroots_stage_3": "beetroots_stage3",
        "door_birch_lower": "birch_door_bottom",
        "door_birch_upper": "birch_door_top",
        "leaves_birch": "birch_leaves",
        "log_birch": "birch_log",
        "log_birch_top": "birch_log_top",
        "planks_birch": "birch_planks",
        "sapling_birch": "birch_sapling",
        "concrete_black": "black_concrete",
        "concrete_powder_black": "black_concrete_powder",
        "glazed_terracotta_black": "black_glazed_terracotta",
        "glass_black": "black_stained_glass",
        "glass_pane_top_black": "black_stained_glass_pane_top",
        "hardened_clay_stained_black": "black_terracotta",
        "wool_colored_black": "black_wool",
        "concrete_blue": "blue_concrete",
        "concrete_powder_blue": "blue_concrete_powder",
        "glazed_terracotta_blue": "blue_glazed_terracotta",
        "flower_blue_orchid": "blue_orchid",
        "glass_blue": "blue_stained_glass",
        "glass_pane_top_blue": "blue_stained_glass_pane_top",
        "hardened_clay_stained_blue": "blue_terracotta",
        "wool_colored_blue": "blue_wool",
        "concrete_brown": "brown_concrete",
        "concrete_powder_brown": "brown_concrete_powder",
        "glazed_terracotta_brown": "brown_glazed_terracotta",
        "mushroom_brown": "brown_mushroom",
        "mushroom_block_skin_brown": "brown_mushroom_block",
        "glass_brown": "brown_stained_glass",
        "glass_pane_top_brown": "brown_stained_glass_pane_top",
        "hardened_clay_stained_brown": "brown_terracotta",
        "wool_colored_brown": "brown_wool",
        "carrots_stage_0": "carrots_stage0",
        "carrots_stage_1": "carrots_stage1",
        "carrots_stage_2": "carrots_stage2",
        "carrots_stage_3": "carrots_stage3",
        "anvil_top_damaged_1": "chipped_anvil_top",
        "quartz_block_chiseled": "chiseled_quartz_block",
        "quartz_block_chiseled_top": "chiseled_quartz_block_top",
        "red_sandstone_carved": "chiseled_red_sandstone",
        "sandstone_carved": "chiseled_sandstone",
        "stonebrick_carved": "chiseled_stone_bricks",
        "web": "cobweb",
        "cocoa_stage_0": "cocoa_stage0",
        "cocoa_stage_1": "cocoa_stage1",
        "cocoa_stage_2": "cocoa_stage2",
        "comparator_off": "comparator",
        "stonebrick_cracked": "cracked_stone_bricks",
        "red_sandstone_smooth": "cut_red_sandstone",
        "sandstone_smooth": "cut_sandstone",
        "concrete_cyan": "cyan_concrete",
        "concrete_powder_cyan": "cyan_concrete_powder",
        "glazed_terracotta_cyan": "cyan_glazed_terracotta",
        "glass_cyan": "cyan_stained_glass",
        "glass_pane_top_cyan": "cyan_stained_glass_pane_top",
        "hardened_clay_stained_cyan": "cyan_terracotta",
        "wool_colored_cyan": "cyan_wool",
        "anvil_top_damaged_2": "damaged_anvil_top",
        "flower_dandelion": "dandelion",
        "door_dark_oak_lower": "dark_oak_door_bottom",
        "door_dark_oak_upper": "dark_oak_door_top",
        "leaves_big_oak": "dark_oak_leaves",
        "log_big_oak": "dark_oak_log",
        "log_big_oak_top": "dark_oak_log_top",
        "planks_big_oak": "dark_oak_planks",
        "sapling_roofed_oak": "dark_oak_sapling",
        "prismarine_dark": "dark_prismarine",
        "deadbush": "dead_bush",
        "rail_detector": "detector_rail",
        "rail_detector_powered": "detector_rail_on",
        "stone_diorite": "diorite",
        "dispenser_front_horizontal": "dispenser_front",
        "dropper_front_horizontal": "dropper_front",
        "endframe_eye": "end_portal_frame_eye",
        "endframe_side": "end_portal_frame_side",
        "endframe_top": "end_portal_frame_top",
        "end_bricks": "end_stone_bricks",
        "farmland_dry": "farmland",
        "furnace_front_off": "furnace_front",
        "tallgrass": "grass",
        "grass_side": "grass_block_side",
        "grass_side_overlay": "grass_block_side_overlay",
        "grass_side_snowed": "grass_block_snow",
        "grass_top": "grass_block_top",
        "concrete_gray": "gray_concrete",
        "concrete_powder_gray": "gray_concrete_powder",
        "glazed_terracotta_gray": "gray_glazed_terracotta",
        "glass_gray": "gray_stained_glass",
        "glass_pane_top_gray": "gray_stained_glass_pane_top",
        "hardened_clay_stained_gray": "gray_terracotta",
        "wool_colored_gray": "gray_wool",
        "concrete_green": "green_concrete",
        "concrete_powder_green": "green_concrete_powder",
        "glazed_terracotta_green": "green_glazed_terracotta",
        "glass_green": "green_stained_glass",
        "glass_pane_top_green": "green_stained_glass_pane_top",
        "hardened_clay_stained_green": "green_terracotta",
        "wool_colored_green": "green_wool",
        "door_iron_lower": "iron_door_bottom",
        "door_iron_upper": "iron_door_top",
        "door_jungle_lower": "jungle_door_bottom",
        "door_jungle_upper": "jungle_door_top",
        "leaves_jungle": "jungle_leaves",
        "log_jungle": "jungle_log",
        "log_jungle_top": "jungle_log_top",
        "planks_jungle": "jungle_planks",
        "sapling_jungle": "jungle_sapling",
        "double_plant_fern_bottom": "large_fern_bottom",
        "double_plant_fern_top": "large_fern_top",
        "concrete_light_blue": "light_blue_concrete",
        "concrete_powder_light_blue": "light_blue_concrete_powder",
        "glazed_terracotta_light_blue": "light_blue_glazed_terracotta",
        "glass_light_blue": "light_blue_stained_glass",
        "glass_pane_top_light_blue": "light_blue_stained_glass_pane_top",
        "hardened_clay_stained_light_blue": "light_blue_terracotta",
        "wool_colored_light_blue": "light_blue_wool",
        "concrete_silver": "light_gray_concrete",
        "concrete_powder_silver": "light_gray_concrete_powder",
        "glazed_terracotta_silver": "light_gray_glazed_terracotta",
        "glass_silver": "light_gray_stained_glass",
        "glass_pane_top_silver": "light_gray_stained_glass_pane_top",
        "hardened_clay_stained_silver": "light_gray_terracotta",
        "wool_colored_silver": "light_gray_wool",
        "double_plant_syringa_bottom": "lilac_bottom",
        "double_plant_syringa_top": "lilac_top",
        "waterlily": "lily_pad",
        "concrete_lime": "lime_concrete",
        "glazed_terracotta_lime": "lime_glazed_terracotta",
        "concrete_powder_lime": "lime_concrete_powder",
        "glass_lime": "lime_stained_glass",
        "glass_pane_top_lime": "lime_stained_glass_pane_top",
        "hardened_clay_stained_lime": "lime_terracotta",
        "wool_colored_lime": "lime_wool",
        "concrete_magenta": "magenta_concrete",
        "concrete_powder_magenta": "magenta_concrete_powder",
        "glazed_terracotta_magenta": "magenta_glazed_terracotta",
        "glass_magenta": "magenta_stained_glass",
        "glass_pane_top_magenta": "magenta_stained_glass_pane_top",
        "hardened_clay_stained_magenta": "magenta_terracotta",
        "wool_colored_magenta": "magenta_wool",
        "melon_stem_disconnected": "melon_stem",
        "cobblestone_mossy": "mossy_cobblestone",
        "stonebrick_mossy": "mossy_stone_bricks",
        "nether_wart_stage_0": "nether_wart_stage0",
        "nether_wart_stage_1": "nether_wart_stage1",
        "nether_wart_stage_2": "nether_wart_stage2",
        "noteblock": "note_block",
        "door_wood_lower": "oak_door_bottom",
        "door_wood_upper": "oak_door_top",
        "leaves_oak": "oak_leaves",
        "log_oak_top": "oak_log_top",
        "log_oak": "oak_log",
        "planks_oak": "oak_planks",
        "sapling_oak": "oak_sapling",
        "observer_back_lit": "observer_back_on",
        "concrete_orange": "orange_concrete",
        "concrete_powder_orange": "orange_concrete_powder",
        "glazed_terracotta_orange": "orange_glazed_terracotta",
        "glass_orange": "orange_stained_glass",
        "glass_pane_top_orange": "orange_stained_glass_pane_top",
        "hardened_clay_stained_orange": "orange_terracotta",
        "flower_tulip_orange": "orange_tulip",
        "wool_colored_orange": "orange_wool",
        "flower_oxeye_daisy": "oxeye_daisy",
        "ice_packed": "packed_ice",
        "double_plant_paeonia_bottom": "peony_bottom",
        "double_plant_paeonia_top": "peony_top",
        "concrete_pink": "pink_concrete",
        "concrete_powder_pink": "pink_concrete_powder",
        "glazed_terracotta_pink": "pink_glazed_terracotta",
        "glass_pink": "pink_stained_glass",
        "glass_pane_top_pink": "pink_stained_glass_pane_top",
        "hardened_clay_stained_pink": "pink_terracotta",
        "flower_tulip_pink": "pink_tulip",
        "wool_colored_pink": "pink_wool",
        "piston_top_normal": "piston_top",
        "dirt_podzol_side": "podzol_side",
        "dirt_podzol_top": "podzol_top",
        "stone_andesite_smooth": "polished_andesite",
        "stone_diorite_smooth": "polished_diorite",
        "stone_granite_smooth": "polished_granite",
        "flower_rose": "poppy",
        "potatoes_stage_0": "potatoes_stage0",
        "potatoes_stage_1": "potatoes_stage1",
        "potatoes_stage_2": "potatoes_stage2",
        "potatoes_stage_3": "potatoes_stage3",
        "rail_golden": "powered_rail",
        "rail_golden_powered": "powered_rail_on",
        "prismarine_rough": "prismarine",
        "pumpkin_face_off": "carved_pumpkin",
        "pumpkin_stem_disconnected": "pumpkin_stem",
        "glazed_terracotta_purple": "purple_glazed_terracotta",
        "concrete_purple": "purple_concrete",
        "concrete_powder_purple": "purple_concrete_powder",
        "glass_purple": "purple_stained_glass",
        "glass_pane_top_purple": "purple_stained_glass_pane_top",
        "hardened_clay_stained_purple": "purple_terracotta",
        "wool_colored_purple": "purple_wool",
        "quartz_block_lines": "quartz_pillar",
        "rail_normal": "rail",
        "rail_normal_turned": "rail_corner",
        "concrete_red": "red_concrete",
        "concrete_powder_red": "red_concrete_powder",
        "glazed_terracotta_red": "red_glazed_terracotta",
        "mushroom_red": "red_mushroom",
        "mushroom_block_skin_red": "red_mushroom_block",
        "red_sandstone_normal": "red_sandstone",
        "glass_pane_top_red": "red_stained_glass_pane_top",
        "glass_red": "red_stained_glass",
        "wool_colored_red": "red_wool",
        "hardened_clay_stained_red": "red_terracotta",
        "flower_tulip_red": "red_tulip",
        "redstone_torch_on": "redstone_torch",
        "repeater_off": "repeater",
        "double_plant_rose_top": "rose_bush_top",
        "double_plant_rose_bottom": "rose_bush_bottom",
        "sandstone_normal": "sandstone",
        "door_spruce_lower": "spruce_door_bottom",
        "door_spruce_upper": "spruce_door_top",
        "leaves_spruce": "spruce_leaves",
        "log_spruce": "spruce_log",
        "log_spruce_top": "spruce_log_top",
        "planks_spruce": "spruce_planks",
        "sapling_spruce": "spruce_sapling",
        "stonebrick": "stone_bricks",
        "double_plant_sunflower_back": "sunflower_back",
        "double_plant_sunflower_bottom": "sunflower_bottom",
        "double_plant_sunflower_top": "sunflower_top",
        "double_plant_sunflower_front": "sunflower_front",
        "double_plant_grass_bottom": "tall_grass_bottom",
        "double_plant_grass_top": "tall_grass_top",
        "torch_on": "torch",
        "trip_wire_source": "tripwire_hook",
        "sponge_wet": "wet_sponge",
        "wheat_stage_0": "wheat_stage0",
        "wheat_stage_1": "wheat_stage1",
        "wheat_stage_2": "wheat_stage2",
        "wheat_stage_3": "wheat_stage3",
        "wheat_stage_4": "wheat_stage4",
        "wheat_stage_5": "wheat_stage5",
        "wheat_stage_6": "wheat_stage6",
        "wheat_stage_7": "wheat_stage7",
        "concrete_white": "white_concrete",
        "concrete_powder_white": "white_concrete_powder",
        "glazed_terracotta_white": "white_glazed_terracotta",
        "glass_white": "white_stained_glass",
        "glass_pane_top_white": "white_stained_glass_pane_top",
        "hardened_clay_stained_white": "white_terracotta",
        "flower_tulip_white": "white_tulip",
        "wool_colored_white": "white_wool",
        "concrete_yellow": "yellow_concrete",
        "concrete_powder_yellow": "yellow_concrete_powder",
        "glazed_terracotta_yellow": "yellow_glazed_terracotta",
        "glass_yellow": "yellow_stained_glass",
        "glass_pane_top_yellow": "yellow_stained_glass_pane_top",
        "hardened_clay_stained_yellow": "yellow_terracotta",
        "wool_colored_yellow": "yellow_wool",
        "quartz_block_lines_top": "quartz_pillar_top",
        "mushroom_block_skin_stem": "mushroom_stem",
        "mob_spawner": "spawner",
        "portal": "nether_portal",
        "acacia_door_lower": "acacia_door_bottom",
        "acacia_door_upper": "acacia_door_top",
        "birch_door_lower": "birch_door_bottom",
        "birch_door_upper": "birch_door_top",
        "brick": "bricks",
        "dark_oak_door_lower": "dark_oak_door_bottom",
        "dark_oak_door_upper": "dark_oak_door_top",
        "farmland_wet": "farmland_moist",
        "fire_layer_0": "fire_0",
        "fire_layer_1": "fire_1",
        "iron_door_lower": "iron_door_bottom",
        "iron_door_upper": "iron_door_top",
        "item_frame_background": "item_frame",
        "jungle_door_lower": "jungle_door_bottom",
        "jungle_door_upper": "jungle_door_top",
        "nether_brick": "nether_bricks",
        "oak_door_lower": "oak_door_bottom",
        "oak_door_upper": "oak_door_top",
        "pumpkin_face": "carved_pumpkin",
        "pumpkin_face_on": "jack_o_lantern",
        "quartz_ore": "nether_quartz_ore",
        "red_nether_brick": "red_nether_bricks",
        "redstone_lamp_off": "redstone_lamp",
        "shulker_top": "shulker_box_top",
        "shulker_top_black": "black_shulker_box_top",
        "shulker_top_blue": "blue_shulker_box_top",
        "shulker_top_brown": "brown_shulker_box_top",
        "shulker_top_cyan": "cyan_shulker_box_top",
        "shulker_top_gray": "gray_shulker_box_top",
        "shulker_top_green": "green_shulker_box_top",
        "shulker_top_light_blue": "light_blue_shulker_box_top",
        "shulker_top_light_gray": "light_gray_shulker_box_top",
        "shulker_top_lime": "lime_shulker_box_top",
        "shulker_top_magenta": "magenta_shulker_box_top",
        "shulker_top_orange": "orange_shulker_box_top",
        "shulker_top_pink": "pink_shulker_box_top",
        "shulker_top_purple": "purple_shulker_box_top",
        "shulker_top_red": "red_shulker_box_top",
        "shulker_top_white": "white_shulker_box_top",
        "shulker_top_yellow": "yellow_shulker_box_top",
        "spruce_door_lower": "spruce_door_bottom",
        "spruce_door_upper": "spruce_door_top",
        "stone_granite": "granite",
        "trip_wire": "tripwire",
        "trip_wire_hook": "tripwire_hook",
        "turtle_egg_not_cracked": "turtle_egg",
        "door_acacia": "acacia_door",
        "wooden_armorstand": "armor_stand",
        "potato_baked": "baked_potato",
        "door_birch": "birch_door",
        "dye_powder_white": "bone_meal",
        "book_normal": "book",
        "book_enchanted": "enchanted_book",
        "book_writable": "writable_book",
        "book_written": "written_book",
        "bow_standby": "bow",
        "bucket_empty": "bucket",
        "bucket_lava": "lava_bucket",
        "bucket_water": "water_bucket",
        "bucket_milk": "milk_bucket",
        "carrot_golden": "golden_carrot",
        "door_spruce": "spruce_door",
        "door_jungle": "jungle_door",
        "door_iron": "iron_door",
        "door_wood": "oak_door",
        "door_dark_oak": "dark_oak_door",
        "apple_golden": "golden_apple",
        "gold_axe": "golden_axe",
        "gold_boots": "golden_boots",
        "gold_chestplate": "golden_chestplate",
        "gold_helmet": "golden_helmet",
        "gold_hoe": "golden_hoe",
        "gold_horse_armor": "golden_horse_armor",
        "gold_leggings": "golden_leggings",
        "gold_pickaxe": "golden_pickaxe",
        "gold_shovel": "golden_shovel",
        "gold_sword": "golden_sword",
        "wood_axe": "wooden_axe",
        "wood_hoe": "wooden_hoe",
        "wood_pickaxe": "wooden_pickaxe",
        "wood_shovel": "wooden_shovel",
        "wood_sword": "wooden_sword",
        "fishing_rod_uncast": "fishing_rod",
        "minecart_hopper": "hopper_minecart",
        "minecart_tnt": "tnt_minecart",
        "minecart_command_block": "command_block_minecart",
        "minecart_normal": "minecart",
        "minecart_furnace": "furnace_minecart",
        "minecart_chest": "chest_minecart",
        "reeds": "sugar_cane",
        "record_11": "music_disc_11",
        "record_13": "music_disc_13",
        "record_blocks": "music_disc_blocks",
        "record_cat": "music_disc_cat",
        "record_chirp": "music_disc_chirp",
        "record_far": "music_disc_far",
        "record_mall": "music_disc_mall",
        "record_mellohi": "music_disc_mellohi",
        "record_stal": "music_disc_stal",
        "record_strad": "music_disc_strad",
        "record_wait": "music_disc_wait",
        "record_ward": "music_disc_ward",
        "slimeball": "slime_ball",
        "totem": "totem_of_undying",
        "map_empty": "map",
        "chicken_cooked": "cooked_chicken",
        "beef_cooked": "cooked_beef",
        "fish_cod_cooked": "cooked_cod",
        "porkchop_cooked": "cooked_porkchop",
        "mutton_cooked": "cooked_mutton",
        "rabbit_cooked": "cooked_rabbit",
        "fish_salmon_cooked": "cooked_salmon",
        "fish_cod_raw": "cod",
        "fish_pufferfish_raw": "pufferfish",
        "netherbrick": "nether_brick",
        "beef_raw": "beef",
        "chicken_raw": "chicken",
        "porkchop_raw": "porkchop",
        "mutton_raw": "mutton",
        "rabbit_raw": "rabbit",
        "fish_salmon_raw": "salmon",
        "fish_clownfish_raw": "clownfish",
        "redstone_dust": "redstone",
        "potion_bottle_drinkable": "glass_bottle",
        "potion_bottle_lingering": "lingering_potion",
        "potion_bottle_splash": "splash_potion",
        "potion_bottle_empty": "potion",
        "fireworks": "firework_rocket",
        "fireworks_charge": "firework_star",
        "fireball": "fire_charge",
        "fireworks_charge_overlay": "firework_star_overlay",
        "seeds_pumpkin": "pumpkin_seeds",
        "seeds_wheat": "wheat_seeds",
        "seeds_melon": "melon_seeds",
        "melon_speckled": "speckled_melon",
        "potato_poisonous": "poisonous_potato",
        "dye_powder_cyan": "cyan_dye",
        "dye_powder_gray": "gray_dye",
        "dye_powder_light_blue": "light_blue_dye",
        "dye_powder_silver": "light_gray_dye",
        "dye_powder_lime": "lime_dye",
        "dye_powder_magenta": "magenta_dye",
        "dye_powder_orange": "orange_dye",
        "dye_powder_pink": "pink_dye",
        "dye_powder_purple": "purple_dye",
        "dye_powder_yellow": "dandelion_yellow",
        "dye_powder_blue": "lapis_lazuli",
        "dye_powder_brown": "cocoa_beans",
        "dye_powder_black": "ink_sac",
        "dye_powder_red": "rose_red",
        "dye_powder_green": "cactus_green",
        "spider_eye_fermented": "fermented_spider_eye",
        "chorus_fruit_popped": "popped_chorus_fruit",
        "speckled_melon": "glistering_melon_slice",
        "clownfish": "tropical_fish",
        "clownfish_bucket": "tropical_fish_bucket",
        "melon": "melon_slice",
        "boat_acacia": "acacia",
        "boat_brich": "birch",
        "boat_darkoak": "dark_oak",
        "boat_jungle": "jungle",
        "boat_oak": "oak",
        "boat_spruce": "spruce",
        "creeper_armor": "charged_overlay",
        "endercrystal": "end_crystal",
        "llama": "creamy",
        "llama_brown": "brown",
        "llama_creamy": "creamy",
        "llama_gray": "gray",
        "llama_white": "white",
        "snowman": "snow_golem",
        "cod_mob": "cod",
        "salmon_mob": "salmon",
        "activator_rail_active_flat": "activator_rail_on",
        "activator_rail_active_raised_ne": "activator_rail_on_raised_ne",
        "activator_rail_active_raised_sw": "activator_rail_on_raised_sw",
        "activator_rail_flat": "activator_rail",
        "detector_rail_flat": "detector_rail",
        "detector_rail_powered_flat": "detector_rail_on",
        "detector_rail_powered_raised_ne": "detector_rail_on_raised_ne",
        "detector_rail_powered_raised_sw": "detector_rail_on_raised_sw",
        "golden_rail_active_flat": "powered_rail_on",
        "golden_rail_active_raised_ne": "powered_rail_on_raised_ne",
        "golden_rail_active_raised_sw": "powered_rail_on_raised_sw",
        "golden_rail_flat": "powered_rail",
        "golden_rail_raised_ne": "powered_rail_raised_ne",
        "golden_rail_raised_sw": "powered_rail_raised_sw",
        "normal_rail_flat": "rail",
        "normal_rail_raised_ne": "rail_raised_ne",
        "normal_rail_raised_sw": "rail_raised_sw",
        "half_slab": "slab",
        "upper_slab": "slab_top"
    }

changesBlockstates = \
    {
        "half=bottom": "type=bottom",
        "half=top": "type=top",
        "normal": ""
    }


# Takes in array and creates directory in order given
def create_dirs(dirs):
    for d in dirs:
        try:
            os.mkdir(d)
        except:
            continue


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#
# Deals with all model files
#

# Store paths to JSON files in list
models = glob.glob('**/assets/**/models/**/*.json', recursive=True)

# Put all JSON into separated list
json = []
for d in models:
    with open(d, "r") as f:
        json.append(load(f))

# Replace required values inside JSON list
json_edited = []
changes_keys = changes.keys()
for model in json:
    textures = [v for k,v in model.items() if k == "textures"]

    parent = [v for k,v in model.items() if k == "parent"][0]
    if parent:
        if str(parent).find("/") != -1:
            path, block = str(parent).split("/", 1)
            path = path + "/"
        else:
            block = str(parent)
            path = ""

        if block in changes_keys:
            parent = path + changes[block]

    if textures:
        textures = textures[0]
        for tex in textures:
            textures[tex] = str(textures[tex]).replace("blocks/", "block/")
            textures[tex] = str(textures[tex]).replace("items/", "item/")

        for tex, ref in textures.items():
            if str(ref).find("/") != -1:
                path, block = str(ref).split("/", 1)
                path = path + "/"
            else:
                block = str(ref)
                path = ""

            if block in changes_keys:
                textures[tex] = path + changes[block]
        model["textures"] = textures
        model["parent"] = parent
    json_edited.append(model)

# Output Edited JSON to files and rename them
for i in range(len(models)):
    # Dump edited JSON back into respective files
    with open(models[i], "w+") as f:
        f.write(dumps(json_edited[i], indent=4))

    # Rename file after if applicable
    path, file = os.path.split(models[i])
    file = file.replace(".json", "")
    if file in changes_keys:
        os.rename(models[i], path + "/" + changes[file] + ".json")

#
# deals with all PNGs and MCMetas
#

# Rename blocks->block and items->item subfolders
blocks_dir = glob.glob('**/assets/**/textures/blocks', recursive=True)
items_dir = glob.glob('**/assets/**/textures/items', recursive=True)

for d in blocks_dir:
    path = os.path.split(d)[0]
    os.rename(d, path + "/" + "block")

for d in items_dir:
    path = os.path.split(d)[0]
    os.rename(d, path + "/" + "item")

# Renames all PNG files
pngs = glob.glob('**/assets/**/textures/**/*.png', recursive=True)

for d in pngs:
    # Rename file if applicable
    path, file = os.path.split(d)
    file = file.replace(".png", "")
    if file in changes_keys:
        os.rename(d, path + "/" + changes[file] + ".png")

# Renames all png.mcmeta files
mcmeta = glob.glob('**/assets/**/textures/**/*.png.mcmeta', recursive=True)

for d in mcmeta:
    # Rename file if applicable
    path, file = os.path.split(d)
    file = file.replace(".png.mcmeta", "")
    if file in changes_keys:
        os.rename(d, path + "/" + changes[file] + ".png.mcmeta")

#
# Deals with all blockstate files
#

# Store paths to JSON files in list
blockstates = glob.glob('**/assets/**/blockstates/**/*.json', recursive=True)

# Put all JSON into separated list
json = []
for d in blockstates:
    with open(d, "r") as f:
        json.append(load(f))

# Replace required values inside JSON list
json_edited = []
for blockstate in json:
    variants = [v for k,v in blockstate.items() if k == "variants"]
    if variants:
        variants = variants[0]

        # Replace blockstate with 1.13 blockstate, e.g. "half=top" -> "type=top"
        models_key = [k for k, v in variants.items()]
        for mk in models_key:
            if mk in changesBlockstates:
                variants[changesBlockstates.get(mk)] = variants[mk]
                del variants[mk]

        # Changes pointer to model, and adds "block/" if necessary
        model_ref = [v for k,v in variants.items()]

        for modelLists in model_ref:
            if isinstance(modelLists, (list,)):
                for dic in modelLists:
                    model_name = [v for k,v in dic.items() if k == "model"][0]
                    if model_name in changes_keys:
                        dic["model"] = "block/" + changes[model_name]
                    elif "block/" not in model_name:
                        dic["model"] = "block/" + model_name
            else:
                model_name = [v for k, v in modelLists.items() if k == "model"][0]
                if model_name in changes_keys:
                    modelLists["model"] = "block/" + changes[model_name]
                elif "block/" not in model_name:
                    modelLists["model"] = "block/" + model_name

    json_edited.append(blockstate)

# Output Edited JSON to files and rename them
for i in range(len(blockstates)):
    # Dump edited JSON back into respective files
    with open(blockstates[i], "w+") as f:
        f.write(dumps(json_edited[i], indent=4))

    # Rename file after if applicable
    path, file = os.path.split(blockstates[i])
    file = file.replace(".json", "")
    if file in changes_keys:
        os.rename(blockstates[i], path + "/" + changes[file] + ".json")

#
# Deals with pack.mcmeta
#

pack_metas = glob.glob('**/assets/**/pack.mcmeta', recursive=True)
json_edited = []
for pack in pack_metas:
    with open(pack, "r+") as f:
        json_edited.append(load(f))

for json in json_edited:
    pack = [v for k,v in json.items() if k == "pack"][0]
    pack["pack_format"] = 4

for i in range(len(pack_metas)):
    with open(pack_metas[i], "w+") as f:
        f.write(dumps(json_edited[i], indent=4))


#
# Deals with particle file 1.13+
#

base_particle_path = resource_path("resources\\particles_base.png")
base_particle = Image.open(base_particle_path)

particles = glob.glob("**/assets/**/textures/particle/particles.png", recursive=True)

for particle_path in particles:
    old_particle_path = os.path.dirname(particle_path) + "\\particlesTEMP.png"
    new_particle_path = os.path.dirname(particle_path) + "\\particles.png"

    image_check = Image.open(particle_path)
    width = Image.Image.size.getter(image_check)
    Image.Image.close(image_check)

    if width != 256:
        os.rename(particle_path, old_particle_path)

        Image.Image.save(base_particle, new_particle_path, 'PNG')

        foreground = Image.open(old_particle_path)
        background = Image.open(new_particle_path)

        Image.Image.paste(background, foreground, (0, 0), foreground)
        Image.Image.save(background, new_particle_path)

        os.remove(old_particle_path)


ctypes.windll.user32.MessageBoxW(0, u"Resource Pack updated to 1.13 successfully!", u"Conversion Complete", 0)