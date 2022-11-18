import mysql.connector
import hashlib, pwinput

class db_commands():
    def __init__(self, _user = "root", _pass = "m::26~{QFuJZ", _host = "localhost", db_name = "mvp_db", interactive = False):
        self._user = _user
        self._pass = _pass
        self._host = _host
        self.db_name = db_name
        if (interactive):
            self._user = input("Enter db user: ")
            self._pass = pwinput.pwinput("Enter db pass: ")
            self._host = input("Enter db host: ")
            self._db_name = input("Enter db name: ")
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
            return True
        except:
            print ("Failed to add customer into database.")
        return False
    
    def get_customer_base(self):
        select_stmt = """SELECT * FROM customer"""
        try:
            self.cursor.execute(select_stmt)
            return self.cursor.fetchall()
        except:
            print("Failed to retrieve customers from database.")
        return []
    
    def authenticate_login(self, c_uname, c_pass):
        select_stmt = """SELECT * FROM customer WHERE c_uname = %s and c_pass = %s"""
        hashed_pass = hashlib.sha256(c_pass.encode('ascii')).hexdigest()

        login_data = (c_uname, hashed_pass)
        try:
            self.cursor.execute(select_stmt, login_data)
            user = self.cursor.fetchall()
            if (self.cursor.rowcount == 1):
                print("login successful.")
                return user[0]
        except:
            pass
        print("Failed to login user.")
        return ()


    def add_recipe(self,r_name,r_desc,r_nutri,r_etype,r_price,m_id):
        select_stmt = "INSERT INTO recipe(r_name,r_desc,r_nutri,r_etype,r_price,m_id) VALUES (%s,%s,%s,%s,%s,%s)"
        recipe_data = (r_name,r_desc,r_nutri,r_etype,r_price,1)
        try:
            self.cursor.execute(select_stmt,(recipe_data))
            self.db.commit() 
            print ("recipe added successfully!")
        except:
            print("Failed to add recipe to database.")

    def remove_recipe(self,r_name,r_id):
        if r_name == "":
            q1 = "DELETE FROM recipe WHERE r_id = %s"
            try:
                self.cursor.execute(q1,tuple(r_id))
                self.db.commit()
                print("Recipe succesfully deleted")
            except:
                print("Failed to delete recipe")
            
        else:
            q2 = "DELETE FROM recipe WHERE r_name = %s"
            try:
                self.cursor.execute(q2,(r_name,))
                self.db.commit()
                print("Recipe succesfully deleted")
            except:
                print("Failed to delete recipe")
    

    def get_recipes(self):
        select_stmt = """SELECT * FROM recipe"""
        try:
            self.cursor.execute(select_stmt)
            return self.cursor.fetchall()
        except:
            print("Failed to retrieve recipes from database.")
        return []
    
    def get_recipe_id(self, r_name):
        select_stmt = """SELECT r_id FROM recipe
                         WHERE r_name = %s"""
        print (r_name.lower())
        recipe_data = (r_name.lower(),)

        try:
            self.cursor.execute(select_stmt, recipe_data)
            data_retrived = self.cursor.fetchone()
            if (len(data_retrived) == 1):
                return data_retrived[0]
        except:
            print("Failed to retrieve recipe item.")
            return -1 
    
    def get_cart_info(self, r_id):
        select_stmt = """SELECT r_id, r_name, r_price
                         FROM recipe WHERE r_id = %s"""
        recipe_data = (r_id,)
        try:
            self.cursor.execute(select_stmt, recipe_data)
            data_retrieved = self.cursor.fetchall()
            if (len(data_retrieved) == 1):
                return data_retrieved[0]
        except:
            print("Failed to get cart info from db.")

    