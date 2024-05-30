from model.write_db import Write_db
from model.read_db import Read_db


class Controller:
    def __init__(self) -> None:
        self.write_db = Write_db()
        self.read_db = Read_db()

<<<<<<< HEAD
    def insert_new_user(self, user_id, username, password):
        self.write_db.insert_new_user(user_id, username, password)

    #this function is not functional
    def retrieve_all_users(self):
        return self.read_db.retrieve_users()
    
    def fetch_user_id(self, username):
        return self.read_db.fetch_user_id(username)
=======

# Write_db methods
    def insert_new_user(self, username, userid, password):
        self.write_db.insert_new_user(username, userid, password)
>>>>>>> main
    
    def insert_plan(self, plan):
        self.write_db.insert_plan(plan)

    def insert_mood(self, user_mood, user_id, current_datetime):
        self.write_db.insert_mood(user_mood, user_id, current_datetime)

#Reade_db methods 
    def fetch_user_id(self, username):
        return self.read_db.fetch_user_id(username)  
    
    def authenticate_user(self, username, password):
        return self.read_db.authenticate_user(username, password)
    
    
    def fetch_plans(self, user_id): 
        return self.read_db.fetch_plans(user_id)
