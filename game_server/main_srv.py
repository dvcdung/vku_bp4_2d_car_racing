import os
import socket
import threading
import mysql
import json
from database import DB

# Định nghĩa thư mục chứa dữ liệu của các tài khoản
DATA_DIR = "server_data"
IP_ADDR = "127.0.0.1"
PORT_NUM = 12345
db = DB()
onlineUsers = {}
matches = {}

# Tạo thư mục chứa dữ liệu
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def handle_client(client_socket: socket.socket):
    try:

        while True:
            client_msg = client_socket.recv(2048).decode()
            if client_msg:
                (id, data) = client_msg.split(":", 1)
                if id == "0000": # Tạo tài khoản
                    username, password, displayname = data.split("|", 3)
                    db.insertUser((username, password, displayname))
                    client_socket.send("OK:Account successfully created".encode())
                elif id == "0001": # Đăng nhập
                    username, password = data.split("|", 1)
                    users = db.getUser(username, password)
                    if users and len(users) == 1:
                        userData = "|".join(list(map(str, users[0])))
                        client_socket.send(f"OK:{userData}".encode())
                        onlineUsers[username] = (client_socket, users[0])
                    else:
                        client_socket.send(f"ER:Failed".encode())
                    print(onlineUsers)
                elif id == "0003": # Đăng xuất
                    username = data
                    del onlineUsers[username]
                    print(f"Client named {username} is disconnected!\n")
                    client_socket.send(f"OK:Log out successfully!".encode())
                    print(onlineUsers)
                elif id == "0010": # Tạo trận đấu
                    username = data
                    matches[username] = []
                elif id == "0011": # Tham gia trận đấu
                    key_match, username = data.split("|")
                    while(len(matches[key_match]) < 2):
                        matches[key_match].append(username)
                        print(matches[key_match])
                        client_socket.send(f"OK:{len(matches[key_match])}".encode())
                elif id == "0013": # Bat dau tran dau
                    pass

                    
    except ConnectionResetError:
        for username, (user_socket, _) in list(onlineUsers.items()):
            if (user_socket == client_socket):
                del onlineUsers[username]
                print(f"Client named {username} is disconnected!\n")
                break
    except mysql.connector.errors.IntegrityError:
        client_socket.send("ER:Failed".encode())
                    
def server_main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP_ADDR, PORT_NUM))
    server.listen(5)
    print(f"Server is listening at {IP_ADDR}:{PORT_NUM}")

    while True:
        client_socket, client_addr = server.accept()
        print(f"Chấp nhận kết nối từ {client_addr[0]}:{client_addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    server_main()