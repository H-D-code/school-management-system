  
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:06:18 2023

@author: Admin
"""

import tkinter as t 
import MySQLdb as db
#import subprocess#subprocess for run file
import staff as stf#import staff module
import student as stu 
import Attendance as att
import fees as fee
import staff_salary_report as sal_repo
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import Canvas, Scrollbar, Frame, Button
from PIL import Image, ImageTk
import os


#from staff import manage_staff#import only one class in module
background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

root=t.Tk()
root.title("Student management System")
root.config(bg=background)
root.geometry("1450x850")

# Load the background image
image_path = Image.open(r"D:\School_management_system\images\s1.png")
new_width = 1500
new_height = 850
resize_image = image_path.resize((new_width, new_height), Image.LANCZOS)
image_photo = ImageTk.PhotoImage(resize_image)

# Create a Canvas widget to display the background image
canvas = t.Canvas(root, width=new_width, height=new_height)
canvas.pack()

# Display the background image on the canvas
canvas.create_image(0, 0, anchor=t.NW, image=image_photo)

# Title Text
title_text = "Dream International School"
canvas.create_text(650, 200, text=title_text, font=("Copperplate Gothic Bold", 45, "bold"), fill="#000066")

# Logo Image
logo_image = Image.open(r"D:\School_management_system\images\school.png")
logo_image = ImageTk.PhotoImage(logo_image)

# Create a Label to display the logo image
logo_label = t.Label(canvas, image=logo_image)
logo_label.image = logo_image  # To prevent the image from being garbage collected
canvas.create_image(350, 250, anchor=t.NW, image=logo_image)




def exitt():
    root.destroy()
def add_student_window():
    stu.add_student()
def manage_student_window():
    stu.manage_student()
def add_staff_window():
     stf.add_staff()
def add_manage_staff_window():
    stf.add_manage_staff()

def student_fees_window():
    fee.Student_Fees()
def fees_report_window():
    fee.Student_Fees_Report()
def student_attendance_window():
    att.Student_Attendance()
def staff_salary_window():
    sal_repo.Staff_Salary_Repo()

menubar=t.Menu(root)
file=t.Menu(menubar,tearoff=0)  # tearoff/tearon=menu ke bich ki space
menubar.add_cascade(label="Student",menu=file)
file.add_cascade(label="Add Student",comman=add_student_window)
file.add_cascade(label="Manage Student",comman=manage_student_window)

file=t.Menu(menubar,tearoff=0)  # tearoff/tearon=menu ke bich ki space
menubar.add_cascade(label="Staff",menu=file)
file.add_cascade(label="Add Staff",comman=add_staff_window)
file.add_cascade(label="Manage Staff",comman=add_manage_staff_window)

file=t.Menu(menubar,tearoff=0)  # tearoff/tearon=menu ke bich ki space
menubar.add_cascade(label="Attandance",menu=file)
file.add_cascade(label="Student",comman=student_attendance_window)

file=t.Menu(menubar,tearoff=0)  # tearoff/tearon=menu ke bich ki space
menubar.add_cascade(label="Fees",menu=file)
file.add_cascade(label="Student Fess",comman=student_fees_window)
file.add_cascade(label="Student Fess Report",comman=fees_report_window)

file=t.Menu(menubar,tearoff=0)  # tearoff/tearon=menu ke bich ki space
menubar.add_cascade(label="Report",menu=file)
file.add_cascade(label="Staff",comman=staff_salary_window)

root.config(menu=menubar)
root.mainloop()