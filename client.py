import socket
import sys
import re

def is_valid_mac(mac_address):
    # Regular expression to validate MAC address format
    mac_pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    return bool(mac_pattern.match(mac_address))

if len(sys.argv) != 2 or not is_valid_mac(sys.argv[1]):
    print("Usage: python script_name.py <server_mac_address>")
    print("Please check the MAC address format.")
    sys.exit(1)

server_mac_address = sys.argv[1]

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    client.connect((server_mac_address, 4))
    print(f"Connected to server at {server_mac_address}")

    while True:
        message = input("Client: ")
        client.send(message.encode("utf-8"))

        if message.lower() == "bye":
            print("Closing the connection. Goodbye!")
            break

        data = client.recv(1024)
        if not data:
            print("Server closed the connection. Goodbye!")
            break

        server_message = data.decode('utf-8')
        print(f"Server: {server_message}")

        if server_message.lower() == "bye":
            print("Server requested to close the connection. Closing...")
            break

except OSError as e:
    print(f"Error: {e}")

finally:
    client.close()
