extends Control

export var Tag = ""
#export var Command = "*"
export var UnderMouse = true
export var HintModulate = true

onready var PopupNode = get_node("Popup")

var ConfiguredPopupPos : Vector2

# Point is a Tag resolver and radio receiver
var Point = load("res://addons/mI/point.gd")
var point = Point.new()


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
	add_child(point)
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
