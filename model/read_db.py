import mysql.connector

class Read_db:
    def __init__(self):
        pass
    
    def open_db(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="GoalDigger",
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

    def get_user_info(self, user_id):
        self.open_db()
        self.mycursor.execute(f"SELECT * From user_info Where user_id = '{user_id}';")
        self.list_of_tuples = self.mycursor.fetchall()
        user_info_list = []
        for tuple in self.list_of_tuples:
            user_info_list.append(str(tuple[0])) 
            user_info_list.append(str(tuple[1]))
            user_info_list.append(str(tuple[2]))
        self.close_db()
        return user_info_list 
    
    def check_cridential(self, user_name, password):
        self.open_db()
        self.mycursor.execute(f"SELECT * FROM user_info WHERE user_name = '{user_name}' and password = '{password}';")
        result = self.mycursor.fetchone()
        user_info_list = []
        for tuple in result:
            user_info_list.append(str(tuple[0])) 
            user_info_list.append(str(tuple[1]))
            user_info_list.append(str(tuple[2]))
            self.close_db()
        if user_info_list !=[]:
            return True
        return  False
    
    
    def fetch_user_id(self, username):
        self.open_db()
        
        # Prepare the query to get the user_id based on the username
        query = "SELECT user_id FROM user_info WHERE user_name = %s;"
        
        # Execute the query with the provided username
        self.mycursor.execute(query, (username,))
        user_id_tuple = self.mycursor.fetchone()
        self.close_db()
        
        if user_id_tuple:
            return str(user_id_tuple[0])
        else:
            return None
    
    
    def authenticate_user(self, username, password):
        self.open_db()
        self.mycursor.execute(f"SELECT * FROM user_info WHERE user_name = '{username}' AND password = '{password}';")
        self.list_of_tuples = self.mycursor.fetchall()
        
        self.close_db()

        if self.list_of_tuples == []:
          return False
        else:
          return True
    
    def fetch_plans(self, user_id):
        self.open_db()
        self.mycursor.execute(f"SELECT plan_date, plan_text FROM to_do_list WHERE user_id = '{user_id}';")
        self.list_of_tuples = self.mycursor.fetchall()
    
        user_plans_list = []
        for (plan_date, plan_text) in self.list_of_tuples:
            formatted_plan = str(plan_date) + " " + plan_text  # Convert date to string
            user_plans_list.append(formatted_plan)
        self.close_db()
    
        return user_plans_list
    
    def fetch_mood(self, user_id):
        self.open_db()
        self.mycursor.execute(f"SELECT user_mood, mood_date FROM mood WHERE user_id = '{user_id}'")
        self.list_of_tuples = self.mycursor.fetchall()
    
        user_moods_list = []
        for (mood_date, user_mood) in self.list_of_tuples:
            formatted_mood = str(mood_date) + " " + str(user_mood)  # Convert date to string
            user_moods_list.append(formatted_mood)
        self.close_db()

        return user_moods_list


