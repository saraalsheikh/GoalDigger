import mysql.connector


class Write_db():

    def __init__(self):
        pass

    def open_db(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="GoalDigger"
            )
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.mycursor = self.mydb.cursor()

    def close_db(self):
        self.mycursor.close()
        self.mydb.close()

    def insert_new_user(self, user_id, username, password):
        self.open_db()
        self.mycursor.execute(f"INSERT INTO user_info (user_id, user_name, password) Values('{user_id}', '{username}', '{password}')")
        self.mydb.commit()
        self.close_db()

    def insert_plan(self, plan):
      plan_text = plan[0]
      plan_date = plan[1]
      user_id = plan[2]
      self.open_db()
      self.mycursor.execute(f"INSERT INTO to_do_list ( user_id, plan_text, plan_date) VALUES ('{user_id}', '{plan_text}', '{plan_date}')")
      self.mydb.commit()
      self.close_db()
    

    def insert_mood(self, user_mood, user_id, current_datetime):
        self.open_db()
        self.mycursor.execute(f"INSERT INTO mood (user_id, user_mood, mood_date) VALUES ('{user_id}', '{user_mood}', '{current_datetime}')")
        self.mydb.commit()
        self.close_db()
