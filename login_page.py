# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:44:33 2023

@author: Admin
"""

# ==================imports===================
import subprocess
import MySQLdb as db
import tkinter as t
#from tkinter import *
from tkinter import messagebox
# ============================================

root = t.Tk()
root.geometry("1366x768")
root.title("School Management ")
root.resizable(0,0)


def login(Event=None):
    username = user.get()
    password = passwd.get()

    con=db.connect(host='localhost',user='root',password='',db='school')
    cur = con.cursor()
    #INSERT IN LOGIN TABLE ID AND PASSWORD
    #cur.execute("insert into login values ('"+user.get()+"','"+ passwd.get()+"')")
    #con.commit()
    
    #find_user = "SELECT * FROM login WHERE id = '"+user.get()+"' and password = '"+passwd.get()+"' "
    #cur.execute(find_user)
    #results = cur.fetchall();
    #print("..................",results)

    sql = "select * from login where id = %s and password = %s"
    cur.execute(sql,[(username),(password)])
    results = cur.fetchall()
    if results:
        global page2
        page2=subprocess.run(["python", "main_file.py"])
    else:
        messagebox.showerror("Error", "Incorrect username or password.")

user = t.StringVar()
passwd = t.StringVar() 

label1 = t.Label(root)
label1.place(relx=0, rely=0, width=1366, height=768)
img = t.PhotoImage(file="./images/admin_login.png")
label1.configure(image=img)

entry1 = t.Entry(root)
entry1.place(relx=0.373, rely=0.273, width=374, height=24)
entry1.configure(font="-family {Poppins} -size 10")
entry1.configure(relief="flat")
entry1.configure(textvariable=user)

entry2 = t.Entry(root)
entry2.place(relx=0.373, rely=0.384, width=374, height=24)
entry2.configure(font="-family {Poppins} -size 10")
entry2.configure(relief="flat")
entry2.configure(show="*")
entry2.configure(textvariable=passwd)

button1 = t.Button(root)
button1.place(relx=0.366, rely=0.685, width=356, height=43)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#D2463E")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#D2463E")
button1.configure(font="-family {Poppins SemiBold} -size 20")
button1.configure(borderwidth="0")
button1.configure(text="""LOGIN""")
button1.configure(command=login)

root.mainloop()
