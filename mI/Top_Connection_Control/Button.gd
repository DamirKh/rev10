extends Button
onready var NW = get_node("/root/MiNetwork")



# Called when the node enters the scene tree for the first time.
func _ready():
	text = NW.websocket_url
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
