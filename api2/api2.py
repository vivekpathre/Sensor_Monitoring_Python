import asyncio

from fastapi import FastAPI, HTTPException
import paho.mqtt.client as mqtt
import time
import json

app = FastAPI()
values = []


# http://localhost:8000/get_sensor_data/?start_sensor_id=1&end_sensor_id=3

@app.get("/get_10_readings/")
async def sens(start_id: int):
    if start_id not in range(101, 251):
        raise HTTPException(status_code=400, detail="Invalid sensor ID.")

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
        if msg['sensor_id'] == start_id:
            values.append(msg)


    broker_hostname = "localhost"
    port = 1883

    client = mqtt.Client("Client5")
    # client.username_pw_set(username="user_name", password="password") # uncomment if you use password auth
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker_hostname, port)
    client.loop_start()

    try:
        await asyncio.sleep(20)  # Let the event loop run for 10 seconds
        return values
    finally:
        client.loop_stop()
