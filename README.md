# A50 Sensor Data Acquisition and Publication

## Overview
This Python script enables the acquisition, parsing, and publication of A50 sensor data from the robot. The A50 sensor data is retrieved from a web server using TCP/IP communication (sockets). The script connects to the specified IP address and port, receives the data stream in JSON format, parses it, and publishes the extracted sensor data.

## Setup
Before running the script, ensure that Python is installed on your system. Additionally, make sure you have the necessary permissions to access the A50 sensor's web server.

## Usage:
1. Modify the `TCP_IP` and `TCP_PORT` constants in the script to match the IP address and port number of your A50 sensor.
2. Run the script using the following command:
   ```
   python3 get_a50_data.py
   ```
3. Once the script is running, it will continuously receive and process A50 sensor data.

## Features:
- Automatically reconnects to the socket in case of connection errors.
- Parses JSON data for specific sensor values such as yaw, pitch, roll, x, y, and z coordinates.
- Publishes the extracted sensor data in the terminal for further processing or visualization.

## Dependencies:
- Python 3.x
- The script uses the built-in `socket` and `json` modules, which are included in Python's standard library.

## Note:
- Ensure that the A50 sensor is properly configured and running, and the specified IP address and port are accessible from your network.
- Handle any errors or exceptions encountered during script execution appropriately to maintain continuous data acquisition.

**Author:**
@Zix on discord

**Contributor:**
-  Halie (@duh on discord)
