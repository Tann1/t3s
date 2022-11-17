import mysql.connector

## GLOBALS
db_name = "mvp_db"
_user = "root"
_pass = "surewhynot1"
_host = "localhost"

def create_mvp_db(cur):
    try:
        cur.execute("DROP DATABASE IF EXISTS " + db_name)
        cur.execute("CREATE DATABASE " + db_name)
        cur.execute("USE " + db_name)
    except:
        print("Failed to create database.")

def create_customer(cur):
    try:
        cur.execute("""CREATE TABLE customer (
            c_id    integer not null auto_increment,
            c_fname varchar(255) not null,
            c_lname varchar(255) not null,
            c_uname varchar(255) not null unique,
            c_email varchar(255) not null,
            c_pass  varchar(256) not null,
            c_addr  varchar(255),
            primary key (c_id)
        )""")
    except:
        print("Failed to create customer table.")

def create_subcriber(cur):
    try:
        cur.execute("""CREATE TABLE subscriber (
            sub_discount    decimal(3, 2),
            sub_loyal_pt    integer not null default 0,
            sub_free_del    boolean not null default true,
            c_id            integer not null,
            unique(c_id),
            foreign key (c_id) references customer(c_id)
                            ON DELETE CASCADE
        )
        """)
    except:
        print("Failed to create subcriber table.")

def create_manager(cur):
    try: 
        cur.execute("""CREATE TABLE manager (
            m_id    integer not null auto_increment,
            m_fname varchar(255) not null,
            m_lname varchar(255) not null,
            primary key (m_id)
            )
        """)
    except:
        print("Failed to create manager table.")

def create_supervisor(cur): 
    try:
        cur.execute("""CREATE TABLE supervisor (
            s_id    integer not null auto_increment,
            s_fname varchar(255) not null,
            s_lname varchar(255) not null,
            m_id    integer,
            primary key (s_id),
            foreign key (m_id) references manager(m_id)
        )
        """)
    except:
        print("Failed to create supervisor.")
    
def create_delivery_person(cur):
    try:
        cur.execute("""CREATE TABLE delivery_person (
            d_id    integer not null auto_increment,
            d_fname varchar(255) not null,
            d_lname varchar(255) not null,
            ds_id   integer not null,
            primary key (d_id),
            foreign key (ds_id) references supervisor(s_id)
        )
        """)
    except:
        print("Failed to create delivery person table.") 

def create_inventory(cur):
    try:
        cur.execute("""CREATE TABLE inventory (
            i_id    integer not null auto_increment,
            i_name  varchar(255) not null,
            i_exp   date not null,
            i_quan  integer not null,
            is_id   integer not null,
            primary key (i_id),
            foreign key (is_id) references supervisor(s_id)
        )
        """)
    except:
        print("Failed to create iventory table.")

        
def create_recipe(cur):
    try:
        cur.execute("""CREATE TABLE recipe (
            r_id    integer not null auto_increment,
            r_name varchar(255) not null,
            r_desc  varchar(255) not null,
            r_nutri varchar(255) not null,
            r_etype varchar(255) not null,
            r_price integer not null, 
            m_id    integer not null,
         
            primary key (r_id),
#UNIQUE KEY `r_name_UNIQUE` (`r_name`)  
            foreign key (m_id) references manager(m_id)
        )
        """)
    except:
        print("Failed to create recipe table.")

def create_ingredients(cur):
    try:
        cur.execute("""CREATE TABLE ingredients (
            i_id    integer not null,
            r_id    integer not null,
            unique(i_id, r_id), 
            foreign key (i_id) references inventory(i_id),
            foreign key (r_id) references recipe(r_id)
                ON DELETE CASCADE
        )
        """)
    except:
        print("Failed to create ingredeints table.")

def create_feedback(cur):
    try:
        cur.execute("""CREATE TABLE feedback (
            c_id    integer not null,
            cs_id   integer not null,
            fd_txt  varchar(255) not null,
            unique(c_id, cs_id, fd_txt), 
            foreign key (c_id) references customer(c_id)
                ON DELETE CASCADE,
            foreign key (cs_id) references supervisor(s_id)
        )
        """)
    except:
        print("Failed to create feedback table.")

def create_customer_order(cur):
    try:
        cur.execute("""CREATE TABLE customer_order (
            o_id        integer not null auto_increment,
            o_cancel    boolean not null default false,
            o_timestamp timestamp not null default current_timestamp,
            d_id        integer not null,
            c_id        integer not null,
            primary key (o_id),
            foreign key (d_id) references delivery_person(d_id),
            foreign key (c_id) references customer(c_id)
                ON DELETE CASCADE     
        )
        """)
    except:
        print("Failed to create customer order table.")
    
def create_order_list(cur):
    try:
        cur.execute("""CREATE TABLE order_list (
            o_id    integer not null,
            r_id    integer not null,
            foreign key (o_id) references customer_order(o_id)
                ON DELETE CASCADE,
            foreign key (r_id) references recipe(r_id) 
        )
        """)
    except:
        print("Failed to create order list table.")

def init_db(db):
    cursor = db.cursor()
    create_mvp_db(cursor)
    create_customer(cursor)
    create_subcriber(cursor)
    create_manager(cursor)
    create_supervisor(cursor)
    create_delivery_person(cursor)
    create_inventory(cursor)
    create_recipe(cursor)
    create_ingredients(cursor)
    create_feedback(cursor)
    create_customer_order(cursor)
    create_order_list(cursor)
    cursor.close()

if __name__ == "__main__":
    db = mysql.connector.connect(user=_user, password=_pass, host=_host)
    init_db(db)
    db.close()
