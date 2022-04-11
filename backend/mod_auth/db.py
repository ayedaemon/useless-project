import sqlite3
from dataclasses import dataclass
from datetime import datetime
from flask import current_app

@dataclass
class UserAuthDB:
    email: str
    username: str
    passwd: str
    last_passwd_date: str = datetime.now()
    last_login_date: str = None
    account_created_date: str = datetime.now()

    def db_add_user(self):
        status = add_row({
            'email': self.email,
            'username' : self.username,
            'passwd' : self.passwd,
            'last_passwd_date' : self.last_passwd_date,
            'last_login_date' : self.last_login_date,
            'account_created_date' : self.account_created_date
        })
        return status




def add_row(data):
    try:
        print(data)
        conn = open_conn('auth.db')
        c = conn.cursor()
        c.execute(f"""INSERT INTO auth (email, username, passwd, last_passwd_date, last_login_date, account_created_date) VALUES (
            "{data.get('email')}",
            "{data.get('username')}",
            "{data.get('passwd')}",
            "{data.get('last_passwd_date')}",
            "{data.get('last_login_date')}",
            "{data.get('account_created_date')}"
        )""")
        conn.commit()
        close_conn(conn)
        return True
    except sqlite3.IntegrityError:
        print("User already registered")
        return False
    except sqlite3.OperationalError as err:
        print(f'Failed to add row. {err}')


def open_conn(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.OperationalError as err:
        current_app.logger.error('Error with database. Error:- {err}')
    return conn
    
        


def close_conn(conn):
    conn.close()       


def create_table(conn):
    c = conn.cursor()
    status = None
    try:
        status = c.execute("""CREATE TABLE auth (
            email text primary key,
            username text,
            passwd text,
            last_passwd_date text,
            last_login_date text,
            account_created_date text
            )
        """)
        con.commit()
        return True
    except sqlite3.OperationalError as err:
        print(f"Failed to create auth table in DB. {err} ")
        return False
    return status
