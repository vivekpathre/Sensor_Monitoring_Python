from fastapi import FastAPI, HTTPException
import paho.mqtt.client as mqtt
import json
import asyncio

app = FastAPI()

sensor_data = []  # Store received sensor data

@app.get("/get_data/")
async def sens(start_id: int, end_id: int):
    if start_id > end_id:
        raise HTTPException(status_code=400, detail="Invalid sensor ID range")
    elif start_id < 101 and end_id > 251:
        raise HTTPException(status_code=400, detail="Invalid sensor ID range")

    def on_connect(client, userdata, flags, return_code):
        if return_code == 0:
            print("connected")
            client.subscribe("Sensor_Reading")
        else:
            print("could not connect, return code:", return_code)

    def on_message(client, userdata, message):
        msg = json.loads(message.payload.decode("utf-8"))
        print(type(msg))
        # If the sensor id is in range then store the data.
        if start_id <= msg['sensor_id'] <= end_id:
            sensor_data.append(msg)

    broker_hostname = "localhost"
    port = 1883

    client = mqtt.Client("Client4")
    # client.username_pw_set(username="user_name", password="password") # uncomment if you use password auth
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker_hostname, port)
    client.loop_start()

    try:
        await asyncio.sleep(10)  # Let the event loop run for 10 seconds
        return sensor_data  # Return the collected sensor data
    finally:
        client.loop_stop()
