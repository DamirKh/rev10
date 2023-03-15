extends Button

export var Tag = "Tag"
export var Command = "*"
export var Release_focus = 1.2
onready var NW = get_node("/root/MiNetwork")
var T := Timer.new()


# Called when the node enters the scene tree for the first time.
func _ready():
	self.add_to_group('control', true)
	self.rect_min_size = self.rect_size
	connect("pressed", self, "clicked")
	self.hint_tooltip = Tag
	if not self.text and not self.icon:
		self.text = Command

	T.wait_time = Release_focus
	T.one_shot = true
	add_child(T)
	T.connect("timeout", self, "_on_T_timeout")




func _enter_tree():

	if not Tag:
		var P = self.get_parent()
		while P:
			if "Tag" in P:
				Tag = P.Tag
				break
			else:
				P = P.get_parent()


func clicked():
	NW.PhoneCall(Tag, Command)
	T.start()


func _on_T_timeout():
	self.release_focus()
