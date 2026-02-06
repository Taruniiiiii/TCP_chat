import socket
import threading

SERVER_IP = "192.168.137.137"   # YOUR server IP
PORT = 7001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

def receive_from_server():
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                print("\nServer disconnected")
                break
            print("\nServer:", msg)
        except:
            break

def send_to_server():
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break
        client.send(msg.encode())

threading.Thread(target=receive_from_server, daemon=True).start()
send_to_server()

client.close()
print("Client closed")