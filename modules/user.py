from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from modules.connections import connection

class User(UserMixin):

    def __init__(self, id: int):
        self.id = id
    
    def get_username(self) -> str:
        username = ""

        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT Username FROM Users WHERE ID = ?", self.id)

            record = cursor.fetchone()
            username = record.Username

        return username

    def get_email(self) -> str:
        email = ""

        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT Email FROM Users WHERE ID = ?", self.id)

            record = cursor.fetchone()
            email = record.Email

        return email

    def __repr__(self) -> int:
        return self.id

    @staticmethod
    def validate_user(identifier: str, password: str) -> bool:
        valid = False

        with connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT ID, Username, Password
                            FROM Users
                            WHERE Username = ? OR Email = ?""", identifier, identifier)

            record = cursor.fetchone()

            if record:
                hashed = record.Password

                if check_password_hash(hashed, password):
                    valid = True

        return valid

    @staticmethod
    def get_user_id(identifier: str) -> int:
        user_id = None

        with connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT ID
                            FROM Users
                            WHERE Username = ? OR Email = ?""", identifier, identifier)

            record = cursor.fetchone()

            if record:
                user_id = record.ID
        
        return user_id

class Create_User:

    def __init__(self, username: str, email: str, password: str):
        self.__username = username
        self.__email = email
        self.__password = generate_password_hash(password)

    def validate_user(self) -> bool:
        found = True

        with connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT ID 
                            FROM Users 
                            WHERE Username = ? OR Email = ?""", self.__username, self.__email)

            record = cursor.fetchone()

            if record:
                found = False
        
        return found

    def create_user(self):
        with connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO Users(Username, Email, Password) 
                            values(?, ?, ?)""", self.__username, self.__email, self.__password)

        connection.commit()