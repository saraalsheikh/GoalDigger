import mysql.connector


class Write_db():

    def __init__(self):
        pass

    def open_db(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="uqTjt8dc",
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

    def insert_user_info(self, user_id, user_name, password):
        self.open_db()
        self.mycursor.execute(f"INSERT INTO user_info (user_id, user_name,password) Values('{user_id}', '{user_name}', '{password}')")
        self.mydb.commit()
        self.close_db()