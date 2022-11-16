import mysql.connector
import hashlib

class db_commands():
    def __init__(self, _user = "root", _pass = "surewhynot1", _host = "localhost", db_name = "mvp_db"):
        self._user = _user
        self._pass = _pass
        self._host = _host
        self.db_name = db_name
        self.db = mysql.connector.connect(user=self._user, password=self._pass, host=self._host, database=self.db_name)
        if self.db.is_connected():
            self.cursor = self.db.cursor()
            self.cursor.execute("USE " + self.db_name)
            print("Connection to database successful!")
        else:
            print("Failed to connect to database.")
    
    def __del__(self):
        try:
            self.db.close()
            self.cursor.close()
        except:
            pass
    
    def insert_new_customer(self, c_fname, c_lname, c_uname, c_email, c_pass, c_addr):
        insert_stmt = """INSERT customer (c_fname, c_lname, c_uname, c_email, c_pass, c_addr)
                         VALUES (%s, %s, %s, %s, %s, %s)
        """
        hash_algo = hashlib.new('sha256')
        hash_algo.update(c_pass.encode('ascii'))
        hashed_pass = hash_algo.hexdigest()
        customer_data = (c_fname, c_lname, c_uname, c_email, hashed_pass, c_addr)
        try:
            self.cursor.execute(insert_stmt, customer_data)
            self.db.commit() 
            print(self.cursor.lastrowid)
            print ("customer added successfully!")
        except:
            print ("Failed to add customer into database.")
    
    def get_customer_base(self):
        select_stmt = """SELECT * FROM customer"""
        try:
            self.cursor.execute(select_stmt)
            return self.cursor.fetchall()
        except:
            print("Failed to commit customer to database.")
        return []
        





# if __name__ == "__main__":
#     db = db_commands()
#     db.insert_new_customer("tanishq", "gadkari", "tannn", "gadkaritanishq@gmail.com", "123", "1234 addr st. city, ST 12345")
    

#     for customer in db.get_customer_base():
#         print(*customer)

