# Sensor Data Monitoring System

## Challenge Overview

### Purpose

The purpose of this project is to create a system that can simulate sensor behavior, collect sensor readings, and provide APIs for retrieving and managing sensor data.

### MQTT Broker Setup

We have deployed a Mosquitto MQTT broker using Docker to facilitate communication between sensors and the data storage components.

### MQTT Publisher

A Python MQTT client has been created to mimic multiple sensor readings and publish them to MQTT topics such as `sensors/temperature` and `sensors/humidity`. The structure of the JSON payload for sensor readings is as follows:

```json
{
    "sensor_id": "unique_sensor_id",
    "value": "<reading_value>",
    "timestamp": "ISO8601_formatted_date_time"
}
