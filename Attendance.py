# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 08:09:16 2023

@author: BAPS
"""

import tkinter as t 
import MySQLdb as db
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

def Student_Attendance():
    global stu_att
    stu_att = t.Toplevel()
    stu_att.title("Student Attendance")
    stu_att.configure(background="#7f8b98")
    t.Frame(stu_att,pady=50,padx=100)
    stu_att.geometry("1450x850")
    
    global stu_reg_no
    global stu_nm
    global start_date_entry
    global end_date_entry
    global present
    global search_box
    
    stu_reg_no=t.StringVar()
    stu_nm=t.StringVar()
    start_date_entry=t.StringVar()
    end_date_entry=t.StringVar()
    present=t.StringVar()
    search_box=t.StringVar()

    def get_student_ids():
        con=db.connect(host='localhost',user='root',password='',db='school')
        cursor = con.cursor()
        cursor.execute("SELECT stu_reg_no FROM add_student")
        ids = [row[0] for row in cursor.fetchall()]
        return ids    
    def update_student_name(event=None):
        selected_id = stu_reg_no.get()
        if selected_id:
            con=db.connect(host='localhost',user='root',password='',db='school')
            cursor = con.cursor()
            cursor.execute("SELECT stu_nm FROM add_student WHERE stu_reg_no=%s", (selected_id,))
            row = cursor.fetchone()
            if row:
                selected_name = row[0]
                stu_nm.set(selected_name)
            else:
                stu_nm.set("")
    def update_date_range_label(event=None):
        global start_date
        global end_date
        global session_day

        start_date = start_date_entry.get_date()
        end_date = end_date_entry.get_date()
        
        if start_date and end_date:
            session_day = (end_date - start_date).days + 1
            #session_day.set(session_day)
            session_days_label.config(text="{} days".format(session_day),background="white")
        else:
            session_days_label.config(text="",background="#d3d2dd")
            #session_day.set("")
    def update_absent_days(event=None):
        global ab_days
        session_day_str=session_day
        present_day_str=present.get()
        
        # Convert strings to integers or floats
        session_days = int(session_day_str)
        present_days = int(present_day_str)
        ab_days = session_days - present_days
        absent_days_label.config(text=ab_days, background="white")
        
    def calculate_percentage(event=None):
        global attendance_percentage
        global total_classes
        global attended_classes
        present_value = present.get()
        if not present_value.isdigit():
            messagebox.showinfo("Error", "Please enter a valid date", parent=stu_att)
            return  # Exit the function if the input is not a valid integer
    
        attended_classes = int(present_value)
        total_classes = int(session_day)
    
        if total_classes <= 0:
            messagebox.showinfo("Error", "Please enter a valid date", parent=stu_att)
        elif session_day < attended_classes:
            messagebox.showinfo("Error", "Present days cannot be greater than total session days", parent=stu_att)
        else:
            attendance_percentage = (attended_classes * 100) // total_classes
            percentage_label.config(text="{} %".format(attendance_percentage), background="white")
            
    #get data        
    def GET_DATA():
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute('SELECT * FROM attendance')
        rows=cur.fetchall()
        if len(rows)!=0:
            Stu_tree.delete(*Stu_tree.get_children())
            for row in rows:
                Stu_tree.insert(parent='',index='end',values=row)
            con.commit()
            con.close()     
   
    #insert data in database
    def add_btn_atdc():
        if stu_reg_no.get()=="" or stu_nm.get() =="" or start_date_entry.get() =="" or end_date_entry.get() =="" or session_day=="" or present.get()=="" or ab_days=="" or percentage_label.cget("text") == "" :
             messagebox.showerror('Error','All Fields required',parent=stu_att) 
        elif total_classes <= 0:
            messagebox.showinfo("Error", "Please enter a valid date", parent=stu_att)
        elif session_day < attended_classes:
            messagebox.showinfo("Error", "Present days cannot be greater than total session days", parent=stu_att)

        else:
            con=db.connect(host='localhost',user='root',password='',db='school')
            cur = con.cursor()
            cur.execute("SELECT * FROM attendance where stu_reg_no = %s"%(stu_reg_no.get()))
            records=cur.fetchone()
            if records:
                messagebox.showinfo("Error","ID is alreay exists",parent=stu_att)
            else:
                insert_data="insert into attendance values(%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(insert_data,(stu_reg_no.get(),stu_nm.get(),start_date,end_date,session_day,present.get(),ab_days,attendance_percentage))
                con.commit()
                messagebox.showinfo("Add Successfully","Record has been saved successfully",parent=stu_att)
                cur.execute('SELECT * FROM attendance')
                rows=cur.fetchall()
                con.close()
                for data in rows:
                    Stu_tree.insert("", "end", values=(data)) 
                GET_DATA()
                clear_btn_atdc_details() 


    def update_atdc():
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur = con.cursor()
        update_qry="UPDATE attendance SET stu_nm=%s, start_date_entry=%s, end_date_entry=%s, session_day=%s, present=%s, absent=%s, per_atdc=%s WHERE stu_reg_no=%s"
        values=(stu_nm.get(),start_date,end_date,session_day,present.get(),ab_days,attendance_percentage,stu_reg_no.get())
        cur.execute(update_qry,values)
        con.commit()
        GET_DATA()
        con.close()
        messagebox.showinfo("Success","Record has been upadated",parent=stu_att)
        clear_btn_atdc_details()
    #delete record
    def delete_atdc():
        decision=messagebox.askquestion("Warning!","Are you sure to delete record",parent=stu_att)
        if decision != "yes":
            return
        else:
            con=db.connect(host='localhost',user='root',password='',database='school')
            cur=con.cursor()
            cur.execute('delete from attendance where stu_reg_no=%s '% stu_reg_no.get())
            con.commit()
            GET_DATA()
            con.close()
            messagebox.showinfo('Success','Record has been deleted',parent=stu_att) 
        clear_btn_atdc_details()
    
    def show_all_record():
        for record in Stu_tree.get_children():
            Stu_tree.delete(record)
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute('SELECT * FROM attendance')
        rows=cur.fetchall()
        for data in rows:
            Stu_tree.insert("", "end", values=(data)) 
        
    def search_record():
        for record in Stu_tree.get_children():
            Stu_tree.delete(record)
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute("SELECT * FROM attendance where stu_reg_no like %s"%(search_box.get()))
        records=cur.fetchall()
        global count
        count=0
        for record in records:
            if record[0] == search_box.get(): 
                    if count % 2==0:
                        Stu_tree.insert(parent="", index='end',value=record)
                    else:
                        Stu_tree.insert(parent="", index='end',value=record)
                    count+=1
                    con.commit()
                    break
        else:
            messagebox.showerror("Oops!!","Student ID: {} not found.".format(search_box.get()),parent=stu_att)
        search_box.set("") 

    def clear_btn_atdc_details():
         stu_reg_no.set("")
         stu_nm.set("")
         present.set("")
         session_days_label.config(text=" ")
         absent_days_label.config(text=" ")
         percentage_label.config(text=" ")
         
    Label1= t.Label(stu_att, text="Student Attendance", font=("Times new roman", 25,"bold"),bg="#31475a",foreground="papayawhip", border=12, relief=t.GROOVE)
    Label1.pack(side=t.TOP,fill=t.X)    
    
    #Frame 1
    Frame_Data = t.Frame(stu_att, bd=12, relief=t.GROOVE, bg="#d3d2dd")
    Frame_Data.place(x=10,y=125,width=550,height=500)
    
    #student id and name show
    stu_reg_no_label=t.Label(stu_att, text="Registration no.",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=150)
    student_id_dropdown = ttk.Combobox(stu_att, textvariable=stu_reg_no, values=get_student_ids())
    student_id_dropdown.bind("<<ComboboxSelected>>", update_student_name)
    student_id_dropdown.place(x=200,y=155)
    
    stu_nm_label=t.Label(stu_att, text="Full Name",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=200)
    student_name_entry = ttk.Entry(stu_att, textvariable=stu_nm, state="readonly")
    student_name_entry.place(x=200,y=205)
    
    #pick calender
    start_date_label=t.Label(stu_att, text="From",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=250)
    start_date_entry = DateEntry(stu_att, width=12, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")
    start_date_entry.place(x=200,y=255)
    
    end_date_label=t.Label(stu_att, text="To",font=("Times 13 bold"),bg="#d3d2dd").place(x=325,y=250)
    end_date_entry = DateEntry(stu_att, width=12, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")
    end_date_entry.place(x=380,y=255)
    
    tot_day_label=t.Label(stu_att, text="Session Days",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=300)
    session_days_label = ttk.Label(stu_att, text="",width=15,font=("Times 13 bold"), background="#d3d2dd")
    #session_day_label = ttk.Entry(stu_att, textvariable=session_day, state="readonly")
    session_days_label.place(x=200,y=305)
    
    # Bind the trace function to the DateEntry widgets
    start_date_entry.bind("<<DateEntrySelected>>", update_date_range_label)
    end_date_entry.bind("<<DateEntrySelected>>", update_date_range_label)
    
    present_label=t.Label(stu_att,text="Number Of Day Present",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=350)
    present_entry=t.Entry(stu_att,textvariable=present)
    present_entry.place(x=250,y=355)
    absent_label=t.Label(stu_att, text="Number Of Day Absent",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=400)
    absent_days_label = ttk.Label(stu_att, text="",width=15,font=("Times 13 bold"), background="#d3d2dd")
    absent_days_label.place(x=250,y=405)
    #absent_entry=t.Entry(stu_att,textvariable=absent).place(x=250,y=455)
    present_entry.bind("<FocusOut>", update_absent_days)
    
    per_label=t.Label(stu_att, text="Percentage of Attendance",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=450)
    percentage_label = ttk.Label(stu_att, text="",width=15,font=("Times 13 bold"), background="#d3d2dd")
    percentage_label.place(x=250,y=450)
    absent_days_label.bind("<FocusOut>", calculate_percentage)
    
    t.Button(stu_att,text="Add",width=10,height=1,font="arial 11 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=add_btn_atdc).place(x=45,y=510)
    t.Button(stu_att,text="Update",width=10,height=1,font="arial 11 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=update_atdc).place(x=165,y=510)
    t.Button(stu_att,text="Delete",width=10,height=1,font="arial 11 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=delete_atdc).place(x=285,y=510)
    t.Button(stu_att,text="Clear",width=10,height=1,font="arial 11 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=clear_btn_atdc_details).place(x=405,y=510)
    t.Button(stu_att,text="Back",width=8,height=1,font="arial 15 bold",bg="#cac9c5",bd=3,relief=t.RAISED,command=stu_att.destroy).place(x=10,y=70)


    def FOCUS(e): 
        cursor=Stu_tree.focus()
        content=Stu_tree.item(cursor)
        row=content['values']
        stu_reg_no.set(row[0])
        stu_nm.set(row[1])
        #start_date_entry.set(row[2])
        #end_date_entry.set(row[3])
        session_days_label.config(text=row[4])
        present.set(row[5])
        absent_days_label.config(text=row[6])
        percentage_label.config(text=row[7])
    #Frame 2
    Frame_Data1 = t.Frame(stu_att, bd=12, relief=t.GROOVE, bg="#d3d2dd")
    Frame_Data1.place(x=580 , y=125, width=660, height=500)

    #Search Frame
    Frame_Search = t.Frame(Frame_Data1, bg="#d3d2dd" , bd=10, relief=t.GROOVE)
    Frame_Search.pack(side=t.TOP, fill=t.X)
    
    Label_Search = t.Label(Frame_Search,text="Registration no:",bg="#d3d2dd",font=("Times new roman", 16))
    Label_Search.grid(row=0, column=0, padx=12, pady=2)
    Search_box_entry=t.Entry(Frame_Search,font=("Times new roman",16),textvariable=search_box,width=10).place(x=150,y=8)    
   
    Search_Button = t.Button(Frame_Search,text="Search",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=search_record)
    Search_Button.grid(row=0, column=2, padx=120, pady=2)
    Show_Button = t.Button(Frame_Search,text="View All",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=show_all_record).place(x=450,y=2)
   

    #Database Frame
    Frame_Database = t.Frame(Frame_Data1, bg="#d3d2dd", bd=11, relief=t.GROOVE)
    Frame_Database.pack(fill=t.BOTH, expand=True)

    Scroll_X = t.Scrollbar(Frame_Database, orient=t.HORIZONTAL)
    Scroll_Y = t.Scrollbar(Frame_Database, orient=t.VERTICAL)
    Stu_tree = ttk.Treeview(Frame_Database, columns=('R. No.', 'Name', 'Start Date','End Date','Session Days','Number Of Day Present','Number Of Day Absent','Percentage'), yscrollcommand= Scroll_Y.set,xscrollcommand= Scroll_X.set)
     
    Scroll_X.config(command=Stu_tree.xview)
    Scroll_X.pack(side=t.BOTTOM, fill=t.X)
    Scroll_Y.config(command=Stu_tree.yview)
    Scroll_Y.pack(side=t.RIGHT, fill=t.Y)
     
    Stu_tree.heading("R. No.", text="R. No.")
    Stu_tree.heading("Name", text="Name")
    Stu_tree.heading("Start Date", text="Start Date")
    Stu_tree.heading("End Date", text="End Date")
    Stu_tree.heading("Session Days", text="Session Days")
    Stu_tree.heading("Number Of Day Present", text="Number Of Day Present")
    Stu_tree.heading("Number Of Day Absent", text="Number Of Day Absent")
    Stu_tree.heading("Percentage", text="Percentage")
        
    Stu_tree['show']='headings'
    Stu_tree.column("R. No.",width= 100, anchor="center")
    Stu_tree.column("Name",width= 100, anchor="center")
    Stu_tree.column("Start Date",width= 100, anchor="center")
    Stu_tree.column("End Date",width= 100, anchor="center")
    Stu_tree.column("Session Days",width= 100, anchor="center")
    Stu_tree.column("Number Of Day Present",width=150, anchor="center")
    Stu_tree.column("Number Of Day Absent",width=150, anchor="center")
    Stu_tree.column("Percentage",width=100, anchor="center")
    
    Stu_tree.pack(fill=t.BOTH, expand=True)
    Stu_tree.bind("<ButtonRelease-1>",FOCUS)
    stu_att.mainloop()
    
    
    
    