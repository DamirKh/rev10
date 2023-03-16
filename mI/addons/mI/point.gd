extends Node

onready var NW = get_node("/root/MiNetwork")
onready var P = self.get_parent()

var Tag = ''

#func _enter_tree():
#	pass

func _ready():
	NW.connect("Radio", self,  "Radio")
	pass

	var ancestor = P # self.get_parent()
	
	if not ancestor.Tag:
		while ancestor:
			if "Tag" in ancestor:
				Tag = ancestor.Tag
				P.Tag = Tag
				break
			else:
				#  go up on tree
				ancestor = ancestor.get_parent()
	else:
		Tag = P.Tag


func PhoneCall(phone_message):
	NW.PhoneCall(Tag, phone_message)
	

func Radio(TagName, Value):
	if TagName == Tag:
		P.Radio(Value)

