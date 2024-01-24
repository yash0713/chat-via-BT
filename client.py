import socket
import threading

def receive_messages(client):
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break

            server_message = data.decode('utf-8')
            print(f"Server: {server_message}")

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
client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    client.connect(("C8:E2:65:CD:D7:FE", 4))
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
