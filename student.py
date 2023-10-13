# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 06:07:10 2023

@author: BAPS
"""

import tkinter as t 
import MySQLdb as db
import re
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
from PIL import Image,ImageTk
from datetime import datetime
from datetime import date
from tkcalendar import DateEntry

def add_student():
    global add_stu
    add_stu = t.Toplevel()
    add_stu.title("Add Student")
    add_stu.configure(background="#7f8b98")
    t.Frame(add_stu,pady=50,padx=100)
    add_stu.geometry("1450x850")
    
    global stu_reg_no
    global stu_nm
    global stu_dob
    #global stu_age
    global stu_class
    global current_date
    global stu_address
    global stu_gender
    global stu_email
    global stu_con
    global d1
        
    global stu_reg_no_entry
    global stu_nm_entry
    global stu_dob_entry
    global stu_age_entry_lbl
    global stu_class_entry
    global current_date_entry
    global stu_address_entry
    global stu_gender_entry
    global stu_email_entry
    global stu_con_entry
    
    stu_reg_no=t.StringVar()
    stu_nm=t.StringVar()
    stu_dob=t.StringVar()
    #stu_age=t.StringVar()
    stu_class=t.StringVar()
    current_date=t.StringVar()
    stu_address=t.StringVar()
    stu_gender=t.StringVar(value='male')
    stu_email=t.StringVar()
    stu_con=t.StringVar()
    """
    def showimage():
        global filename
        global img
        
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetype=(("JPG file","*.jpg"),("PNG file","*.png"),("JFIF file","*.jfif"),("All files","*.txt")))
        img=(Image.open(filename)) 
        resized_image=img.resize((190,190)) 
        photo2=ImageTk.PhotoImage(resized_image) 
        #t.config(image=photo2)
        #t.image=photo2
        """
    def calculate_age(event):
        global birthdate
        global age

        birthdate = stu_dob_entry.get()
        try:
            birthdate = datetime.strptime(birthdate, "%d-%m-%Y")
            today = datetime.now()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            stu_age_entry_lbl.config(text=age)
            return age
        except ValueError:
            stu_age_entry_lbl.config(text="Invalid date format")
            
    def valid_phone(phn):
         if re.match(r"[789]\d{9}$", phn):
             return True
         return False

    def add_btn_student():
        age = calculate_age(stu_dob_entry.get())
        date_pattern = r'^\d{2}-\d{2}-\d{4}$' 
        if stu_reg_no.get()=="" or stu_nm.get() =="" or stu_class.get()=="" or current_date.get()=="" or stu_address.get()=="" or stu_gender.get()=="" or stu_email.get()=="" or stu_con.get()=="" :
             messagebox.showerror('Error','All Fields required',parent=add_stu) 
        elif not re.match(date_pattern, stu_dob_entry.get()):
              messagebox.showerror("Error","Invaild Date Formate",parent=add_stu)
        elif age is None:
                 messagebox.showerror("Error","Age calculation failed",parent=add_stu)
        else:
            con=db.connect(host='localhost',user='root',password='',db='school')
            cur = con.cursor()
            cur.execute("SELECT * FROM add_student where stu_reg_no = %s"%(stu_reg_no.get()))
            records=cur.fetchone()
            if records:
                messagebox.showinfo("Error","ID is alreay exists",parent=add_stu)
            else:
                if valid_phone(stu_con.get()):
                    query = "INSERT INTO add_student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
                    values =(stu_reg_no.get(),stu_nm.get(),stu_dob_entry.get(),age,stu_class.get(),current_date.get(),stu_address.get(),stu_gender.get(),stu_email.get(),stu_con.get())
                    try:
                        con = db.connect(host='localhost', user='root', password='', db='school')
                        cur = con.cursor()
                        cur.execute(query, values)
                        con.commit()
                        messagebox.showinfo("Add Successfully", "Record has been saved successfully", parent=add_stu)
                        clear_btn_student()
                    except db.Error as e:
                        messagebox.showerror("Error", f"An error occurred: {e}", parent=add_stu)
                    finally:
                        cur.close()  # Close the cursor
                        con.close()  # Close the connection
                else:
                    messagebox.showinfo("Error", "Valid phone number required", parent=add_stu)
          
    def clear_btn_student():
        stu_reg_no.set("")
        stu_nm.set("")
        stu_dob.set("")
        stu_age_entry_lbl.config(text="")
        stu_class.set("")
        current_date.set("")
        stu_address.set("")
        stu_gender.set("")
        stu_email.set("")
        stu_con.set("") 

    Label1= t.Label(add_stu, text="Add New Student", font=("Times new roman", 25,"bold"),bg="#31475a",foreground="papayawhip", border=12, relief=t.GROOVE)
    Label1.pack(side=t.TOP,fill=t.X)    
    
    stu_reg_no_label=t.Label(add_stu, text="Registration no.",font=("Times 15 bold"),bg="#7f8b98").place(x=100,y=150)
    stu_reg_no_entry=t.Entry(add_stu,textvariable=stu_reg_no,width=25).place(x=250,y=155)
    
    stu_nm_label=t.Label(add_stu, text="Full Name",font=("Times 15 bold"),bg="#7f8b98").place(x=100,y=200)
    stu_nm_entry=t.Entry(add_stu,textvariable=stu_nm,width=25).place(x=250,y=205)
    
    stu_dob_label=t.Label(add_stu, text="Date Of Birth\n(DD-MM-YY)",font=("Times 13 bold"),bg="#7f8b98").place(x=100,y=250)
    stu_dob_entry = DateEntry(add_stu, width=20, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")
    stu_dob_entry.place(x=250,y=255)
    
    stu_age_label=t.Label(add_stu, text="Age",font=("Times 15 bold"),bg="#7f8b98").place(x=100,y=300)
    stu_age_entry_lbl = t.Label(add_stu, text="",width=20)  
    stu_age_entry_lbl.place(x=250,y=305)
    stu_dob_entry.bind("<FocusOut>", calculate_age)
    
    stu_class_label=t.Label(add_stu,text="Class",font=("Times 15 bold"),bg="#7f8b98").place(x=100,y=350)  
    stu_class_entry=ttk.Combobox(add_stu,values=['1','2','3','4','5','6','7','8','9','10'],font="Robot 10",width=19,state="r",textvariable=stu_class).place(x=250,y=355)
    #Class.set("Select class")
    
    today=date.today()
    d1=today.strftime("%d/%m/%y")
    current_date_label=t.Label(add_stu, text="Date",font=("Times 15 bold"),bg="#7f8b98").place(x=500,y=150)
    current_date_entry=t.Entry(add_stu,textvariable=current_date,width=25).place(x=650,y=155)
    current_date.set(today)
    
    stu_address_label=t.Label(add_stu, text="Address",font=("Times 15 bold"),bg="#7f8b98").place(x=500,y=200)
    stu_address_entry=t.Entry(add_stu,textvariable=stu_address,width=25).place(x=650,y=205,height=50)
    
    stu_gender_label=t.Label(add_stu, text="Gender",font=("Times 15 bold"),bg="#7f8b98").place(x=500,y=250)
    #stu_gender_entry=t.Entry(add_stu,textvariable=stu_gender,width=25).place(x=650,y=205)
    t.Radiobutton(add_stu,text="Male", variable=stu_gender,value="male",font=("Times 13 bold"),padx = 5,bg="#7f8b98").place(x=650,y=255)
    t.Radiobutton(add_stu,text="Female",variable=stu_gender,value="female",font=("Times 13 bold"),padx = 5,bg="#7f8b98").place(x=720,y=255)
    
    stu_email_label= t.Label(add_stu, text="E Mail",font=("Times 15 bold"),bg="#7f8b98").place(x=500,y=300)
    stu_email_entry=t.Entry(add_stu,textvariable=stu_email,width=25).place(x=650,y=305)
    
    stu_con_label=t.Label(add_stu, text="Contact No.",font=("Times 15 bold"),bg="#7f8b98").place(x=500,y=350)
    stu_con_entry=t.Entry(add_stu,textvariable=stu_con,width=25).place(x=650,y=355)
    
    t.Button(add_stu,text="Add",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=add_btn_student).place(x=350,y=450)
    t.Button(add_stu,text="Clear",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=clear_btn_student).place(x=650,y=450)
   
    #t.Frame(add_stu,bd=3,bg="black",width=150,height=150).place(x=1010,y=150)
    #t.Button(add_stu,text="Upload",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=showimage).place(x=1010,y=350)

    t.Button(add_stu,text="Back",width=8,height=1,font="arial 15 bold",bg="#cac9c5",bd=3,relief=t.RAISED,command=add_stu.destroy).place(x=10,y=70)
    add_stu.mainloop()

#---------------------------------------Manage Staff---------------------------------------------
def manage_student():
     global man_stu
     man_stu = t.Toplevel()
     man_stu.title("Manage Student")
     man_stu.configure(background="#7f8b98")
     t.Frame(man_stu,pady=50,padx=100)
     man_stu.geometry("1450x850") 
     
     global stu_reg_no
     global stu_nm
     global stu_dob
     global stu_dob_entry
     global stu_age
     global stu_class
     global current_date
     global stu_address
     global stu_gender
     global stu_email
     global stu_con
     global search_box
     
     stu_reg_no=t.StringVar()
     stu_nm=t.StringVar()
     stu_dob=t.StringVar()
     stu_age=t.StringVar()
     stu_class=t.StringVar()
     current_date=t.StringVar()
     stu_address=t.StringVar()
     stu_gender=t.StringVar()
     stu_email=t.StringVar()
     stu_con=t.StringVar()
     search_box=t.StringVar()
     
     def calculate_age(event):
        global birthdate
        global age

        birthdate = stu_dob_entry.get()
        try:
            birthdate = datetime.strptime(birthdate, "%d-%m-%Y")
            today = datetime.now()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            stu_age.set(str(age))  # Update the stu_age variable
            return age
        except ValueError:
            stu_age_entry.set(text="Invalid date format")
     
     Label1= t.Label(man_stu, text="Manage Student", font=("Times new roman", 25,"bold"),bg="#31475a",foreground="papayawhip", border=12, relief=t.GROOVE)
     Label1.pack(side=t.TOP,fill=t.X)
     
     #Frame 1 
     Frame_Data = t.Frame(man_stu, bd=12, relief=t.GROOVE, bg="#d3d2dd")
     Frame_Data.place(x=10 , y=120, width=350, height=500)
     
     stu_reg_no_label=t.Label(Frame_Data, text="Registration no.",font=("Times 13 bold"),bg="#d3d2dd").place(x=20,y=15)
     stu_reg_no_entry=t.Entry(Frame_Data,textvariable=stu_reg_no,state='readonly').place(x=170,y=19)
     
     stu_nm_label=t.Label(Frame_Data, text="Full Name",font=("Times 13 bold"),bg="#d3d2dd").place(x=20,y=55)
     stu_nm_entry=t.Entry(Frame_Data,textvariable=stu_nm).place(x=170,y=59)
     
     stu_dob_label=t.Label(Frame_Data, text="Date Of Birth",font=("Times 13 bold"),bg="#d3d2dd").place(x=20,y=95)
     stu_dob_entry = DateEntry(Frame_Data, width=20, background="blue", foreground="white", date_pattern="dd-mm-yyyy")
     stu_dob_entry.place(x=170, y=99)

     stu_age_label=t.Label(Frame_Data, text="Age",font=("Times 13 bold"),bg="#d3d2dd").place(x=20,y=135)
     stu_age_entry = t.Label(Frame_Data, text="",textvariable=stu_age, font=("Times 13"), bg="#d3d2dd")
     stu_age_entry.place(x=170, y=139)
     stu_dob_entry.bind("<FocusOut>", calculate_age)
     
     stu_class_label=t.Label(Frame_Data,text="Class",font=("Times 13 bold"),bg="#d3d2dd").place(x=20,y=175)  
     stu_class_entry=ttk.Combobox(Frame_Data,values=['1','2','3','4','5','6','7','8','9','10'],font="Robot 10",width=15,state="r",textvariable=stu_class).place(x=170,y=179)
     
     current_date_label=t.Label(Frame_Data,text="Date",font=("Times 13 bold"),bg="#d3d2dd").place(x=20,y=223)
     current_date_entry=t.Entry(Frame_Data,textvariable=current_date).place(x=170,y=227)
    
     stu_address_label=t.Label(Frame_Data, text="Address",font=("Times 13 bold"),bg="#d3d2dd").place(x=20,y=263)
     stu_address_entry=t.Entry(Frame_Data,textvariable=stu_address).place(x=170,y=267)
    
     stu_gender_label=t.Label(Frame_Data, text="Gender",font=("Times 13 bold"),bg="#d3d2dd").place(x=20,y=303)
     #stu_gender_entry=t.Entry(Frame_Data,textvariable=stu_gender).place(x=170,y=307)
     stu_gender_entry=ttk.Combobox(Frame_Data,values=['Male','Female'],font="Robot 10",width=15,state="r",textvariable=stu_gender).place(x=170,y=307)
     
     stu_email_label=t.Label(Frame_Data, text="E Mail",font=("Times 13 bold"),bg="#d3d2dd").place(x=20,y=343)
     stu_email_entry=t.Entry(Frame_Data,textvariable=stu_email).place(x=170,y=347)
     
     stu_con_label=t.Label(Frame_Data, text="Contact No.",font=("Times 13 bold"),bg="#d3d2dd").place(x=20,y=383)
     stu_con_entry=t.Entry(Frame_Data,textvariable=stu_con).place(x=170,y=387)
     
     def GET_DATA():
         con=db.connect(host='localhost',user='root',password='',database='school')
         cur=con.cursor()
         cur.execute('SELECT * FROM add_student')
         rows=cur.fetchall()
             
         if len(rows)!=0:
             Stu_table.delete(*Stu_table.get_children())
             for row in rows:
                 Stu_table.insert(parent='',index='end',values=row)
             con.commit()
             con.close()

     def update_btn_manage_student():
         con=db.connect(host='localhost',user='root',password='',database='school')
         cur = con.cursor()
         query = "UPDATE add_student SET stu_nm=%s, stu_dob=%s, stu_age=%s, stu_class=%s, stu_address=%s, stu_gender=%s, stu_email=%s, stu_con=%s WHERE stu_reg_no=%s"
         values = (stu_nm.get(), stu_dob.get(), stu_age.get(), stu_class.get(), stu_address.get(), stu_gender.get(), stu_email.get(), stu_con.get(), stu_reg_no.get())
         cur.execute(query, values)
         con.commit()
         GET_DATA()
         con.close()
         #clear_btn_manage_staff_details()
         messagebox.showinfo("Success","Record has been upadated",parent=man_stu)
     def delete_btn_manage_student():
         con=db.connect(host='localhost',user='root',password='',database='school')
         cur=con.cursor()
         try:
             cur.execute('delete from add_student where stu_reg_no=%s '%stu_reg_no.get())
             con.commit()
             con.close()
             GET_DATA()
             messagebox.showinfo('Success','Record has been deleted',parent=man_stu)  
         except Exception as e:
             con.rollback()
             messagebox.showerror("Error", f"Error while deleting record: {e}", parent=man_stu)
         finally:
            con.close()
     
     t.Button(Frame_Data,text="Delete",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=delete_btn_manage_student).place(x=10,y=410)
     t.Button(Frame_Data,text="Update",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=update_btn_manage_student).place(x=170,y=410)
     
     t.Button(man_stu,text="Back",width=8,height=1,font="arial 15 bold",bg="#cac9c5",bd=3,relief=t.RAISED,command=man_stu.destroy).place(x=10,y=70)
     
     #Frame 2
     Frame_Data1 = t.Frame(man_stu, bd=12, relief=t.GROOVE, bg="#d3d2dd")
     Frame_Data1.place(x=380 , y=120, width=850, height=500)
     #Search Frame
     Frame_Search = t.Frame(Frame_Data1, bg="#d3d2dd" , bd=10, relief=t.GROOVE)
     Frame_Search.pack(side=t.TOP, fill=t.X)
     
     Label_Search = t.Label(Frame_Search, text="Registration no:", bg="#d3d2dd", font=("Times new roman", 16))
     Label_Search.grid(row=0, column=0, padx=12, pady=2)
     
     Search_box_entry=t.Entry(Frame_Search,font=("Times new roman", 16),textvariable=search_box)
     Search_box_entry.grid(row=0,column=1,padx=12,pady=2)
     
     def search_record():
        for record in Stu_table.get_children():
            Stu_table.delete(record)
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute("SELECT * FROM add_student where stu_reg_no like %s"%(search_box.get()))
        records=cur.fetchall()
        global count
        count=0
        for record in records:
            if record[0]==search_box.get():
                if count % 2==0:
                    Stu_table.insert(parent="", index='end',value=record)
                else:
                    Stu_table.insert(parent="", index='end',value=record)
                count+=1
                con.commit()  
                break
        else:
            messagebox.showerror("Oops!!","Student ID: {} not found.".format(search_box.get()),parent=man_stu)
        search_box.set("") 
            
     def show_record():
         for record in Stu_table.get_children():
             Stu_table.delete(record)
         con=db.connect(host='localhost',user='root',password='',database='school')
         cur=con.cursor()
         cur.execute('SELECT * FROM add_student')
         rows=cur.fetchall()
         for data in rows:
             Stu_table.insert("", "end", values=(data))
     
     Search_Button = t.Button(Frame_Search,text="Search",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=search_record)
     Search_Button.grid(row=0, column=2, padx=12, pady=2)
                         
     Show_Button = t.Button(Frame_Search,text="View All",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=show_record)
     Show_Button.grid(row=0, column=3, padx=12, pady=2)

     def FOCUS(e): 
        cursor=Stu_table.focus()
        content=Stu_table.item(cursor)
        row=content['values']
        stu_reg_no.set(row[0])
        stu_nm.set(row[1])
        stu_dob.set(row[2])
        stu_age.set(row[3])
        stu_class.set(row[4])
        current_date.set(row[5])
        stu_address.set(row[6])
        stu_gender.set(row[7])
        stu_email.set(row[8])
        stu_con.set(row[9])
        
     #Database Frame
     Frame_Database = t.Frame(Frame_Data1, bg="#d3d2dd", bd=11, relief=t.GROOVE)
     Frame_Database.pack(fill=t.BOTH, expand=True)
     Scroll_X = t.Scrollbar(Frame_Database, orient=t.HORIZONTAL)
     Scroll_Y = t.Scrollbar(Frame_Database, orient=t.VERTICAL)
     Stu_table = ttk.Treeview(Frame_Database, columns=('R. No.', 'Name', 'DOB','Age','Class','Date','Address','Gender','Email','Contact'), yscrollcommand= Scroll_Y.set,xscrollcommand= Scroll_X.set)
      
     Scroll_X.config(command=Stu_table.xview)
     Scroll_X.pack(side=t.BOTTOM, fill=t.X)
     Scroll_Y.config(command=Stu_table.yview)
     Scroll_Y.pack(side=t.RIGHT, fill=t.Y)
      
     Stu_table.heading("R. No.", text="R. No.")
     Stu_table.heading("Name", text="Name")
     Stu_table.heading("DOB", text="DOB")
     Stu_table.heading("Age", text="Age")
     Stu_table.heading("Class", text="Class")
     Stu_table.heading("Date", text="Date")
     Stu_table.heading("Address", text="Address")
     Stu_table.heading("Gender", text="Gender")
     Stu_table.heading("Email", text="Email")
     Stu_table.heading("Contact", text="Contact")
     
     Stu_table['show']='headings'
     Stu_table.column("R. No.",width= 100, anchor="center")
     Stu_table.column("Name",width= 100, anchor="center")
     Stu_table.column("DOB",width= 100, anchor="center")
     Stu_table.column("Age",width= 100, anchor="center")
     Stu_table.column("Class",width= 100, anchor="center")
     Stu_table.column("Date",width= 100, anchor="center")
     Stu_table.column("Address",width= 150, anchor="center")
     Stu_table.column("Gender",width= 150, anchor="center")
     Stu_table.column("Email",width= 150, anchor="center")
     Stu_table.column("Contact",width= 100, anchor="center")
     
     Stu_table.pack(fill=t.BOTH, expand=True)
     Stu_table.bind("<ButtonRelease-1>",FOCUS)
     man_stu.mainloop()