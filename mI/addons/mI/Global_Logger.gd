extends Node
export var messages = []
export var History_Lenght = 100
export var Tag = "LOG"

# Point is a Tag resolver and radio receiver
var Point = load("res://addons/mI/point.gd")
var point = Point.new()

# Called when the node enters the scene tree for the first time.
func _ready():
	add_child(point)
	messages.append("Log started")

func Radio(Value):
	#print_debug('Label got Radio')
	messages.append(Value)
	while len(messages) > History_Lenght:
		messages.pop_front()
