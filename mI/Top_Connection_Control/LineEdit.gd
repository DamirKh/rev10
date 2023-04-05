extends LineEdit


# Called when the node enters the scene tree for the first time.
func _ready():
	text = MiNetwork.websocket_url
	pass # Replace with function body.



func _on_LineEdit_text_entered(new_text):
	MiNetwork.websocket_url = new_text
	
	pass # Replace with function body.


func _on_Button_pressed():
	_on_LineEdit_text_entered(text)
	var config = ConfigFile.new()
	config.set_value("ESP", "URL", text)
	config.save("user://config.ini")
	
	Global.goto_scene("res://main.tscn")
	#Global.go_back()
