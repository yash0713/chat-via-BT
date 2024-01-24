import socket
import threading

def receive_messages(client):
    try:
        while True:
            data = client.recv(1024)
            if not data:
                break

            message = data.decode('utf-8')
            print(f"Client: {message}")

            if message.lower() == "bye":
                print("Client requested to close the connection. Closing...")
                break

    except ConnectionResetError:
        print("Connection reset by the client.")
    except ConnectionAbortedError:
        print("Connection aborted.")
    except OSError as e:
        print(f"Error: {e}")
    finally:
        client.close()

def send_messages(client):
    try:
        while True:
            response = input("Server: ")
            client.send(response.encode("utf-8"))

            if response.lower() == "bye":
                print("Closing the connection. Goodbye!")
                break

    except OSError as e:
        print(f"Error: {e}")
    finally:
        client.close()



## connection establish.
server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    server.bind(("C8:E2:65:CD:D7:FE", 4))
    server.listen(1)
    print("Waiting for incoming connections...")

    client, addr = server.accept()
    print(f"Connected to {addr}")

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
    print(f"Socket error: {e}")

finally:
    server.close()
    print("Server closed.")
