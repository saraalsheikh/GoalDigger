from model.write_db import Write_db
from model.read_db import Read_db


class Controller:
    def __init__(self) -> None:
        self.write_db = Write_db()
        self.read_db = Read_db()

    def insert_new_user(self, user_id, username, password):
        self.write_db.insert_new_user(user_id, username, password)

    #this function is not functional
    def retrieve_all_users(self):
        return self.read_db.retrieve_users()
    
    def fetch_user_id(self, username):
        return self.read_db.fetch_user_id(username)
    
    def insert_plan(self, plan):
        self.write_db.insert_plan(plan)
    
    def authenticate_user(self, username, password):
        return self.read_db.authenticate_user (username, password)
