from model.write_db import Write_db


class Controller:
    def __init__(self) -> None:
        self.write_db = Write_db()

    def insert_new_user(self, username, userid, password):
        write_db.insert_new_user(username, userid, password)