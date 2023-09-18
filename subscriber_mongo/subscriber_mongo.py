import json
import pymongo
import paho.mqtt.client as mqtt
import time


# Connect to the MongoDB instance
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

# Select the database and collection you want to use
db = client["admin"]
collection = db["sensor_data"]


def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("connected")
        client.subscribe("Sensor_Reading")
    else:
        print("could not connect, return code:", return_code)


def on_message(client, userdata, message):
    msg = json.loads((message.payload.decode("utf-8")))
    print(type(msg))
    # Insert the document into the collection
    result = collection.insert_one(msg)

    # Print the ID of the inserted document
    print(result.inserted_id)
    print("Received message: ", msg)


broker_hostname = "localhost"
port = 1883

client = mqtt.Client("Client2")
# client.username_pw_set(username="user_name", password="password") # uncomment if you use password auth
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_hostname, port)
client.loop_start()

try:
    time.sleep(100000)
finally:
    client.loop_stop()
