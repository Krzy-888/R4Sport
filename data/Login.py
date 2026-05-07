# Libraries
import tkinter as tk
from tkinter import ttk
import sqlite3
from typing import Protocol
# Input
class DataInput(Protocol):
    def read(self,widget) -> str: ...

class TextBoxInput:
    def read(self,widget) -> str:
        text = widget.get()
        return text



# login = input()
# password = input()

def GetLoginNPassword(LW,PW):
    login = TextBoxInput().read(widget=LW)
    password = TextBoxInput().read(widget=PW)
    return [login, password]

def ExecuteQuery(cur,LW,PW):
    login, password = GetLoginNPassword(LW,PW)
    res = cur.execute(f"SELECT * FROM users WHERE login='{login}' AND password='{password}'")
    res = res.fetchall()
    print(res)

    if res:
        print('User Found')
    else:
        print('Wrong User name or Password')

# Logic
conn = sqlite3.connect('data/Users.sqlite')
curr = conn.cursor()



# UI
root = tk.Tk()
root.title('R4Sport')
mainframe = tk.Frame(root)
mainframe.pack(fill='both',expand=True)
mainframe.grid_columnconfigure(0, weight=1)
frame = ttk.Frame(mainframe, padding=10)
frame.grid(row=0, column=0, sticky="ew")
frame.grid_columnconfigure(0, weight=1, uniform="equal")
frame.grid_columnconfigure(1, weight=1, uniform="equal")
label_Login = ttk.Label(frame, text="Login:", anchor="w")
label_Login.grid(row=0, column=0, sticky="ew",padx=10,pady=10)
entry_Login = ttk.Entry(frame)
entry_Login.grid(row=0, column=1, sticky="ew",padx=10,pady=10)
label_password = ttk.Label(frame, text="Password:", anchor="w")
label_password.grid(row=1, column=0, sticky="ew",padx=10,pady=10)
entry_pass = ttk.Entry(frame,show='*')
entry_pass.grid(row=1, column=1, sticky="ew",padx=10,pady=10)
Button = ttk.Button(mainframe,text='login',
                    command=lambda : ExecuteQuery(curr,entry_Login,entry_pass)
                    ).grid(sticky='s',padx=10,pady=10)
root.mainloop()



conn.close()

# Output
# print(res)
# if res:
#     print('User Found')
# else:
#     print('Wrong User name or Password')