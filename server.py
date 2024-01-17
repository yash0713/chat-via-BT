import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    server.bind(("C8:E2:65:CD:D7:FE", 4))
    server.listen(1)
    print("Waiting for incoming connections...")

    client, addr = server.accept()
    print(f"Connected to {addr}")

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

            response = input("Server:")
            client.send(response.encode("utf-8"))

    except ConnectionResetError:
        print("Connection reset by the client.")
    except ConnectionAbortedError:
        print("Connection aborted.")
    except OSError as e:
        print(f"Error: {e}")
    finally:
        client.close()

except OSError as e:
    print(f"Socket error: {e}")

finally:
    server.close()
    print("Server closed.")
