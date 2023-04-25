import sqlite3 as sq

'''Create a connection to a database and create a cursor object.\
The cursor object is used to execute SQL statements and traverse the records in the database.'''

conn =sq.connect("database.db", check_same_thread=False)
c = conn.cursor()


'''This code is an example of a database connection using the sqlite3 library in Python.\
It contains functions to create a table, add user data, delete data, check for email, select users based on a prediction,\
and view all data.'''

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT,email TEXT,prediction TEXT)')

def add_userdata(username, email, prediction):
    c.execute('INSERT INTO usertable(username,email,prediction) VALUES (?,?,?)', (username, email, prediction))
    conn.commit()

def delete():
    c.execute('DELETE FROM usertable')
    conn.commit()

def check_mail(email):
    c.execute('SELECT email FROM usertable WHERE email = ?', [email])
    got = c.fetchall()
    return got
def select_user(pred):
    c.execute('SELECT username,email FROM usertable WHERE prediction = ?', [pred])
    new = c.fetchall()
    return new
def view_all_data():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data

