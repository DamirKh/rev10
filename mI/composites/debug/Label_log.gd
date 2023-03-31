extends Label

export var Update_Time = 1

var T := Timer.new()

# Called when the node enters the scene tree for the first time.
func _ready():
	GlobalLogger.messages.append('-------------------------------------')
	_fill()
	T.wait_time = Update_Time
	T.one_shot = false
	add_child(T)
	T.connect("timeout", self, "_fill")
	T.start()
	get_parent().scroll_vertical = 50000

func _fill():
	var new_log_messages = ""
	for msg in GlobalLogger.messages:
		new_log_messages += '\n'
		new_log_messages += msg
	self.text = new_log_messages
