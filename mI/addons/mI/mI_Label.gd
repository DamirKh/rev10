extends Label
export var Tag = ""

# Point is a Tag resolver and radio receiver
var Point = load("res://addons/mI/point.gd")
var point = Point.new()

onready var TextFormat = self.text

# Called when the node enters the scene tree for the first time.
func _ready():
	add_child(point)

	self.text = TextFormat%"***"
	pass # Replace with function body.

func _enter_tree():
	self.hint_tooltip = Tag


func Radio(Value):
	#print_debug('Label got Radio')
	self.text = TextFormat%str(Value)
