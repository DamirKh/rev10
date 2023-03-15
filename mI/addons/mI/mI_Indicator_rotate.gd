extends Sprite
export var Tag = ""
export var ON_color =  Color(0.0, 1.0, 0.0, 1.0)
export var OFF_color =  Color(1.0, 0.0, 0.0, 1.0)
export var Undefined_color = Color(1.0, 1.0, 1.0, 0.5)
export var Rotation_Speed = 180
export var Color_change_time = 1.2
var Rotate = false
var white = Color(1.0, 1.0, 1.0, 1.0)
#var T = Timer.new()
var DestColor: Color
var FromColor: Color
var T01 = Timer01.new()
var From_rotation_speed = 0
var Dest_rotation_speed = 0



onready var NW = get_node("/root/MiNetwork")

# Called when the node enters the scene tree for the first time.
func _ready():
	NW.connect("Radio", self,  "Radio")
	
	self.self_modulate = Undefined_color
	FromColor = self.self_modulate
	
	T01.wait_time = Color_change_time
	T01.one_shot = true
	add_child(T01)
	T01.connect("timeout", self, "_on_T_timeout")
	pass # Replace with function body.


func _process(delta):
	self.rotation_degrees = fmod((self.rotation_degrees + delta * lerp(From_rotation_speed, Dest_rotation_speed, T01.part)), 360)
	
	self.self_modulate = lerp(FromColor, DestColor, T01.part)
	

func _enter_tree():
	if not Tag:
		var P = self.get_parent()
		while P:
			if "Tag" in P:
				Tag = P.Tag
				break
			else:
				P = P.get_parent()
	pass
	#self.hint_tooltip = Tag


func Radio(TagName, Value):
	if TagName == Tag:
		match Value:
			"ON", 1:
				#self.
				self.DestColor = ON_color
				
				Dest_rotation_speed = Rotation_Speed
				From_rotation_speed = 0
				
				T01.start()

			"OFF", 0:
				self.DestColor = OFF_color
				
				From_rotation_speed = Rotation_Speed
				Dest_rotation_speed = 0
				
				T01.start()

			_:
				#self.color = Undefined_color
				pass
				
func _on_T_timeout():

	self.FromColor = self.self_modulate

	
