import socket
import json

# Define constants
TCP_IP = '192.168.194.95'  # IP address of the A50 sensor
TCP_PORT = 16171  # Port number the A50 sensor is listening on
BUFFER_SIZE = 1024  # Size of the receive buffer

class A50Node:
    def __init__(self):
        self.sock = None  # Initialize socket to None
        self.serv_addr = ("localhost", 56789)  # Server address (IP and port)
        self.buffer = bytearray(BUFFER_SIZE)  # Create a buffer to store received data
        self.resetDeadReckoning()

    def resetDeadReckoning(self):
        try:
            # Create a socket, connect to the server, send reset command, and close the socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(self.serv_addr)
            json_command = {"command": "reset_dead_reckoning"}
            sock.send(json.dumps(json_command).encode())
            sock.close()
        except Exception as e:
            print("Failed to reset dead reckoning:", e)

    def connectToSocket(self):
        try:
            # Create a socket and connect to the server
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(self.serv_addr)
            return sock  # Return the connected socket
        except Exception as e:
            print("Failed to connect to socket:", e)
            return None  # Return None if connection fails

    def parseJson(self, json_dict):
        try:    
            x = json_dict["x"]
            y = json_dict["y"]
            z = json_dict["z"]
            yaw = json_dict["yaw"]
            pitch = json_dict["pitch"]
            roll = json_dict["roll"]

            return [yaw, pitch, roll, x, y, z]
        except Exception as e:
            print("Failed to parse JSON:", e)
            return []  # Return an empty list if parsing fails

    def printData(self, a50_data):
        print("Publishing State Data:")
        print("Yaw:", a50_data[0], "Pitch:", a50_data[1], "Roll:", a50_data[2])
        print("X:", a50_data[3], "Y:", a50_data[4], "Z:", a50_data[5])

    def recieveData(self):
        try:
            # Receive data from the socket, parse JSON, and publish data
            bytesRead = self.sock.recv(BUFFER_SIZE)
            json_stream = bytesRead.decode()
            json_dict = json.loads(json_stream)
            a50_data = self.parseJson(json_dict)
            self.printData(a50_data)
            return a50_data
        except Exception as e:
            print("Error in getting A50 data:", e)
            self.sock.close()
            self.sock = self.connectToSocket()  # Reconnect if an error occurs
            return None

    def run(self):
        # Connect to the socket and continuously receive data
        self.sock = self.connectToSocket()
        if self.sock:
            while True:
                self.recieveData()  # Receive and process A50 sensor data

# Run the node
if __name__ == "__main__":
    a50_node = A50Node()
    a50_node.run()
