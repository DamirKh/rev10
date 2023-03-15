extends CheckBox

export var Tag = "Tag"
onready var NW = get_node("/root/MiNetwork")


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func _enter_tree():
	connect("pressed", self, "clicked")
	self.hint_tooltip = Tag


func clicked():
	if self.pressed:
		NW.PhoneCall(Tag, "ON")
		#print("Checked!")
	else:
		NW.PhoneCall(Tag, "OFF")
