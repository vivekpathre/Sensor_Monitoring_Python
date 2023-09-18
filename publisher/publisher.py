import paho.mqtt.client as mqtt
import time
import json
import random
from datetime import datetime

# MQTT broker configuration
broker_hostname = "localhost"  # Replace with the actual broker hostname or IP
port = 1883

# Callback function when the client connects to the MQTT broker
def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("Connected to MQTT broker")
    else:
        print("Could not connect to MQTT broker, return code:", return_code)

# Create an MQTT client
client = mqtt.Client("Client1")
# Uncomment and set username and password if you use authentication
# client.username_pw_set(username="user_name", password="password")
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(broker_hostname, port)
client.loop_start()

# MQTT topic to publish sensor readings
topic = 'Sensor_Reading'

# Function to generate random sensor values
def values():
    sensor_id = random.randint(101, 251)
    temperature = random.uniform(-5.0, 55)
    timestamp = datetime.now().isoformat()
    topic1 = {"sensor_id": sensor_id, "value": temperature, "timestamp": timestamp}
    return topic1

msg_count = 0

try:
    while msg_count < 10000:
        time.sleep(2)
        msg_count += 1
        output = values()
        result = client.publish(topic, payload=json.dumps(output))
        print(output)
        status = result[0]
        if status == 0:
            print("Message " + str(msg_count) + " is published to topic " + str(topic))
        else:
            print("Failed to send message to topic " + str(topic))
finally:
    # Stop the MQTT client loop when finished
    client.loop_stop()

