extends ProgressBar
export var Tag = ""

export var HiHiSetpoint = 35.0
export var HiSetpoint = 30.0
export var LoSetpoint = 18.0
export var LoLoSetpoint = 5.0

export var HiHi_color = Color(1.0, 0.0, 0.0, 1.0)
export var Hi_color = Color(1.0, 1.0, 0.0, 1.0)
export var normal_color =  Color(0.0, 1.0, 0.0, 1.0)
export var Lo_color =  Color(1.0, 1.0, 0.0, 1.0)
export var LoLo_color =  Color(1.0, 0.0, 0.0, 1.0)


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
		if LoSetpoint < self.value and self.value < HiSetpoint:
			self_modulate = normal_color
		if HiSetpoint < self.value and self.value < HiHiSetpoint:
			self_modulate = Hi_color
		if HiHiSetpoint < self.value:
			self_modulate = HiHi_color
		if LoLoSetpoint < self.value and self.value < LoSetpoint:
			self_modulate = Lo_color
		if self.value < LoLoSetpoint:
			self_modulate = LoLo_color

