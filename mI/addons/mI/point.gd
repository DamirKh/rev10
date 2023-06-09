extends Node

onready var NW = get_node("/root/MiNetwork")
onready var P = self.get_parent()

const Radio = 'Radio'
const Directive = 'Directive'

var Tag = ''


#func _enter_tree():
#	pass

func _ready():
	NW.connect(Radio, self,  Radio)
	NW.connect(Directive, self,  Directive)
	pass

	var ancestor = P # self.get_parent()
	
	while ancestor:
		if ancestor.get('Tag'):  #DONE
			Tag = ancestor.Tag
			P.Tag = Tag
			break
		else:
			#  go up on tree
			ancestor = ancestor.get_parent()
	if not Tag:
		printerr("Tag was not found for node {}".format([ self.get_parent(), ], '{}'))


func PhoneCall(phone_message):
	NW.PhoneCall(Tag, phone_message)
	

func Radio(TagName, Value):
	if TagName == Tag and P.has_method(Radio):
		P.Radio(Value)
		
func Directive(TagName, Value):
	if (TagName == Tag or TagName == '*') and P.has_method(Directive):
		P.Directive(Value)
