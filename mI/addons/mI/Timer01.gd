class_name Timer01
extends Timer
var part setget ,part

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func part():
	var T_Ratio = (self.wait_time - self.time_left) / self.wait_time
	return(T_Ratio)
