extends Label
export var Tag = "Tag"

onready var NW = get_node("/root/MiNetwork")
onready var TextFormat = self.text

# Called when the node enters the scene tree for the first time.
func _ready():
	NW.connect("Radio", self,  "Radio")
	
	self.text = TextFormat%"***"
	self.hint_tooltip = Tag
	pass # Replace with function body.

func _enter_tree():
	self.hint_tooltip = Tag


func Radio(TagName, Value):
	if TagName == Tag:
		self.text = TextFormat%str(Value)
