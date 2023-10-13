# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 01:34:51 2023

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
from tkcalendar import DateEntry

def Student_Fees():
    global stu_fees
    stu_fees= t.Toplevel()
    stu_fees.title("Student Fees")
    stu_fees.configure(background="#7f8b98")
    t.Frame(stu_fees,pady=50,padx=100)
    stu_fees.geometry("1450x850")
        
    global stu_reg_no
    global stu_nm
    global stu_class
    global session
    global term
    global tot_fee
    global paid
    global due_amo
    global paid_date
    global fee_status
    global search_box
    
    global stu_reg_no_dropdown
    global stu_nm_entry
    global stu_class_entry
    global session_entry
    global term_entry
    global tot_fee_entry
    global paid_entry
    global due_amo_entry
    global date_entry
    global fee_status_entry
    
    stu_reg_no=t.StringVar()
    stu_nm=t.StringVar()
    session=t.StringVar()
    term=t.StringVar()
    stu_class=t.StringVar()
    tot_fee=t.StringVar()
    paid=t.StringVar()
    due_amo=t.StringVar()
    paid_date=t.StringVar()
    fee_status=t.StringVar() 
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
            cursor.execute("SELECT stu_nm,stu_class FROM add_student WHERE stu_reg_no=%s", (selected_id,))
            row = cursor.fetchall()
            if row:
                selected_name = row[0]
                stu_nm.set(selected_name[0])
                stu_class.set(selected_name[1])
            else:
                stu_nm.set("")
                stu_class.set("")
    def update_due_fees(event=None):
        global due_amount
        total_amount=tot_fee.get()
        paid_amount=paid.get()
        
        # Convert strings to integers or floats
        #tot_amount = int(total_amount)
        #paid_amt = int(paid_amount)
        due_amount = int(total_amount) - int(paid_amount)
        #due_amo_entry.config(text=due_amo, background="white")
        due_amo.set(due_amount)
    def clear_btn_fees_details():
        stu_reg_no.set("")
        stu_nm.set("")
        stu_class.set("")
        session.set("")
        term.set("")
        tot_fee.set("")
        paid.set("")
        due_amo.set("")
        paid_date.set("")
        fee_status.set("")
            
    def add_fees():
        con=db.connect(host='localhost',user='root',password='',db='school')
        cur = con.cursor()
        cur.execute("SELECT * FROM fees where stu_reg_no = %s"%(stu_reg_no.get()))
        records=cur.fetchone()
        if records:
            messagebox.showinfo("Error","ID is alreay exists",parent=stu_fees)
        else:
            insert_data="insert into fees values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(insert_data,(stu_reg_no.get(),stu_nm.get(),stu_class.get(),session.get(),term.get(),tot_fee.get(),paid.get(),due_amo.get(),paid_date.get(),fee_status.get()))
            con.commit()
            messagebox.showinfo("Add Successfully","Record has been saved successfully",parent=stu_fees)
            clear_btn_fees_details() 


    def update_stu_fees():
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur = con.cursor()
        update_qry="UPDATE fees SET stu_nm=%s, stu_class=%s, session=%s, term=%s, tot_fee=%s, paid=%s, due_amo=%s , paid_date=%s, fee_status=%s WHERE stu_reg_no=%s"
        values=(stu_nm.get(),stu_class.get(),session.get(),term.get(),tot_fee.get(),paid.get(),due_amount,date_entry.get(),fee_status.get(),stu_reg_no.get())
        cur.execute(update_qry,values)
        
        con.commit()
        #GET_DATA()
        con.close()
        messagebox.showinfo("Success","Record has been upadated",parent=stu_fees)
        clear_btn_fees_details()
    def search_record():
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute("SELECT * FROM fees where stu_reg_no = %s"%(search_box.get()))
        records=cur.fetchall()
        global count
        count=0
        for record in records:
            if record[0] == search_box.get(): 
                stu_reg_no_dropdown.delete(0, 'end')
                stu_reg_no_dropdown.insert(0, record[0])
           
                stu_nm_entry.delete(0, 'end')
                stu_nm_entry.insert(0, record[1])
           
                stu_class_entry.delete(0, 'end')
                stu_class_entry.set(record[2])
           
                session_entry.delete(0, 'end')
                session_entry.set(record[3])
                
                term_entry.delete(0, 'end')
                term_entry.set(record[4])
           
                tot_fee_entry.delete(0, 'end')
                tot_fee_entry.insert(0, record[5])
           
                paid_entry.delete(0, 'end')
                paid_entry.insert(0, record[6])
                
                due_amo_entry.delete(0, 'end')
                due_amo_entry.insert(0, record[7])
           
                date_entry.delete(0, 'end')
                date_entry.insert(0, record[8])
           
                fee_status_entry.delete(0, 'end')
                fee_status_entry.set(record[9])
                break
        else:
            messagebox.showerror("Oops!!","Student ID: {} not found.".format(search_box.get()),parent=stu_fees)
        search_box.set("") 
    
    Label1= t.Label(stu_fees, text="Student Fees", font=("Times new roman", 25,"bold"),bg="#31475a",foreground="papayawhip", border=12, relief=t.GROOVE)
    Label1.pack(side=t.TOP,fill=t.X) 
    
    Label_Search = t.Label(stu_fees, text="Update of Record No:", bg="#7f8b98", font=("Times new roman", 16))
    Label_Search.place(x=300,y=150)
    Search_box_entry=t.Entry(stu_fees,font=("Times new roman", 16),textvariable=search_box)
    Search_box_entry.place(x=500,y=150)
    Search_Button = t.Button(stu_fees,text="Search",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=search_record)
    Search_Button.place(x=750,y=130)
    
    #Enter Details frame1
    frame =  t.LabelFrame(stu_fees, text="Enter Details", font = ("Times new roman", 22,"bold"), bd=10, relief=t.GROOVE, bg="#d3d2dd")
    frame.place(x=300, y=200, width=800, height=450)
    
    stu_reg_no_label=t.Label(frame, text="Registration no.",font=("Times 15 bold"),bg="#d3d2dd")
    stu_reg_no_label.grid(row=0,column=0,padx=20,pady=5,sticky='W')
    stu_reg_no_dropdown = ttk.Combobox(frame, textvariable=stu_reg_no, values=get_student_ids())
    stu_reg_no_dropdown.bind("<<ComboboxSelected>>", update_student_name)
    stu_reg_no_dropdown.grid(row=0,column=1,padx=20,pady=5,ipadx=15)
    
    stu_nm_label=t.Label(frame, text="Name",font=("Times 15 bold"),bg="#d3d2dd")
    stu_nm_label.grid(row=1,column=0,padx=20,pady=5,sticky='W')
    stu_nm_entry=t.Entry(frame,textvariable=stu_nm,width=25)
    stu_nm_entry.grid(row=1,column=1,padx=20,pady=5,sticky='W')

    stu_class_label=t.Label(frame,text="Class",font=("Times 15 bold"),bg="#d3d2dd")
    stu_class_label.grid(row=2,column=0,padx=20,pady=5,sticky='W')
    stu_class_entry=ttk.Combobox(frame,values=['1','2','3','4','5','6','7','8','9','10'],font="Robot 10",width=15,state="r",textvariable=stu_class)
    stu_class_entry.grid(row=2,column=1,padx=20,pady=5,sticky='W')

    
    session_label=t.Label(frame, text="Session",font=("Times 15 bold"),bg="#d3d2dd")
    session_label.grid(row=3,column=0,padx=20,pady=5,sticky='W')
    session_entry=ttk.Combobox(frame,values=['2020-21','2021-22','2022-23'],font="Robot 10",width=15,state="r",textvariable=session)
    session_entry.grid(row=3,column=1,padx=20,pady=5,sticky='W')

    
    term_label=t.Label(frame, text="Term",font=("Times 15 bold"),bg="#d3d2dd")
    term_label.grid(row=4,column=0,padx=20,pady=5,sticky='W')
    term_entry=ttk.Combobox(frame,values=['1','2'],font="Robot 10",width=15,state="r",textvariable=term)
    term_entry.grid(row=4,column=1,padx=20,pady=5,sticky='W')

        
    tot_fee_label=t.Label(frame, text="Total Amount",font=("Times 15 bold"),bg="#d3d2dd")
    tot_fee_label.grid(row=0,column=2,padx=20,pady=5,sticky='W')
    tot_fee_entry=t.Entry(frame,textvariable=tot_fee,width=25)
    tot_fee_entry.grid(row=0,column=3,padx=20,pady=5,sticky='W')

    
    paid_label=t.Label(frame, text="Paid Fee",font=("Times 15 bold"),bg="#d3d2dd")
    paid_label.grid(row=1,column=2,padx=20,pady=5,sticky='W')
    paid_entry=t.Entry(frame,textvariable=paid,width=25)
    paid_entry.grid(row=1,column=3,padx=20,pady=5,sticky='W')

    
    due_amo_label= t.Label(frame, text="Due Amount",font=("Times 15 bold"),bg="#d3d2dd")
    due_amo_label.grid(row=2,column=2,padx=20,pady=5,sticky='W')
    due_amo_entry=t.Entry(frame,textvariable=due_amo,width=25,state='readonly')
    due_amo_entry.grid(row=2,column=3,padx=20,pady=5,sticky='W')
    paid_entry.bind("<FocusOut>", update_due_fees)

    date_label=t.Label(frame, text="Date Of Paid Fee",font=("Times 15 bold"),bg="#d3d2dd")
    date_label.grid(row=3,column=2,padx=20,pady=5,sticky='W')
    date_entry = DateEntry(frame, width=20, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")
    #date_entry=t.Entry(frame,textvariable=paid_date,width=25)
    date_entry.grid(row=3,column=3,padx=20,pady=5,sticky='W')

    
    fee_status_label=t.Label(frame, text="Fees Status",font=("Times 15 bold"),bg="#d3d2dd")
    fee_status_label.grid(row=4,column=2,padx=20,pady=5,sticky='W')
    fee_status_entry=ttk.Combobox(frame,values=['Paid','Not Paid'],font="Robot 10",width=15,state="r",textvariable=fee_status)
    fee_status_entry.grid(row=4,column=3,padx=20,pady=5,sticky='W')

    
    t.Button(frame,text="Add",width=10,height=1,font="arial 11 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=add_fees).place(x=100,y=250)
    t.Button(frame,text="Update",width=10,height=1,font="arial 11 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=update_stu_fees).place(x=300,y=250)    
    #update_button.grid(row=0,column=4,padx=12,pady=2)
    t.Button(frame,text="Clear",width=10,height=1,font="arial 11 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=clear_btn_fees_details).place(x=500,y=250)

    t.Button(stu_fees,text="Back",width=8,height=1,font="arial 15 bold",bg="#cac9c5",bd=3,relief=t.RAISED,command=stu_fees.destroy).place(x=10,y=70)
    stu_fees.mainloop()
    
#--------------------------------------------------Fees Report-----------------------------------------------------------   
def Student_Fees_Report():
    global fees_report
    fees_report= t.Toplevel()
    fees_report.title("Student Fees Report")
    fees_report.configure(background="#7f8b98")
    t.Frame(fees_report,pady=50,padx=100)
    fees_report.geometry("1450x850")
    
    global stu_reg_no
    global stu_nm
    global stu_class
    global session
    global term
    global tot_fee
    global paid
    global due_amo
    global paid_date
    global fee_status
    global search_box
    
    stu_reg_no=t.StringVar()
    stu_nm=t.StringVar()
    session=t.StringVar()
    term=t.StringVar()
    stu_class=t.StringVar()
    tot_fee=t.StringVar()
    paid=t.StringVar()
    due_amo=t.StringVar()
    paid_date=t.StringVar()
    fee_status=t.StringVar() 
    search_box=t.StringVar()
    def GET_DATA():
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute('SELECT * FROM fees')
        rows=cur.fetchall()
            
        if len(rows)!=0:
            fees_tree.delete(*fees_tree.get_children())
            for row in rows:
                fees_tree.insert(parent='',index='end',values=row)
            con.commit()
            con.close()

    def show_all_record():
        for record in fees_tree.get_children():
            fees_tree.delete(record)
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute('SELECT * FROM fees')
        rows=cur.fetchall()
        for data in rows:
            fees_tree.insert("", "end", values=(data)) 
        
    def search_record():
        for record in fees_tree.get_children():
            fees_tree.delete(record)
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute("SELECT * FROM fees where stu_reg_no like %s"%(search_box.get()))
        records=cur.fetchall()
        global count
        count=0
        for record in records:
            if record[0] == search_box.get(): 
                    if count % 2==0:
                        fees_tree.insert(parent="", index='end',value=record)
                    else:
                        fees_tree.insert(parent="", index='end',value=record)
                    count+=1
                    con.commit()
                    break
        else:
            messagebox.showerror("Oops!!","Student ID: {} not found.".format(search_box.get()),parent=fees_report)
        search_box.set("") 
    def delete_btn_fees_details():      
        decision=messagebox.askquestion("Warning!","Are you sure to delete record",parent=fees_report)
        if decision != "yes":
            return
        else:
            con=db.connect(host='localhost',user='root',password='',database='school')
            cur=con.cursor()
            query = 'DELETE FROM fees WHERE stu_reg_no=%s'
            cur.execute(query, (stu_reg_no.get(),))
            con.commit()
            GET_DATA()
            con.close()
            messagebox.showinfo('Success','Record has been deleted',parent=fees_report) 
        
    Label1= t.Label(fees_report, text="Student Fees Report", font=("Times new roman", 25,"bold"),bg="#31475a",foreground="papayawhip", border=12, relief=t.GROOVE)
    Label1.pack(side=t.TOP,fill=t.X) 
    
    #Frame 2
    Frame_Data1 = t.Frame(fees_report, bd=12, relief=t.GROOVE, bg="#d3d2dd")
    Frame_Data1.place(x=30 , y=120, width=1200, height=500)
    #Search Frame
    Frame_Search = t.Frame(Frame_Data1, bg="#d3d2dd" , bd=10, relief=t.GROOVE)
    Frame_Search.pack(side=t.TOP, fill=t.X)
    
    Label_Search = t.Label(Frame_Search, text="Registration no:", bg="#d3d2dd", font=("Times new roman", 16))
    Label_Search.grid(row=0, column=0, padx=12, pady=2)
    
    Search_box_entry=t.Entry(Frame_Search,font=("Times new roman", 16),textvariable=search_box)
    Search_box_entry.grid(row=0,column=1,padx=12,pady=2)
    
    Search_Button = t.Button(Frame_Search,text="Search",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=search_record)
    Search_Button.grid(row=0, column=2, padx=12, pady=2)
    
    Show_Button = t.Button(Frame_Search,text="View All",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=show_all_record)
    Show_Button.grid(row=0, column=3, padx=12, pady=2)


    delete_button=t.Button(Frame_Search,text="Delete",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=delete_btn_fees_details)
    delete_button.grid(row=0,column=5,padx=12,pady=2)
    
    t.Button(fees_report,text="Back",width=8,height=1,font="arial 15 bold",bg="#cac9c5",bd=3,relief=t.RAISED,command=fees_report.destroy).place(x=10,y=70)
    def FOCUS(e): 
        cursor=fees_tree.focus()
        content=fees_tree.item(cursor)
        row=content['values']
        stu_reg_no.set(row[0])
        stu_nm.set(row[1])
        stu_class.set(row[2])
        term.set(row[3])
        tot_fee.set(row[4])
        paid.set(row[5])
        due_amo.set(row[6])
        paid_date.set(row[7])
        fee_status.set(row[8])

      # Create an instance of Style widget
    style = ttk.Style()
    style.theme_use('clam')
    #Database Frame
    Frame_Database = t.Frame(Frame_Data1, bg="#d3d2dd", bd=11, relief=t.GROOVE)
    Frame_Database.pack(fill=t.BOTH, expand=True)
    Scroll_X = t.Scrollbar(Frame_Database, orient=t.HORIZONTAL)
    Scroll_Y = t.Scrollbar(Frame_Database, orient=t.VERTICAL)
    fees_tree = ttk.Treeview(Frame_Database, columns=('R. No.', 'Name', 'Class','Term','Session','Total Fee','Paid Fee','Balance','Date','Fee Status'), yscrollcommand= Scroll_Y.set,xscrollcommand= Scroll_X.set)
    
    Scroll_X.config(command=fees_tree.xview)
    Scroll_X.pack(side=t.BOTTOM, fill=t.X)
    Scroll_Y.config(command=fees_tree.yview)
    Scroll_Y.pack(side=t.RIGHT, fill=t.Y)
     
    fees_tree.heading("R. No.", text="R. No.")
    fees_tree.heading("Name", text="Name")
    fees_tree.heading("Class", text="Class")
    fees_tree.heading("Session", text="Session")
    fees_tree.heading("Term", text="Term")
    fees_tree.heading("Total Fee", text="Total Fee")
    fees_tree.heading("Paid Fee", text="Paid Fee")
    fees_tree.heading("Balance", text="Balance")
    fees_tree.heading("Date", text="Date")
    fees_tree.heading("Fee Status", text="Fee Status")
        
    fees_tree['show']='headings'
    fees_tree.column("R. No.",width= 100, anchor="center")
    fees_tree.column("Name",width= 100, anchor="center")
    fees_tree.column("Class",width= 100, anchor="center")
    fees_tree.column("Session",width= 100, anchor="center")
    fees_tree.column("Term",width= 100, anchor="center")
    fees_tree.column("Total Fee",width= 100, anchor="center")
    fees_tree.column("Paid Fee",width= 150, anchor="center")
    fees_tree.column("Balance",width= 150, anchor="center")
    fees_tree.column("Date",width= 100, anchor="center")
    fees_tree.column("Fee Status",width= 150, anchor="center")
    
    fees_tree.pack(fill=t.BOTH, expand=True)
    fees_tree.bind("<ButtonRelease-1>",FOCUS)

    fees_report.mainloop()