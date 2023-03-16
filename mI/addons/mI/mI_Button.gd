extends Button

export var Tag = "Tag"
export var Command = "*"
export var Release_focus = 1.0


var T := Timer.new()

# Point is a Tag resolver and radio receiver
var Point = load("res://addons/mI/point.gd")
var point = Point.new()


# Called when the node enters the scene tree for the first time.
func _ready():
	add_child(point)
	self.rect_min_size = self.rect_size
	connect("pressed", self, "clicked")
	self.hint_tooltip = Tag
	if not self.text and not self.icon:
		self.text = Command

	T.wait_time = Release_focus
	T.one_shot = true
	add_child(T)
	T.connect("timeout", self, "_on_T_timeout")


func clicked():
	point.PhoneCall(Command)
	T.start()

func Radio(Value):
	pass


func _on_T_timeout():
	self.release_focus()
