extends Control

export var Tag = ""
#export var Command = "*"
export var UnderMouse = true
export var HintModulate = true

onready var NW = get_node("/root/MiNetwork")
onready var PopupNode = get_node("Popup")
onready var Parent = get_parent()

var ConfiguredPopupPos : Vector2

#onready var place = Rect2(Parent., Parent.margin_top, PopupNode.rect_size.x, rect_size.y)

func _enter_tree():
	if not Tag:
		var P = self.get_parent()
		while P:
			if "Tag" in P:
				Tag = P.Tag
				break
			else:
				P = P.get_parent()
				
func _gui_input(event):
	if not PopupNode:
		return
	if event is InputEventMouseButton and event.button_index == BUTTON_LEFT and event.pressed:
		if UnderMouse:
			PopupNode.set_global_position(self.get_global_mouse_position() + ConfiguredPopupPos)
			PopupNode.popup_centered()
		else:
			PopupNode.popup_centered()
		pass

func _notification(what):
	match what:
		NOTIFICATION_MOUSE_ENTER:
			pass # Mouse entered the area of this control.
		NOTIFICATION_MOUSE_EXIT:
			pass # Mouse exited the area of this control.

# Called when the node enters the scene tree for the first time.
func _ready():
	if not PopupNode:
		print_debug(self.name, " was not properly configured!")
		print_debug("No Popup child node!")
	else:
		ConfiguredPopupPos = PopupNode.rect_position
		mouse_default_cursor_shape = Control.CURSOR_POINTING_HAND
	pass # Replace with function body.



func _on_TouchScreenButton_released():
	PopupNode.popup_centered()
	pass # Replace with function body.
