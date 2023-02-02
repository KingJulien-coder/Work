import sqlite3


with sqlite3.connect("users.db") as conn:
    conn.execute('CREATE TABLE users(username TEXT not null, password TEXT not null)')

'''
with sqlite3.connect('admin_login.db') as conn:
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS `admin_login` (`admin_id` int(11) NOT NULL AUTO_INCREMENT,`admin_name` varchar(250) NOT NULL,`admin_password` varchar(250) NOT NULL)')


    #conn.execute("INSERT INTO admin_login(admin_id,admin_name,admin_password) VALUES (1,'admin','pbkdf2:sha256:150000$FXLDgm3a$bd46f6b7b44124a523f9566d03bf110ba2ebf28bfd3522faeddd56eabebcb7f5')")
    #print('added successfully')
    


conn.execute('CREATE TABLE user(id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password TEXT, name TEXT, membership TEXT)')
print('Table created successffuly');conn.close()'''
