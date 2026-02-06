import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", 7001))
server_socket.listen()

print("Server started on port 7001")
client_socket, addr = server_socket.accept()
print("Client connected:", addr)

def receive_from_client():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                print("\nClient disconnected")
                break
            print("\nClient:", msg)
        except:
            break

def send_to_client():
    while True:
        msg = input("Server: ")
        if msg.lower() == "exit":
            break
        client_socket.send(msg.encode())

threading.Thread(target=receive_from_client, daemon=True).start()
send_to_client()

client_socket.close()
server_socket.close()
print("Server closed")
