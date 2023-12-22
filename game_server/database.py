import mysql.connector
from datetime import datetime

class DB:
    # Thiết lập thông tin kết nối
    host = "localhost"  # Địa chỉ IP hoặc tên máy chủ của máy chủ MySQL (localhost nếu chạy trên máy cá nhân)
    user = "root"       # Tên người dùng MySQL
    password = ""       # Mật khẩu MySQL (thường để trống mật khẩu trong cấu hình mặc định của XAMPP)
    database = "bp4_db"  # Tên của cơ sở dữ liệu bạn muốn kết nối

    def connect_db(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                return connection
        except mysql.connector.Error as error:
            print("Connection error:", error)
        return None
    
    def insert(self, query, params):
        connection = self.connect_db()
        if (connection):   
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            cursor.close()
            connection.close()
    
    def select(self, query, params):
        connection = self.connect_db()
        if (connection):
            cursor = connection.cursor()
            if params: cursor.execute(query, params)
            else: cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            connection.close()
            return records
        else: return None

    
    def getUser(self, username, password):
        connection = self.connect_db()
        if (connection):
            cursor = connection.cursor()
            query = f"Select * from users where username = '{username}' and password = '{password}'"
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            connection.close()
            return records
        else: return None

    
    def getUsers(self):
        connection = self.connect_db()
        if (connection):
            cursor = connection.cursor()
            query = "SELECT * FROM USERS"
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            connection.close()
            return records
        else: return None

    def insertUser(self, user):
        query = "insert into users (username, password, display_name, phone) values (%s, %s, %s, %s)"
        self.insert(query, (user[0], user[1], user[2], user[3]))