# Libraries
import tkinter as tk
import sqlite3

# Input
login = input()
password = input()
# Logic
conn = sqlite3.connect('data/Users.sqlite')
curr = conn.cursor()
res = curr.execute(f"SELECT * FROM users WHERE login='{login}' AND password='{password}'")
res = res.fetchall()
conn.close()
# Output
print(res)
if res:
    print('User Found')
else:
    print('Wrong User name or Password')