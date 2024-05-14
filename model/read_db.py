import mysql.connector

class Read_db:
    def __init__(self):
        pass
    
    def open_db(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="uqTjt8dc",
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
    

    #this function is not functional
    def retrieve_users(self, user_id):
        return "users_list"