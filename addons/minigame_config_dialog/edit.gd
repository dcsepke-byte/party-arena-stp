@tool
extends PopupPanel

const MINIGAME_TYPES := ["1v3", "2v2", "Duel", "FFA", "GnuCoop", "GnuSolo", "NolokCoop", "NolokSolo"]

const PRESETS := [
	{
		"actions": ["spacer", "up", "spacer", "left", "down", "right"],
		"text": "MINIGAME_ACTION_MOVEMENT"
	}]

var path: String
var file_dialog: EditorFileDialog

func _enter_tree():
	file_dialog = EditorFileDialog.new()
	file_dialog.current_path = path
	file_dialog.access = EditorFileDialog.ACCESS_RESOURCES
	add_child(file_dialog)

func _ready():
	$VBoxContainer/HBoxContainer2/MainScene.pressed.connect(_set_file.bind($VBoxContainer/HBoxContainer2/MainScene, FileDialog.FILE_MODE_OPEN_FILE))
	$VBoxContainer/HBoxContainer3/Screenshot.pressed.connect(_set_file.bind($VBoxContainer/HBoxContainer3/Screenshot, FileDialog.FILE_MODE_OPEN_FILE))
	$VBoxContainer/HBoxContainer4/Translations.pressed.connect(_set_file.bind($VBoxContainer/HBoxContainer4/Translations, FileDialog.FILE_MODE_OPEN_DIR))
	$VBoxContainer/HBoxContainer7/Toolbox/Presets.get_popup().index_pressed.connect(_add_preset)

func load_from_file():
	var minigame_loader := load("res://common/scripts/loader/minigame_loader.gd")
	var config = minigame_loader.parse_file(path)
	if not config:
		return
	$VBoxContainer/HBoxContainer/Name.text = config.name
	$VBoxContainer/HBoxContainer2/MainScene.text = config.scene_path
	if config.image_path:
		$VBoxContainer/HBoxContainer3/Screenshot.text = config.image_path
	else:
		$VBoxContainer/HBoxContainer3/Screenshot.text = "..."
	if config.translation_directory:
		$VBoxContainer/HBoxContainer4/Translations.text = config.translation_directory
	else:
		$VBoxContainer/HBoxContainer4/Translations.text = "..."
	$VBoxContainer/HBoxContainer6/Description.text = config.description
	
	$VBoxContainer/HBoxContainer5/Type.deselect_all()
	for type in config.type:
		var idx = MINIGAME_TYPES.find(type)
		if idx >= 0:
			$VBoxContainer/HBoxContainer5/Type.select(idx, false)
	
	for child in $VBoxContainer/HBoxContainer7/List/ScrollContainer/VBoxContainer.get_children():
		child.free()
	for control in config.controls:
		add_control(control)

func fix_columns(parent: GridContainer):
	parent.columns = (parent.get_child_count() + 1) / 2

func add_action(parent: GridContainer, name: String):
	var entry: Node = load("res://addons/minigame_config_dialog/action_entry.tscn").instantiate()
	entry.get_node("Name").text = name
	entry.tree_exited.connect(fix_columns.bind(parent))
	parent.add_child(entry)
	fix_columns(parent)

func add_control(control: Dictionary):
	var template: Node = load("res://addons/minigame_config_dialog/control_entry.tscn").instantiate()
	var popup: PopupMenu = template.get_node("Add").get_popup()
	popup.index_pressed.connect(_add_action.bind(template.get_node("Actions"), popup))
	if "actions" in control:
		var parent := template.get_node("Actions")
		for action in control.actions:
			add_action(parent, action)
	if "text" in control:
		template.get_node("Text").text = control.text
	if "team" in control:
		template.get_node("Team").select(control.team + 1)
	$VBoxContainer/HBoxContainer7/List/ScrollContainer/VBoxContainer.add_child(template)

func _set_file(button, mode):
	file_dialog.mode = mode
	file_dialog.popup_centered_clamped(Vector2(600, 500))
	if mode == FileDialog.FILE_MODE_OPEN_FILE:
		button.text = await file_dialog.file_selected
	else:
		button.text = await file_dialog.dir_selected

func _on_Save_pressed():
	var types := []
	for i in $VBoxContainer/HBoxContainer5/Type.get_selected_items():
		types.append(MINIGAME_TYPES[i])
	if $VBoxContainer/HBoxContainer2/MainScene.text == "...":
		$AcceptDialog.dialog_text = "No main scene selected. Config was not saved."
		$AcceptDialog.popup_centered()
		return
	if types.is_empty():
		$AcceptDialog.dialog_text = "No minigame types selected. Config was not saved."
		$AcceptDialog.popup_centered()
		return
	
	var file := FileAccess.open(path, FileAccess.WRITE)
	
	var dict := {}
	dict["name"] = $VBoxContainer/HBoxContainer/Name.text
	dict["scene_path"] = $VBoxContainer/HBoxContainer2/MainScene.text
	if $VBoxContainer/HBoxContainer3/Screenshot.text != "...":
		dict["image_path"] = $VBoxContainer/HBoxContainer3/Screenshot.text
	if $VBoxContainer/HBoxContainer4/Translations.text != "...":
		dict["translation_directory"] = $VBoxContainer/HBoxContainer4/Translations.text
	dict["type"] = types
	dict["description"] = $VBoxContainer/HBoxContainer6/Description.text
	var controls := []
	for child in $VBoxContainer/HBoxContainer7/List/ScrollContainer/VBoxContainer.get_children():
		var actions := []
		for action in child.get_node("Actions").get_children():
			actions.append(action.get_node("Name").text)
		controls.append({"actions": actions, "text": child.get_node("Text").text})
		if child.get_node("Team").selected != 0:
			controls[-1].team = child.get_node("Team").selected - 1
	dict["controls"] = controls
	file.store_string(JSON.stringify(dict, "\t"))
	file.close()
	hide()

func _add_action(idx: int, parent, popup):
	add_action(parent, popup.get_item_text(idx))

func _add_preset(idx: int):
	add_control(PRESETS[idx])

func _on_Add_pressed():
	add_control({})

func _on_PopupPanel_about_to_show():
	$VBoxContainer/HBoxContainer/Name.grab_click_focus()

func _on_Close_pressed():
	hide()
