extends ProgressBar
export var Tag = ""

#export var ON_color =  Color(0.0, 1.0, 0.0, 1.0)
#export var OFF_color =  Color(1.0, 0.0, 0.0, 1.0)
#export var Undefined_color = Color(1.0, 1.0, 1.0, 0.5)
#var white = Color(1.0, 1.0, 1.0, 1.0)
#export var Color_ON =  Color(1.0, 1.0, 1.0, 0.3)
#export var Color_OFF =  Color(1.0, 1.0, 1.0, 0.3)


onready var NW = get_node("/root/MiNetwork")

# Called when the node enters the scene tree for the first time.
func _ready():
	NW.connect("Radio", self,  "Radio")
	#self.antialiased = true
#	self.color = Undefined_color
	pass # Replace with function body.

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
		self.value = float(Value)
