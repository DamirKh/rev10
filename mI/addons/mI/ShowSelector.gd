extends Node2D
export var Tag = ""

onready var Variants = get_children()

# Point is a Tag resolver and radio receiver
var Point = load("res://addons/mI/point.gd")
var point = Point.new()


func _ready():
	add_child(point)
	for node in Variants:
		node.visible = false
	Directive('DIS')
	pass # Replace with function body.


func Radio(Value):
	var variant = str(Value).to_upper()
	print_debug('Selector got '+ Value)
	for node in Variants:
		node.visible = node.name.to_upper() == Value


func Directive(Value):
	if Value == 'DIS':
		Radio('DIS')
