import socket
import threading
import sys
import re

def is_valid_mac(mac_address):
    # Regular expression to validate MAC address format
    mac_pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    return bool(mac_pattern.match(mac_address))

def receive_messages(client):
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break

            server_message = data.decode('utf-8')
            print(f"\rServer: {server_message}")

            if server_message.lower() == "bye":
                print("Server requested to close the connection. Closing...")
                break

    except ConnectionResetError:
        print("Connection reset by the server.")
    except ConnectionAbortedError:
        print("Connection aborted.")
    except OSError as e:
        print(f"Error: {e}")
    finally:
        client.close()

def send_messages(client):
    try:
        while True:
            message = input("Client: ")
            client.send(message.encode("utf-8"))

            if message.lower() == "bye":
                print("Closing the connection. Goodbye!")
                break

    except OSError as e:
        print(f"Error: {e}")
    finally:
        client.close()

# Your original client code
if len(sys.argv) != 2 or not is_valid_mac(sys.argv[1]):
    print("Usage: python script_name.py <server_mac_address>")
    print("Please check the MAC address format.")
    sys.exit(1)
server_mac_address = sys.argv[1]
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    client.connect(({server_mac_address}, 4))
    server_address, server_port = client.getpeername()
    print(f"Connected to server at {server_address}:{server_port}")

    # Create two threads, one for receiving and one for sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client,))

    # Start both threads
    receive_thread.start()
    send_thread.start()

    # Wait for both threads to finish
    receive_thread.join()
    send_thread.join()

except OSError as e:
    print(f"Error: {e}")

finally:
    client.close()
