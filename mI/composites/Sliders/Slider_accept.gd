extends Node2D
export var Tag = ""

# Point is a Tag resolver and radio receiver
var Point = load("res://addons/mI/point.gd")
var point = Point.new()


func _ready():
	add_child(point)
	$HSlider.connect("drag_ended", self, "value_changed" )

func value_changed(changed):
	if changed:
		print_debug('New value:'.format($HSlider.value))
	pass
	
