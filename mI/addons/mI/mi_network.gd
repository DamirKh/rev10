extends Node
signal Radio(Tag, Value)
signal Directive(Tag, Value)

var config = ConfigFile.new()

# The default URL we will connect to
# This is an IP adress when ESP32 in AccessPoint mode
export var websocket_url = "ws://192.168.4.1:7777"

var _client = WebSocketClient.new()

var WaitForPingRespondTimer := Timer.new()
var PingPeriodTimer := Timer.new()

var Connected_to_ESP = false
var ControlsDisabled = false

func _ready():
	disable_all_controls()
	Connected_to_ESP = false
	
	# Load config file
	var err = config.load("user://config.ini")
	# If the file didn't load, ignore it.
	if err == OK:
		websocket_url = config.get_value('ESP', "URL")
		print_debug('Loaded ESP URL ', websocket_url)
	
	# Connect base signals to get notified of connection open, close, and errors.
	_client.connect("connection_closed", self, "_closed")
	_client.connect("connection_error", self, "_closed")
	# the "connection established" signal gives false information for no clear reason
	#_client.connect("connection_established", self, "_connected")

	# Initiate WaitForPingRespondTimer
	WaitForPingRespondTimer.wait_time = 1.0
	WaitForPingRespondTimer.one_shot = true
	WaitForPingRespondTimer.connect("timeout", self, "_No_Ping_Respond")
	add_child(WaitForPingRespondTimer)

	# Initiate PingPeriodTimer
	PingPeriodTimer.wait_time = 3.0
	PingPeriodTimer.one_shot = false
	PingPeriodTimer.connect("timeout", self, "_on_PingPeriodTimer")
	add_child(PingPeriodTimer)
	PingPeriodTimer.start()
	Reconnect()
	
func _on_PingPeriodTimer():
	print_debug('Time to ping ESP')
	var data_to_esp = '.'  # + ' '+'.'
	_client.get_peer(1).put_packet(data_to_esp.to_ascii())
	WaitForPingRespondTimer.start()

func _No_Ping_Respond():
	print_debug('No PING respond')
	Connected_to_ESP = false
	yield(get_tree().create_timer(1.0), "timeout")
	Log("Lost connection to ESP32")
	Reconnect()

func _closed(was_clean = false):
	# was_clean will tell you if the disconnection was correctly notified
	# by the remote peer before closing the socket.
	print("Closed, clean: ", was_clean)
	Connected_to_ESP = false
	Log("Connection to ESP32 closed")
	disable_all_controls()

func Reconnect():
	Log("Try to (re)connect to ESP32")
	_client.disconnect_from_host(1000, "connection_error")
	print_debug("Trying to connect to "+websocket_url)
	var err = _client.connect_to_url(websocket_url)
	print_debug("Connection status: "+String(err))
	if err != OK:
		print_debug("Unable to connect")
	else:
		print_debug("Connected to "+_client.get_connected_host())
		_client.get_peer(1).set_write_mode(WebSocketPeer.WRITE_MODE_TEXT)

func disable_all_controls():
	# comment next line for Local debug
	if not ControlsDisabled:
		emit_signal("Directive", '*', 'DIS')
		ControlsDisabled = true
	pass

func enable_all_controls():
	if not Connected_to_ESP:
		return
	emit_signal("Directive", '*', 'EN')
	ControlsDisabled = false

func _process(_delta):
	# Call this in _process or _physics_process. Data transfer, and signals
	# emission will only happen when calling this function.
	var state = _client.get_connection_status()
	if state == WebSocketClient.CONNECTION_DISCONNECTED:
		disable_all_controls()
		return
	_client.poll()
	if state == WebSocketClient.CONNECTION_CONNECTED:
		while _client.get_peer(1).get_available_packet_count():
			var in_message = _client.get_peer(1).get_packet().get_string_from_ascii()
			if in_message == '.':
				WaitForPingRespondTimer.stop()
				if not Connected_to_ESP:
					Log("Connection to ESP32 established")
					Connected_to_ESP = true
				continue
			var from_array = in_message.split(" ", true, 1)
			if from_array.size() == 2:
				print_debug("From: ", from_array[0])
				print_debug("Value: ", from_array[1])
				emit_signal("Radio", from_array[0], from_array[1])
			else:
				print_debug("Message: ", in_message)

func _connected(proto = ""):
	# This is called on connection, "proto" will be the selected WebSocket
	# sub-protocol (which is optional)
	print_debug("Connected with protocol: ", proto)
	_client.get_peer(1).set_write_mode(WebSocketPeer.WRITE_MODE_TEXT)
	enable_all_controls()

func PhoneCall(from, message, advanced=""):
	print_debug("HMI Message to ESP32: ", from, " ", message)
	# Uncomment next line for local debug. 
	#emit_signal("Radio", from, message)
	var data_to_esp = from + ' ' + message
	_client.get_peer(1).put_packet(data_to_esp.to_ascii())
	
func Log(text):
	emit_signal("Radio", "LOG", text)
	

