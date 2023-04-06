extends Node2D
export var Tag = ""
export var TextOnLabel = "Setpoint"
export var MinValue = 0
export var MaxValue = 100


# Point is a Tag resolver and radio receiver
var Point = load("res://addons/mI/point.gd")
var point = Point.new()

var T := Timer.new()

func _ready():
	add_child(point)
	$HSlider.min_value = MinValue
	$HSlider.max_value = MaxValue
	$Panel.set_visible(false)
	$HSlider.connect("drag_ended", self, "value_changed" )
	$HSlider.connect("drag_started", self, "drag_started" )
	$Button.connect("pressed", self, "_on_Button_Pressed")
	$Label.text = TextOnLabel
	
	T.wait_time = 5.0
	T.one_shot = true
	add_child(T)
	T.connect("timeout", self, "_on_T_timeout")
	
func _process(delta):
	$Panel/Label.text=str($HSlider.value)

func value_changed(changed):
	if changed:
		print_debug('Slider changed: {0}'.format([$HSlider.value,]))
		T.set_paused(false)
		T.start()
		#yield(get_tree().create_timer(1.0), "timeout")
		#$Panel.set_visible(false)
	pass
	
func drag_started():
	$Panel.set_visible(true)
	T.set_paused(true)

func _on_T_timeout():
	$Panel.set_visible(false)

func _on_Button_Pressed():
	point.PhoneCall(str($HSlider.value))
	T.start()

func Directive(Value):
	if Value == 'DIS':
		$Button.disabled = true
	if Value == 'EN':
		$Button.disabled = false
