import json
import paho.mqtt.client as mqtt
import time
import redis
from pprint import pprint

# Connect to the Redis instance
r = redis.Redis(host="127.0.0.1", port=6379, db=0)
n = 0


def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("connected")
        client.subscribe("Sensor_Reading")
    else:
        print("could not connect, return code:", return_code)


def on_message(client, userdata, message):
    global n
    msg = json.loads((message.payload.decode("utf-8")))
    print(type(msg))
    # n = 1
    # Insert the document into the redis
    r.set("reading_{0}".format(str(n)), json.dumps(msg))
    n = n + 1
    if n == 11:
        n = 0
    else:
        pass
    print("Received message: ", msg)


broker_hostname = "localhost"
port = 1883

client = mqtt.Client("Client3")
# client.username_pw_set(username="user_name", password="password") # uncomment if you use password auth
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_hostname, port)
client.loop_start()

try:
    time.sleep(100)
finally:
    client.loop_stop()
