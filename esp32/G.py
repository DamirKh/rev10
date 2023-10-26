from typing import Dict, Any

print("Globals loading...")
from primitives.queue import Queue
from forcer.Forcer import Forcer

MAIN_IF = ""
CLIENTS = {}
IN_QUEUE = Queue(maxsize=10)
OUT_QUEUE = Queue(maxsize=100)
DEVICES: dict[Any, Any] = {}

INPUT_TAG = {}
OUTPUT_TAG = {}

FORCER = Forcer(enable=True)
