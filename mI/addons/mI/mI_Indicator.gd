extends Polygon2D
export var Tag = ""
export var ON_color =  Color(0.0, 1.0, 0.0, 1.0)
export var OFF_color =  Color(1.0, 0.0, 0.0, 1.0)
export var Undefined_color = Color(1.0, 1.0, 1.0, 0.5)
var white = Color(1.0, 1.0, 1.0, 1.0)

# Point is a Tag resolver and radio receiver
var Point = load("res://addons/mI/point.gd")
var point = Point.new()


# Called when the node enters the scene tree for the first time.
func _ready():
	add_child(point)
#	NW.connect("Radio", self,  "Radio")
	self.antialiased = true
	self.color = Undefined_color
	pass # Replace with function body.


func Radio(Value):
	match Value:
		"ON", 1:
			self.color = ON_color
		"OFF", 0:
			self.color = OFF_color
		_:
			self.color = Undefined_color

