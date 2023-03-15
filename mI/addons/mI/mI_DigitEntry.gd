extends Control

export var Tag = ""
export var MinValue = -10
export var MaxValue = 100
export var AcceptDot = true
onready var NW = get_node("/root/MiNetwork")

var b = "0"
var b_backup :String

func _enter_tree():
	if not Tag:
		var P = self.get_parent()
		while P:
			if "Tag" in P:
				Tag = P.Tag
				break
			else:
				P = P.get_parent()

# Called when the node enters the scene tree for the first time.
func _ready():
	NW.connect("Radio", self,  "Radio")
	$mI_ControlPopup/Popup.window_title = Tag
	if not AcceptDot:
		$mI_ControlPopup/Popup/VBoxContainer/GridContainer/ButtonDot.disabled=true
	pass # Replace with function body.


func _on_Button_pressed(extra_arg_0):
	match extra_arg_0:
		1,2,3,4,5,6,7,8,9,0:
			b = b + str(extra_arg_0)
			b = str(float(b))
		-1:
			b = str(-1*float(b))
		-2:
			b=b.left(b.length()-1)
			if not b:
				b="0"
		-3:
			b=b+"."
		-5:
			b = b_backup
			$mI_ControlPopup/Popup.hide()
		-6:
			NW.PhoneCall(Tag, b)
			b_backup = b
			$mI_ControlPopup/Popup.hide()
	if "." in b:
		$mI_ControlPopup/Popup/VBoxContainer/GridContainer/ButtonDot.disabled=true
	else:
		$mI_ControlPopup/Popup/VBoxContainer/GridContainer/ButtonDot.disabled=not AcceptDot
	if float(b) < MinValue or float(b) > MaxValue:
		$mI_ControlPopup/Popup/VBoxContainer/GridContainer/ButtonOK.disabled=true
	else:
		$mI_ControlPopup/Popup/VBoxContainer/GridContainer/ButtonOK.disabled=false
	$mI_ControlPopup/Popup/VBoxContainer/LabelValue.text = b
	pass # Replace with function body.


func Radio(TagName, Value):
	if TagName == Tag:
		b = Value
		b_backup = b


func clicked():
	NW.PhoneCall(Tag, b)


func _on_Popup_about_to_show():
	b_backup = b
	pass # Replace with function body.
