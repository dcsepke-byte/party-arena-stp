extends Control

signal item_selected(idx)

func select_item(player) -> void:
	var i := 0
	while i < len(player.items):
		var node = get_node("Item%d" % (i + 1))
		var item = player.items[i]
		node.texture_normal = item.icon

		if node.is_connected("focus_entered", self, "_on_focus_entered"):
			node.disconnect("focus_entered", self, "_on_focus_entered")
		if node.is_connected("focus_exited", self, "_on_focus_exited"):
			node.disconnect("focus_exited", self, "_on_focus_exited")
		if node.is_connected("mouse_entered", self, "_on_mouse_entered"):
			node.disconnect("mouse_entered", self, "_on_mouse_entered")
		if node.is_connected("mouse_exited", self, "_on_mouse_exited"):
			node.disconnect("mouse_exited", self, "_on_mouse_exited")
		if node.is_connected("pressed", self, "_on_item_select"):
			node.disconnect("pressed", self, "_on_item_select")

		node.connect("focus_entered", self, "_on_focus_entered", [node])
		node.connect("focus_exited", self, "_on_focus_exited", [node])
		node.connect("mouse_entered", self, "_on_mouse_entered", [node])
		node.connect("mouse_exited", self, "_on_mouse_exited", [node])
		node.connect("pressed", self, "_on_item_select", [i])

		node.material.set_shader_param("enable_shader", false)

		i += 1

	# Clear all remaining item slots.
	while i < player.MAX_ITEMS:
		var node = get_node("Item%d" % (i + 1))
		node.texture_normal = null

		if node.is_connected("focus_entered", self, "_on_focus_entered"):
			node.disconnect("focus_entered", self, "_on_focus_entered")
		if node.is_connected("focus_exited", self, "_on_focus_exited"):
			node.disconnect("focus_exited", self, "_on_focus_exited")
		if node.is_connected("mouse_entered", self, "_on_mouse_entered"):
			node.disconnect("mouse_entered", self, "_on_mouse_entered")
		if node.is_connected("mouse_exited", self, "_on_mouse_exited"):
			node.disconnect("mouse_exited", self, "_on_mouse_exited")
		if node.is_connected("pressed", self, "_on_item_select"):
			node.disconnect("pressed", self, "_on_item_select")

		node.material.set_shader_param("enable_shader", false)

		i += 1

	show()
	$Item1.grab_focus()

func _on_item_select(idx) -> void:
	# Reset the state.
	hide()

	# Continue execution.
	emit_signal("item_selected", idx)

func _on_focus_entered(button) -> void:
	button.material.set_shader_param("enable_shader", true)

func _on_focus_exited(button) -> void:
	button.material.set_shader_param("enable_shader", false)

func _on_mouse_entered(button) -> void:
	button.material.set_shader_param("enable_shader", true)

func _on_mouse_exited(button) -> void:
	if not button.has_focus():
		button.material.set_shader_param("enable_shader", false)
