from model.write_db import Write_db
from model.read_db import Read_db


class Controller:
    def __init__(self) -> None:
        self.write_db = Write_db()
        self.read_db = Read_db()

    def insert_new_user(self, username, userid, password):
        self.write_db.insert_new_user(username, userid, password)

    #this function is not functional
    def retrieve_all_users(self):
        return self.read_db.retrieve_users()