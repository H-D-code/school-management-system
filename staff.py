
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:03:24 2023

@author: Admin
"""
import tkinter as t 
import MySQLdb as db
import re
from tkcalendar import DateEntry
#import main_file as mf
from tkinter import filedialog
from tkinter import ttk
from datetime import datetime
from datetime import date
from tkinter import *
from tkinter import messagebox
#class staff_add:

def add_staff():
    global add_stff  

    add_stff = t.Toplevel()
    add_stff.grab_set()
    #add_stff=t.Tk()
    add_stff.title("Add Staff")
    add_stff.geometry("1450x850")
    add_stff.configure(background="#7f8b98")
    add_stff.resizable(0, 0)#resizeble winwdow maximize and disable

    #main heading label(ADD NEW STAFF)
    Label_Heading = t.Label(add_stff, text="Add New Staff", font=("Times new roman", 25,"bold"),bg="#31475a",foreground="papayawhip", border=12, relief=t.GROOVE)
    Label_Heading.pack(side=t.TOP, fill=t.X)

    global stff_id
    global stff_f_nm
    global stff_gen
    global stff_dob
    #global stff_age
    global stff_desig
    global stff_adrss
    global stff_phone
    global stff_email
    global stff_dt_join_entry
    global stff_pan
    global stff_aadhar
    global stff_exp
    global stff_edu
    global stff_salary
    
    stff_id=t.StringVar()
    stff_f_nm=t.StringVar()
    stff_gen=t.StringVar(value="male")
    stff_dob=t.StringVar
    #stff_age=t.StringVar()
    stff_desig=t.StringVar()
    stff_adrss=t.StringVar()
    stff_phone=t.StringVar()
    stff_email=t.StringVar()
    stff_dt_join_entry=t.StringVar()
    stff_pan=t.StringVar()
    stff_aadhar=t.StringVar()
    stff_exp=t.StringVar()
    stff_edu=t.StringVar()
    stff_salary=t.StringVar()
    
    def calculate_age(event):
        global birthdate
        global age

        birthdate = stff_dob_entry.get()
        try:
            birthdate = datetime.strptime(birthdate, "%d-%m-%Y")
            today = datetime.now()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            stff_age_entry_lbl.config(text=age)
            return age
        except ValueError:
            stff_age_entry_lbl.config(text="Invalid date format")
    
    def valid_phone(phn):
        if re.match(r"[789]\d{9}$", phn):
            return True
        return False
    def random_emp_id(e):
        current_id=1
        current_id += 1
        stff_id_lbl.config(text=str(current_id))
        #Digits = string.Digitsx
        #strr=''.join(random.choice(Digits) for i in range(stringLength-3))
        #return ('EMP'+strr)
    def add_btn_staff_details():
        age = calculate_age(stff_dob_entry.get())
        date_pattern = r'^\d{2}-\d{2}-\d{4}$' 
        if stff_id.get() == "" or stff_f_nm.get() == "" or stff_adrss.get() == "" or stff_phone.get() == "" or stff_email.get() == "" or stff_pan.get() == "" or stff_aadhar.get() == "":
                messagebox.showerror('Error', 'All Fields are required', parent=add_stff)
        elif not re.match(date_pattern, stff_dob_entry.get()):
              messagebox.showerror("Error","Invaild Date Formate",parent=add_staff)
        elif age is None:
                 messagebox.showerror("Error","Age calculation failed",parent=add_staff)
        else:
            con=db.connect(host='localhost',user='root',password='',db='school')
            cur = con.cursor()
            cur.execute("SELECT * FROM staff_manage where stff_id = %s"%(stff_id.get()))
            records=cur.fetchone()
            if records:
                messagebox.showinfo("Error","ID is alreay exists",parent=add_stff)
            else:
                if valid_phone(stff_phone.get()):
                    query = "INSERT INTO staff_manage (stff_id, stff_f_nm, stff_gen, stff_dob, stff_age, stff_desig, stff_adrss, stff_phone, stff_email, stff_pan, stff_aadhar, stff_exp, stff_edu, stff_salary, stff_dt_join) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    values = (
                        stff_id.get(), stff_f_nm.get(), stff_gen.get(), stff_dob_entry.get(),age, stff_desig.get(),
                        stff_adrss.get(), stff_phone.get(), stff_email.get(), stff_pan.get(), stff_aadhar.get(), stff_exp.get(), stff_edu.get(), stff_salary.get(), stff_dt_join_entry.get()
                    )
                    try:
                        con = db.connect(host='localhost', user='root', password='', db='school')
                        cur = con.cursor()
                        cur.execute(query, values)
                        con.commit()
                        messagebox.showinfo("Add Successfully", "Record has been saved successfully", parent=add_stff)
                        clear_btn_staff_details()
                    except db.Error as e:
                        messagebox.showerror("Error", f"An error occurred: {e}", parent=add_stff)
                    finally:
                        cur.close()  # Close the cursor
                        con.close()  # Close the connection
                else:
                    messagebox.showinfo("Error", "Valid phone number required", parent=add_stff)
                    
        
    def clear_btn_staff_details():
        stff_id.set("")
        stff_f_nm.set("")
        stff_adrss.set("")
        stff_gen.set("")
        stff_age_entry_lbl.config(text="")
        stff_desig.set("")
        stff_phone.set("")
        stff_email.set("")
        #stff_dt_join.set("")
        stff_pan.set("")
        stff_aadhar.set("")
        stff_exp.set("")
        stff_edu.set("")
        stff_salary.set("")
    def Exit():
       # import main_file
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?",parent=add_stff)
        if sure == True:
            add_stff.destroy()
            #main_file.destroy()
            #main_file.deiconify()#for show main file

    #Enter Details frame1
    frame =  t.LabelFrame(add_stff, text="Enter Details", font = ("Times new roman", 22,"bold"), bd=10, relief=t.GROOVE, bg="#d3d2dd")
    frame.place(x=250, y=100, width=750, height=500)
    
    #enter deatis in frame
    stff_id_lable = t.Label(frame, text="Staff ID", bg="#d3d2dd", font=("Times 12 bold"))
    stff_id_lable.grid(row=0,column=0,padx=20,pady=5,sticky='W')
    stff_id_entry = t.Entry(frame, textvariable=stff_id)
    stff_id_entry.grid(row=0,column=1,padx=20,pady=5,ipadx=15)
    
    stff_f_nm_lable = t.Label(frame, text="Full Name", bg="#d3d2dd", font=("Times 12 bold"))
    stff_f_nm_lable.grid(row=1,column=0,padx=20,pady=5,sticky='W')
    stff_f_nm_entry = t.Entry(frame, textvariable=stff_f_nm)
    stff_f_nm_entry.grid(row=1,column=1,padx=20,pady=5,ipadx=15)
    
    stff_gen_lable = t.Label(frame, text="Gender", bg="#d3d2dd", font=("Times 12 bold"))
    stff_gen_lable.grid(row=2,column=0,padx=20,pady=5,sticky='W')
    stff_gen_entry=t.Radiobutton(frame,text="Male", variable = stff_gen,value="male",font=("Times 11 bold"),bg="#d3d2dd")
    stff_gen_entry.grid(row=2,column=1,padx=20,pady=5,sticky='W')    
    stff_gen_entry=t.Radiobutton(frame,text="Female",variable = stff_gen,value="female",font=("Times 11 bold"),bg="#d3d2dd")
    stff_gen_entry.grid(row=2,column=1,padx=20,pady=5,sticky='E')  
    
    stff_dob_label=t.Label(frame, text="DOB",font=("Times 12 bold"),bg="#d3d2dd")
    stff_dob_label.grid(row=3,column=0,padx=20,pady=5,sticky='W')   
    stff_dob_entry = DateEntry(frame, width=18, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")
    stff_dob_entry.grid(row=3,column=1,padx=20,pady=5,ipadx=15)
    
    stff_age_lable = t.Label(frame, text="Age", bg="#d3d2dd", font=("Times 12 bold"))
    stff_age_lable.grid(row=4,column=0,padx=20,pady=5,sticky='W')
    stff_age_entry_lbl = t.Label(frame, text="",width=18)  
    stff_age_entry_lbl.grid(row=4,column=1,padx=20,pady=5,ipadx=15)
    stff_dob_entry.bind("<FocusOut>", calculate_age)

    stff_desig_lable = t.Label(frame, text="Designation", bg="#d3d2dd", font=("Times 12 bold"))
    stff_desig_lable.grid(row=5,column=0,padx=20,pady=5,sticky='W')
    stff_desig_entry=ttk.Combobox(frame,values=['Teacher','Lacturer','Office Staff','Super visor',],font="Robot 10",width=15,state="r",textvariable=stff_desig)
    stff_desig_entry.grid(row=5,column=1,padx=20,pady=5,ipadx=15)  
    
    stff_adrss_lable = t.Label(frame, text="Address", bg="#d3d2dd", font=("Times 12 bold"))
    stff_adrss_lable.grid(row=6,column=0,padx=20,pady=5,sticky='W')
    stff_adrss_entry = t.Entry(frame, textvariable=stff_adrss)
    stff_adrss_entry.grid(row=6,column=1,padx=20,pady=5,ipadx=15,ipady=20)  
    
    stff_phone_lable = t.Label(frame, text="Phone No.", bg="#d3d2dd", font=("Times 12 bold"))
    stff_phone_lable.grid(row=7,column=0,padx=20,pady=5,sticky='W')
    stff_phone_entry = t.Entry(frame, textvariable=stff_phone)
    stff_phone_entry.grid(row=7,column=1,padx=20,pady=5,ipadx=15)  
    
    stff_email_lable = t.Label(frame, text="Email", bg="#d3d2dd", font=("Times 12 bold"))
    stff_email_lable.grid(row=8,column=0,padx=20,pady=5,sticky='W')
    stff_email_entry = t.Entry(frame, textvariable=stff_email)
    stff_email_entry.grid(row=8,column=1,padx=20,pady=5,ipadx=15)   

    
    stff_pan_lable = t.Label(frame, text="Pan No.", bg="#d3d2dd", font=("Times 12 bold"))
    stff_pan_lable.grid(row=0,column=2,padx=20,pady=5,sticky='W')
    stff_pan_entry = t.Entry(frame, textvariable=stff_pan)
    stff_pan_entry.grid(row=0,column=3,padx=20,pady=5,ipadx=15)  
    
    stff_aadhar_lable = t.Label(frame, text="Aadhar No.", bg="#d3d2dd", font=("Times 12 bold"))
    stff_aadhar_lable.grid(row=1,column=2,padx=20,pady=5,sticky='W')
    stff_aadhar_entry = t.Entry(frame, textvariable=stff_aadhar)
    stff_aadhar_entry.grid(row=1,column=3,padx=20,pady=5,ipadx=15)  
    
    stff_exp_lable = t.Label(frame, text="Work of Experience", bg="#d3d2dd", font=("Times 12 bold"))
    stff_exp_lable.grid(row=2,column=2,padx=20,pady=5,sticky='W')
    stff_exp_entry = t.Entry(frame, textvariable=stff_exp)
    stff_exp_entry.grid(row=2,column=3,padx=20,pady=5,ipadx=15)  
    
    stff_edu_lable = t.Label(frame, text="Highst Education", bg="#d3d2dd", font=("Times 12 bold"))
    stff_edu_lable.grid(row=3,column=2,padx=20,pady=5,sticky='W')
    stff_edu_entry = t.Entry(frame, textvariable=stff_edu)
    stff_edu_entry.grid(row=3,column=3,padx=20,pady=5,ipadx=15)  
    
    stff_salary_lbl=t.Label(frame, text="Basic Salary", bg="#d3d2dd", font=("Times 12 bold"))
    stff_salary_lbl.grid(row=4,column=2,padx=20,pady=5,sticky='W')
    stff_salary_entry=t.Entry(frame,textvariable=stff_salary)
    stff_salary_entry.grid(row=4,column=3,padx=20,pady=5,ipadx=15)
    
    stff_dt_join_lable = t.Label(frame, text="Date Of Join", bg="#d3d2dd", font=("Times 12 bold"))
    stff_dt_join_lable.grid(row=5,column=2,padx=20,pady=5,sticky='W')
    stff_dt_join_entry = DateEntry(frame, width=18, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")
    #stff_dt_join_entry = t.Entry(frame, textvariable=stff_dt_join)
    stff_dt_join_entry.grid(row=5,column=3,padx=20,pady=5,ipadx=15) 
    
    
    #frame of button
    #Frame_Btn = t.Frame(frame, bg="pink3", bd=7, relief=t.SUNKEN )
    #Frame_Btn.place(x=80, y=300, width=470, height=90)
    btn_add=t.Button(frame, text="Add",command = add_btn_staff_details,width=10,height=1,activebackground="#314063",activeforeground="#ffedc7",font="Times 15 bold",bg="#cac9c5",foreground="black",relief=t.RAISED,bd=8)
    btn_add.grid(row=9,column=0,pady=30,columnspan=2)
    btn_clear=t.Button(frame, text="Clear",command = clear_btn_staff_details,width=10,height=1,activebackground="#314063",activeforeground="#ffedc7",font="Times 15 bold",bg="#cac9c5",foreground="black",relief=t.RAISED,bd=8)
    btn_clear.grid(row=9,column=2,pady=30,sticky='W')
    btn_close=t.Button(frame, text="Close",command = Exit,width=10,height=1,activebackground="#314063",activeforeground="#ffedc7",font="Times 15 bold",bg="#cac9c5",foreground="black",relief=t.RAISED,bd=8)
    btn_close.grid(row=9,column=3,pady=30)
    add_stff.mainloop()
        

#.............................................Manage staff details............................................

#class manage_staff:
def add_manage_staff():
    global add_manage_sttf

    add_manage_sttf = t.Toplevel()
    add_manage_sttf.title("Manage Staff")
    add_manage_sttf.geometry("1450x850")
    add_manage_sttf.configure(background="#7f8b98")
    add_manage_sttf.resizable(0, 0)#resizeble window maximize and disable

    #main heading label(MANAGE STAFF)
    Label_Heading = t.Label(add_manage_sttf, text="Manage Staff", font=("Times new roman", 25,"bold"),bg="#31475a",foreground="papayawhip", border=12, relief=t.GROOVE)
    Label_Heading.pack(side=t.TOP, fill=t.X)
    
    #Enter Details frame1
    frame =  t.LabelFrame(add_manage_sttf, text="Enter Details", font = ("Times new roman", 22,"bold"), bd=10, relief=t.GROOVE, bg="#d3d2dd")
    frame.place(x=20, y=80, width=450, height=650)
    #frame.pack(side="left")
    #search and treeview frame2
    Frame_Data = t.Frame(add_manage_sttf, bd=12, relief=t.GROOVE, bg="#d3d2dd")
    Frame_Data.place(x=500 , y=80, width=750, height=625)
   
    #Frame_Data.pack(side="right")
    
    global stff_id
    global stff_f_nm
    global stff_gen
    global stff_dob_entry
    global stff_age
    global stff_desig
    global stff_adrss
    global stff_phone
    global stff_email
    global stff_dt_join
    global stff_pan
    global stff_aadhar
    global stff_exp
    global stff_edu
    global stff_salary
    global m_search_box
  
    stff_id=t.StringVar()
    stff_f_nm=t.StringVar()
    stff_gen=t.StringVar()
    stff_dob_entry=t.StringVar()
    stff_age=t.StringVar()
    stff_desig=t.StringVar()
    stff_adrss=t.StringVar()
    stff_phone=t.StringVar()
    stff_email=t.StringVar()
    stff_dt_join=t.StringVar()
    stff_pan=t.StringVar()
    stff_aadhar=t.StringVar()
    stff_exp=t.StringVar()
    stff_edu=t.StringVar()
    stff_salary=t.StringVar()
    m_search_box=t.StringVar()
    
    def calculate_age(event):
        global birthdate
        global age

        birthdate = stff_dob_entry.get()
        try:
            birthdate = datetime.strptime(birthdate, "%d-%m-%Y")
            today = datetime.now()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            stff_age.set(str(age))  # Update the stu_age variable
            return age
        except ValueError:
            stff_age_entry.config(text="Invalid date format")

    stff_id_lbl=t.Label(frame, text="Staff ID", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_id_lbl.grid(row=1,column=0,padx=20,pady=5,sticky='W')
    stff_id_entry=t.Entry(frame,textvariable=stff_id,state='readonly')
    stff_id_entry.grid(row=1,column=1,padx=20,pady=5)
    
    stff_f_nm_lbl=t.Label(frame, text="Name", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_f_nm_lbl.grid(row=2,column=0,padx=20,pady=5,sticky='W')
    stff_f_nm_entry=t.Entry(frame,textvariable=stff_f_nm)
    stff_f_nm_entry.grid(row=2,column=1,padx=20,pady=5)
    
    stff_gen_lable = t.Label(frame, text="Gender", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_gen_lable.grid(row=3,column=0,padx=20,pady=5,sticky='W')
    stff_gen_entry = t.Entry(frame, textvariable=stff_gen)
    stff_gen_entry.grid(row=3,column=1,padx=20,pady=5)    
    
    stff_dob_lable = t.Label(frame, text="DOB", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_dob_lable.grid(row=4,column=0,padx=20,pady=5,sticky='W')
    
    stff_dob_entry = DateEntry(frame, width=18, background="blue", foreground="white", date_pattern="dd-mm-yyyy")    
    stff_dob_entry.grid(row=4,column=1,padx=20,pady=5)
    
    stff_age_lable = t.Label(frame, text="Age", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_age_lable.grid(row=5,column=0,padx=20,pady=5,sticky='W')
    
    stff_age_entry = t.Label(frame, text="",textvariable=stff_age, font=("Times 13"), bg="#d3d2dd")
    stff_age_entry.grid(row=5,column=1,padx=20,pady=5)
    stff_dob_entry.bind("<FocusOut>", calculate_age)
    
    stff_desig_lable = t.Label(frame, text="Designation", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_desig_lable.grid(row=6,column=0,padx=20,pady=5,sticky='W')
    stff_desig_entry = t.Entry(frame, textvariable=stff_desig)
    stff_desig_entry.grid(row=6,column=1,padx=20,pady=5)  
    
    stff_adrss_lable = t.Label(frame, text="Address", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_adrss_lable.grid(row=7,column=0,padx=20,pady=5,sticky='W')
    stff_adrss_entry = t.Entry(frame, textvariable=stff_adrss)
    stff_adrss_entry.grid(row=7,column=1,padx=20,pady=5)  
    
    stff_phone_lable = t.Label(frame, text="Phone No.", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_phone_lable.grid(row=8,column=0,padx=20,pady=5,sticky='W')
    stff_phone_entry = t.Entry(frame, textvariable=stff_phone)
    stff_phone_entry.grid(row=8,column=1,padx=20,pady=5)  
    
    stff_email_lable = t.Label(frame, text="Email", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_email_lable.grid(row=9,column=0,padx=20,pady=5,sticky='W')
    stff_email_entry = t.Entry(frame, textvariable=stff_email)
    stff_email_entry.grid(row=9,column=1,padx=20,pady=5)   
    
    stff_pan_lable = t.Label(frame, text="Pan No.", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_pan_lable.grid(row=10,column=0,padx=20,pady=5,sticky='W')
    stff_pan_entry = t.Entry(frame, textvariable=stff_pan)
    stff_pan_entry.grid(row=10,column=1,padx=20,pady=5)  
    
    stff_aadhar_lable = t.Label(frame, text="Aadhar No.", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_aadhar_lable.grid(row=11,column=0,padx=20,pady=5,sticky='W')
    stff_aadhar_entry = t.Entry(frame, textvariable=stff_aadhar)
    stff_aadhar_entry.grid(row=11,column=1,padx=20,pady=5)  
    
    stff_exp_lable = t.Label(frame, text="Work of Experience", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_exp_lable.grid(row=12,column=0,padx=20,pady=5,sticky='W')
    stff_exp_entry = t.Entry(frame, textvariable=stff_exp)
    stff_exp_entry.grid(row=12,column=1,padx=20,pady=5)  
    
    stff_edu_lable = t.Label(frame, text="Education", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_edu_lable.grid(row=13,column=0,padx=20,pady=5,sticky='W')
    stff_edu_entry = t.Entry(frame, textvariable=stff_edu)
    stff_edu_entry.grid(row=13,column=1,padx=20,pady=5)  
    
    stff_salary_lbl=t.Label(frame, text="Salary", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_salary_lbl.grid(row=14,column=0,padx=20,pady=5,sticky='W')
    stff_salary_entry=t.Entry(frame,textvariable=stff_salary)
    stff_salary_entry.grid(row=14,column=1,padx=20,pady=5)
       
    stff_dt_join_lable = t.Label(frame, text="Date Of Join", font=("Times new roman", 11,"bold"), bg="#d3d2dd")
    stff_dt_join_lable.grid(row=15,column=0,padx=20,pady=5,sticky='W')
    stff_dt_join_entry = t.Entry(frame, textvariable=stff_dt_join)
    stff_dt_join_entry.grid(row=15,column=1,padx=20,pady=5) 
    def GET_DATA():
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute('SELECT * FROM staff_manage')
        rows=cur.fetchall()
            
        if len(rows)!=0:
            Staff_table.delete(*Staff_table.get_children())
            for row in rows:
                Staff_table.insert(parent='',index='end',values=row)
            con.commit()
            con.close()

        
    def edit_btn_manage_staff_details():
        con = db.connect(host='localhost', user='root', password='', database='school')
        cur = con.cursor()
        # Update the selected record
        query=("""
            UPDATE staff_manage
            SET stff_f_nm=%s, stff_gen=%s, stff_dob=%s, stff_age=%s, stff_desig=%s, stff_adrss=%s,
                stff_phone=%s, stff_email=%s, stff_pan=%s, stff_aadhar=%s, stff_exp=%s, stff_edu=%s,
                stff_salary=%s, stff_dt_join=%s
            WHERE stff_id=%s
        """) 
        values=(stff_f_nm.get(), stff_gen.get(), stff_dob_entry.get(), stff_age.get(), stff_desig.get(),
              stff_adrss.get(), stff_phone.get(), stff_email.get(), stff_pan.get(), stff_aadhar.get(),
              stff_exp.get(), stff_edu.get(), stff_salary.get(), stff_dt_join.get(), stff_id.get())
        cur.execute(query, values)
        con.commit()
        con.close()
        GET_DATA()
        messagebox.showinfo("Success", "Record has been updated.",parent=add_manage_sttf)
        clear_btn_manage_staff_details()

    def delete_btn_manage_staff_details():      
        decision=messagebox.askquestion("Warning!","Are you sure to delete record",parent=add_manage_sttf)
        if decision != "yes":
            return
        else:
            con=db.connect(host='localhost',user='root',password='',database='school')
            cur=con.cursor()
            cur.execute('delete from staff_manage where stff_id=%s '% stff_id.get())
            con.commit()
            GET_DATA()
            con.close()
            messagebox.showinfo('Success','Record has been deleted',parent=add_manage_sttf) 
            clear_btn_manage_staff_details()
    def clear_btn_manage_staff_details():
         stff_id.set("")
         stff_f_nm.set("")
         stff_gen.set("")
         stff_dob_entry.set_date(None)
         stff_age.set("")
         stff_desig.set("")
         stff_adrss.set("")
         stff_phone.set("")
         stff_email.set("")
         stff_dt_join.set("")
         stff_pan.set("")
         stff_aadhar.set("")
         stff_exp.set("")
         stff_edu.set("")
         stff_salary.set("")


    #Frame_Btn = t.Frame(frame, bg="#d3d2dd", bd=7, relief=t.SUNKEN )
    #Frame_Btn.place(x=15, y=480, width=340, height=60)

    btn_edit=t.Button(frame, text="Update",command = edit_btn_manage_staff_details, bg="#cac9c5",relief=t.RAISED,bd=8, font="Times 15 bold", width=10)
    btn_edit.grid(row=16,column=0,pady=2,padx=10)
    btn_delete=t.Button(frame, text="Delete",command = delete_btn_manage_staff_details, bg="#cac9c5",relief=t.RAISED,bd=8, font="Times 15 bold", width=10)
    btn_delete.grid(row=16,column=1,pady=2,padx=10)
    btn_clear=t.Button(frame, text="Clear",command = clear_btn_manage_staff_details, bg="#cac9c5", relief=t.RAISED,bd=8, font="Times 15 bold", width=10)
    btn_clear.grid(row=17,column=0,pady=2,padx=10,)
    btn_exit=t.Button(frame, text="Exit",command =add_manage_sttf.destroy , bg="#cac9c5", relief=t.RAISED,bd=8, font="Times 15 bold", width=10)
    btn_exit.grid(row=17,column=1,pady=2,padx=10)

    # Search Frame3(frame_data main frame1)   
    Frame_Search = t.Frame(Frame_Data, bg="#d3d2dd" , bd=10, relief=t.GROOVE)
    Frame_Search.pack(side=t.TOP, fill=t.X)
    Frame_Search.pack(fill=t.BOTH)


    def show_all_record():
        for record in Staff_table.get_children():
            Staff_table.delete(record)
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute('SELECT * FROM staff_manage')
        rows=cur.fetchall()
        for data in rows:
            Staff_table.insert("", "end", values=(data)) 
        
    def search_record():
        for record in Staff_table.get_children():
            Staff_table.delete(record)
        con=db.connect(host='localhost',user='root',password='',database='school')
        cur=con.cursor()
        cur.execute("SELECT * FROM staff_manage where stff_id like %s"%(m_search_box.get()))
        records=cur.fetchall()

        global count
        count=0
        for record in records:
            if record[0] == m_search_box.get(): 
                    if count % 2==0:
                        Staff_table.insert(parent="", index='end',value=record)
                    else:
                        Staff_table.insert(parent="", index='end',value=record)
                    count+=1
                    con.commit()
                    break
        else:
            messagebox.showerror("Oops!!","Staff ID: {} not found.".format(m_search_box.get()),parent=add_manage_sttf)
        m_search_box.set("") 
        
    Label_Search = t.Label(Frame_Search, text="Search By ID :", bg="#d3d2dd", font=("Times new roman", 14))
    Label_Search.grid(row=0, column=0, padx=12, pady=2)
     
    Search_Box_entry = t.Entry(Frame_Search, font=("Times new roman", 16),textvariable=m_search_box)
    Search_Box_entry.grid(row=0, column=1, padx=12, pady=2)
         
    Search_Button = t.Button(Frame_Search, bg="#cac9c5", text="Search",relief=t.RAISED,bd=8, font="Times 15 bold", width=10,command=search_record)
    Search_Button.grid(row=0, column=2, padx=12, pady=2)
     
    Show_Button = t.Button(Frame_Search, bg="#cac9c5", text="View All",relief=t.RAISED,bd=8, font="Times 15 bold", width=10,command=show_all_record)
    Show_Button.grid(row=0, column=3, padx=12, pady=2)
    def FOCUS(e): 
        cursor=Staff_table.focus()
        content=Staff_table.item(cursor)
        row=content['values']
        stff_id.set(row[0])
        stff_f_nm.set(row[1])
        stff_gen.set(row[2])
        stff_dob_entry.set_date(row[3])
        stff_age.set(row[4])
        stff_desig.set(row[5])
        stff_adrss.set(row[6])
        stff_phone.set(row[7])
        stff_email.set(row[8])
        stff_pan.set(row[9])
        stff_aadhar.set(row[10])
        stff_exp.set(row[11])
        stff_edu.set(row[12])
        stff_salary.set(row[13])
        stff_dt_join.set(row[14])

    # Database Frame4 TREEVIEW(frame_data main frame2)
    Frame_Database = t.Frame(Frame_Data, bg="#d3d2dd", bd=11, relief=t.GROOVE)
    Frame_Database.pack(fill=t.BOTH, expand=True)
    Scroll_X = t.Scrollbar(Frame_Database, orient=t.HORIZONTAL)
    Scroll_Y = t.Scrollbar(Frame_Database, orient=t.VERTICAL)
    Staff_table = ttk.Treeview(Frame_Database, columns=('Staff ID', 'Name', 'Gender','DOB','Age','Designation','Address','Phone No','Email','Pan No.','Aadhar No.','Work of Experience','Education','Salary','Date Of Join'), yscrollcommand= Scroll_Y.set,xscrollcommand= Scroll_X.set)
    Scroll_X.config(command=Staff_table.xview)
    Scroll_X.pack(side=t.BOTTOM, fill=t.X)
    Scroll_Y.config(command=Staff_table.yview)
    Scroll_Y.pack(side=t.RIGHT, fill=t.Y)
     
    Staff_table.heading("Staff ID", text="Staff ID")
    Staff_table.heading("Name", text="Name")
    Staff_table.heading("Gender", text="Gender")
    Staff_table.heading("DOB", text="DOB")
    Staff_table.heading("Age", text="Age")
    Staff_table.heading("Designation", text="Designation")
    Staff_table.heading("Address", text="Address")
    Staff_table.heading("Phone No", text="Phone No")
    Staff_table.heading("Email", text="Email")
    Staff_table.heading("Pan No.", text="Pan No.")
    Staff_table.heading("Aadhar No.", text="Aadhar No.")
    Staff_table.heading("Work of Experience", text="Work of Experience")
    Staff_table.heading("Education", text="Education")
    Staff_table.heading("Salary", text="Salary")
    Staff_table.heading("Date Of Join", text="Date Of Join")

    Staff_table['show']='headings'
    Staff_table.column("Staff ID",width= 100, anchor="center")
    Staff_table.column("Name",width= 100, anchor="center")
    Staff_table.column("Gender",width= 100, anchor="center")
    Staff_table.column("DOB",width= 100, anchor="center")
    Staff_table.column("Age",width= 100, anchor="center")
    Staff_table.column("Designation",width= 100, anchor="center")
    Staff_table.column("Address",width= 100, anchor="center")
    Staff_table.column("Phone No",width= 100, anchor="center")
    Staff_table.column("Email",width= 100, anchor="center")
    Staff_table.column("Pan No.",width= 100, anchor="center")
    Staff_table.column("Aadhar No.",width= 100, anchor="center")
    Staff_table.column("Work of Experience",width= 100, anchor="center")
    Staff_table.column("Education",width= 100, anchor="center")
    Staff_table.column("Salary",width= 100, anchor="center")
    Staff_table.column("Date Of Join",width= 100, anchor="center")

    Staff_table.pack(fill=t.BOTH, expand=True)
    Staff_table.bind("<ButtonRelease-1>",FOCUS)
    add_manage_sttf.mainloop()
 







