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
}```

### MQTT Subscriber

A Python MQTT subscriber has been implemented to receive messages from the MQTT broker and store them in a MongoDB collection for further processing and analysis.
Data Storage

We have initiated a MongoDB instance using Docker to save incoming MQTT messages, providing a robust and scalable data storage solution.
### In-Memory Data Management

Redis has been implemented using Docker to store the latest ten sensor readings in memory, allowing for fast retrieval and real-time analysis of recent data.
### FastAPI Endpoint

We have designed a FastAPI-based API with the following endpoints:

    Retrieve Sensor Readings by Range: This endpoint allows users to fetch sensor readings by specifying a start and end range.

    Retrieve Last Ten Sensor Readings: This endpoint retrieves the last ten sensor readings for a specific sensor.

### Docker Integration

All services and components of this system have been integrated using Docker Compose, making it easy to set up and manage the entire system.
Deliverables
Repository

The entire codebase for this project is hosted on GitHub.
### Docker Compose

The docker-compose.yml file included in this repository ensures easy system setup. It encompasses services for the Python apps (MQTT publisher, subscriber, FastAPI application), Mosquitto MQTT broker, MongoDB, and Redis.
Setup and Usage

To set up and interact with the system, follow these steps:

    Clone this repository:

    bash

git clone https://github.com/vivekpathre/sensor-data-monitoring-system.git

Navigate to the project directory:

bash

cd sensor-data-monitoring-system

Start the system using Docker Compose:

bash

    docker-compose up -d

    Access the FastAPI application and its endpoints by opening your web browser and navigating to http://localhost:8000/docs. You can use the interactive Swagger documentation to explore and interact with the API.

### Design Choices and Rationale

    We chose Docker for containerization to ensure consistency and ease of deployment across different environments.
    Mosquitto MQTT was selected as the broker due to its lightweight and efficient nature.
    MongoDB provides a flexible and scalable solution for storing sensor data.
    Redis is used for in-memory storage to enable fast access to recent sensor readings.
    FastAPI was chosen for its high performance and automatic generation of interactive API documentation using Swagger.

### Challenges and Solutions

During the development of this project, we encountered some challenges, including:

    Integration Complexity: Integrating multiple services using Docker Compose required careful configuration and coordination. We addressed this by thoroughly testing the setup and ensuring proper service intercommunication.

    Data Consistency: Ensuring consistency between in-memory data stored in Redis and data stored in MongoDB was challenging. We implemented data synchronization mechanisms to address this issue.

    Security: Securing MQTT communication and API endpoints was a priority. We implemented authentication and encryption to protect data in transit.

Please refer to the project documentation for more details on the challenges faced and their respective solutions.

For any questions or issues, please contact your@email.com.
"""
