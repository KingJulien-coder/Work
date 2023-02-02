import sqlite3


with sqlite3.connect("users.db") as conn:
    cur = conn.cursor()
    email = 'second@gmail.com'
    password = "456DEF"
    name = 'Samantha'
    membership = False
    
    conn.execute('INSERT INTO user(email,password,name,membership) VALUES (?,?,?,?)',(email,password,name,membership))
    msg = "Record successfully added"
