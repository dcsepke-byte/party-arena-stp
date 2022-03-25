class_name ItemLoader

const NEEDED_FILES := ["item.gd", "item.gdc"]
const ITEM_PATH := "res://plugins/items"

# Stores the path to each item.gd file of each subdirectory of ITEM_PATH.
var items := {}

var buyable_items := {}

func discover_item(filename: String) -> void:
	items[filename] = true
	if filename.ends_with(".gdc"):
		items[filename.substr(0, len(filename) - 1)] = true
	
	if load(filename).new().can_be_bought:
		buyable_items[filename] = true

func _init() -> void:
	print("Loading items...")
	PluginSystem.load_files_from_path(ITEM_PATH, NEEDED_FILES,
			self, "discover_item")
	print("Loading items finished")

	print_loaded_items()

func print_loaded_items() -> void:
	print("Loaded items:")
	for i in items:
		print("\t" + i)

func has_item(path: String) -> bool:
	return path in items

func get_loaded_items() -> Array:
	return items.keys()

func get_buyable_items() -> Array:
	return buyable_items.keys()
