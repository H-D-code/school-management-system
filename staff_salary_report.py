# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
import shutil
import pdf_format as pf
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from num2words import num2words
import os


import tkinter as t 
import MySQLdb as db
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry


def Staff_Salary_Repo():
    global staff_salary
    staff_salary = t.Toplevel()
    staff_salary.title("Staff Salary Report")
    staff_salary.configure(background="#7f8b98")
    t.Frame(staff_salary,pady=50,padx=100)
    staff_salary.geometry("1450x850")
    
    global stff_id
    global stff_f_nm
    global stff_desig
    global search_box
    global stf_salary
    global da
    global hra
    global ta
    global pf
    global net_pay
    global gross_pay
        
    stff_id=t.StringVar()
    stff_f_nm=t.StringVar()
    stff_desig=t.StringVar()
    search_box=t.StringVar()
    stf_salary=t.StringVar()
    def generate_salary_pdf(staff_id, employee_name, designastion, basic_salary, da, hra, ta, gross_salary, pf, net_salary):
       # Define the data for the salary slip
       pdf_filename = f"Salary_Report_{staff_id}.pdf"
       pdf_folder = "Salary_PDFs"
       if not os.path.exists(pdf_folder):
           os.mkdir(pdf_folder)
       #pdf_filename = os.path.join(pdf_folder, f"Salary_Slip_{staff_id}.pdf")
       company_name = "DREAM INTERNATIONAL SCHOOL"
       #salary_month = "Mar 2023"
       employee_id = staff_id
       employee_name = employee_name
       designation = designastion
       earnings = {
           "Basic Salary": basic_salary,
           "DA(0.25%)": da,
           "HRA(0.15%)":hra,
           "TA(0.075%)":ta,
           "Special Allowances": 0,
       }
       deductions = {
           "EPF": 0,
           "Health Insurance": 0,
           "PF(0.12%)": pf,
           "TDS": 0,  # You can set this based on your needs
       }
       basic_salary = float(stf_salary.get())
       da = float(da)  # Convert da to float
       hra = float(hra)  # Convert hra to float
       ta = float(ta)  # Convert ta to float
       gross_salary = basic_salary + da + hra + ta
       pf=float(pf)
       #gross_salary =sum(earnings.values())
       total_deductions = sum(deductions.values())
       net_pay = gross_salary - total_deductions
       
       # Create a PDF document
       doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
       #doc = SimpleDocTemplate("Salary_Slip.pdf", pagesize=letter)
       
       # Define the content of the salary slip
       elements = []
       # Create a Paragraph for the company name and salary month
       styles = getSampleStyleSheet()
       company_name_style = styles['Title']
       company_name_style.fontSize = 25
       company_name_para = Paragraph(company_name, company_name_style)
       elements.extend([company_name_para])
       
       # Create a table for the salary slip data
       data = [
           ["Staff Salary Slip","","",""],    
           ["Emp. No", "",employee_id],
           ["Name", "",employee_name],
           ["Designation", "",designation],
       ]

       # Earnings table with colspan
       data.extend([["Earnings", "", "Deductions", ""]])
        # Iterate over both earnings and deductions dictionaries
       for (earning, earning_amount), (deduction, deduction_amount) in zip(earnings.items(), deductions.items()):
           data.append([earning, "{:.2f}".format(float(earning_amount)), deduction, "{:.2f}".format(float(deduction_amount))])
    
       # Deductions table
       data.extend([["", "", "", ""]])
       data.extend([["Gross Salary", f"{gross_salary:,.2f}", "Total Deductions", f"{total_deductions:,.2f}"],
                    ["Net Pay", f"{net_pay:,.2f}", int(net_pay), ""]])

       table = Table(data, colWidths=[120, 120, 120, 120])
       table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                  ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                  ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                                  ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                  ('FONTSIZE', (0, 0), (-1, 0), 15),
                                  ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                  ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                  ('BOTTOMPADDING', (0, 0), (-1, 0), 15),
                                  ('BACKGROUND', (0, 1), (-1, 1), colors.lightslategray),
                                  ('BACKGROUND', (0, 2), (-1, 2), colors.lightslategray),
                                  ('BACKGROUND', (0, 3), (-1, 3), colors.lightslategray),
                                  ('BACKGROUND', (0, 4), (-1, 4), colors.rosybrown),
                                  ('BACKGROUND', (0, 10), (-1, 10), colors.rosybrown),
                                  ('BACKGROUND', (0, 11), (-1, 11), colors.gray),
                                  ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                  ('ALIGN', (1, 6), (1, 7), 'CENTER')])),
       # Apply colspan for "Earnings" section
       table_style = [
                      ('SPAN', (0, 0), (-1, 0)),
                      #('SPAN', (0, 0), (3, 0)),
                      #('SPAN', (3, 0), (3, 0)),            
           
                      ('SPAN', (0, 1), (1, 1)),
                      ('SPAN', (2, 1), (3, 1)),
                      
                      ('SPAN', (0, 2), (1, 2)),
                      ('SPAN', (2, 2), (3, 2)),
                      
                      ('SPAN', (0, 3), (1, 3)),
                      ('SPAN', (2, 3), (3, 3)),
                      
                      ('SPAN', (0, 4), (1, 4)),
                      ('SPAN', (2, 4), (3, 4)),
                      ('SPAN', (0, 11), (1, 11)),
                      ('SPAN', (2, 11), (3, 11))
                     ]
       table.setStyle(table_style)
       elements.append(table)
    
       total_net_pay = net_pay 
       # Calculate the amount in words
       amount_in_words = num2words(total_net_pay, lang='en_IN').title()
       # Amount in Words
       amount_in_words = f"{amount_in_words} Rupees"
       amount_in_words_para = Paragraph(f"Amount in Words: {amount_in_words} (Total Net Pay: {total_net_pay:.2f})", styles['Normal'])
       elements.append(amount_in_words_para)
       # Build the PDF document
       doc.build(elements)
       return pdf_filename
             
       
       # Rest of your code remains unchanged
    def save_pdf():
        #basic_salary = float(stf_salary.get())

        try:
            basic_salary = float(stf_salary.get())
            da = 0.25 * basic_salary
            hra = 0.15 * basic_salary
            ta = 0.075 * basic_salary
            pf = 0.12 * basic_salary
            gross_pay = basic_salary + da + hra + ta
            net_pay = gross_pay - pf
            
            #generate_salary_pdf(stff_id.get(), stff_f_nm.get(), stff_desig.get(), stf_salary.get(), da, hra, ta, gross_pay, pf, net_pay)
            
            pdf_filename = generate_salary_pdf(stff_id.get(), stff_f_nm.get(), stff_desig.get(), stf_salary.get(), da, hra, ta, gross_pay, pf, net_pay)
            pdf_folder = os.path.join("D:/School_management_system/Salary_PDFs", stff_id.get())
            if not os.path.exists(pdf_folder):
                os.makedirs(pdf_folder)
            dst = os.path.join(pdf_folder, f"Salary_Slip_{stff_id.get()}.pdf")
            shutil.move(pdf_filename, dst)
            messagebox.showinfo("Success", "PDF Report downloaded successfully!", parent=staff_salary)
        except FileNotFoundError:
            messagebox.showerror("Error", "PDF Report not found!", parent=staff_salary)
            
        #except FileNotFoundError:
        
    def get_staff_ids():
        con=db.connect(host='localhost',user='root',password='',db='school')
        cursor = con.cursor()
        cursor.execute("SELECT stff_id FROM staff_manage")
        ids = [row[0] for row in cursor.fetchall()]
        return ids    
    def update_staff_name(event=None):
        selected_id = stff_id.get()
        if selected_id:
            con=db.connect(host='localhost',user='root',password='',db='school')
            cursor = con.cursor()
            cursor.execute("SELECT stff_f_nm,stff_desig,stff_salary FROM staff_manage WHERE stff_id=%s", (selected_id,))
            row = cursor.fetchall()
            if row:
                selected_name = row[0]
                #selected_sal = row[1]
                stff_f_nm.set(selected_name[0])
                stff_desig.set(selected_name[1])
                stf_salary.set(selected_name[2])
                #select_salary=row[]
            else:
                stff_f_nm.set("")
                stf_salary.set("")

    Label1= t.Label(staff_salary, text="Staff Salary", font=("Times new roman", 25,"bold"),bg="#31475a",foreground="papayawhip", border=12, relief=t.GROOVE)
    Label1.pack(side=t.TOP,fill=t.X)    
    
    #Frame 1
    Frame_Data = t.LabelFrame(staff_salary,text="Enter Details", bd=12, relief=t.GROOVE, bg="#d3d2dd", font = ("Times new roman", 22,"bold"))
    Frame_Data.place(x=10,y=130,width=550,height=500)
    
    #student id and name show
    stf_id_label=t.Label(staff_salary, text="Staff ID ",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=250)
    stf_id_dropdown = ttk.Combobox(staff_salary, textvariable=stff_id, values=get_staff_ids())
    stf_id_dropdown.bind("<<ComboboxSelected>>", update_staff_name)
    stf_id_dropdown.place(x=200,y=250)
    
    stf_nm_label=t.Label(staff_salary, text="Full Name",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=300)
    stf_name_entry = ttk.Entry(staff_salary, textvariable=stff_f_nm, state="readonly")
    stf_name_entry.place(x=200,y=300)
    
    stf_nm_label=t.Label(staff_salary, text="Designation",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=350)
    stf_name_entry = ttk.Entry(staff_salary, textvariable=stff_desig, state="readonly")
    stf_name_entry.place(x=200,y=350)
    
    stf_sal_label=t.Label(staff_salary, text="Basic salary",font=("Times 13 bold"),bg="#d3d2dd").place(x=55,y=400)
    stf_salary_entry = ttk.Entry(staff_salary, textvariable=stf_salary, state="readonly")
    stf_salary_entry.place(x=200,y=400)

    def calculate_gross_salary_btn():
         try:
             basic_salary = float(stf_salary.get())
             da = 0.25 * basic_salary
             hra = 0.15 * basic_salary
             ta = 0.075 * basic_salary
             pf = 0.12 * basic_salary
             gross_pay = basic_salary + da + hra + ta
             net_pay = gross_pay - pf
     
             generate_salary_pdf(stff_id.get(),stff_f_nm.get(),stff_desig.get(),stf_salary.get(), da, hra, ta,gross_pay, pf, net_pay)
         except ValueError:
             pass

         #result_label.config(text="Invalid input")
         txtpaysilp.delete("1.0",t.END)
         txtpaysilp.insert(t.END,"                           DREAM INTERNATIONAL SCHOOL               \n")
         txtpaysilp.insert(t.END,"======================= Salary Slip =======================\n")
         txtpaysilp.insert(t.END,"\t Staff Id :\t\t\t\t"+stff_id.get()+"\t\n\n")
         txtpaysilp.insert(t.END,"\t Name :\t\t\t\t"+stff_f_nm.get()+"\t\n\n")
         txtpaysilp.insert(t.END,"\t Designation :\t\t\t\t"+stff_desig.get()+"\t\n\n")
         txtpaysilp.insert(t.END,"\t Basic Salary :\t\t\t\t"+stf_salary.get()+"\n\n")
         txtpaysilp.insert(t.END,"\t DA(0.25%) :\t\t\t\t"+str(da)+"\n\n")
         txtpaysilp.insert(t.END,"\t HRA(0.15%) :\t\t\t\t"+str(hra)+"\n\n")
         txtpaysilp.insert(t.END,"\t TA(0.075%) :\t\t\t\t"+str(ta)+"\n\n")
         txtpaysilp.insert(t.END,"=====================================================\n")    
         txtpaysilp.insert(t.END,"\t Gross Payment :\t\t\t\t"+str(gross_pay)+"\n\n")
         txtpaysilp.insert(t.END,"\t PF(0.12%) :\t\t\t\t"+str(pf)+"\n\n")
         txtpaysilp.insert(t.END,"=====================================================\n")
         txtpaysilp.insert(t.END,"\t Net Salary Pay  :\t\t\t\t"+str(net_pay)+"\n\n")
        
    t.Button(staff_salary,text="Calculate",width=10,height=1,font="arial 15 bold",bg="#cac9c5",bd=8,relief=t.RAISED,command=calculate_gross_salary_btn).place(x=80,y=450)
    download_button = t.Button(staff_salary, text="Download PDF", width=15, height=1, font="arial 15 bold", bg="#cac9c5", bd=8, relief=t.RAISED, command=save_pdf)
    download_button.place(x=250, y=450)
         
    #Frame 2
    Frame_Data1 = t.Frame(staff_salary, bd=12, relief=t.GROOVE, bg="#d3d2dd")
    Frame_Data1.place(x=580 , y=130, width=660, height=500)

    #Database Frame
    txtpaysilp=t.Text(Frame_Data1,height=22,width=30,wrap=t.WORD, state=t.NORMAL ,font=("Times new roman", 15))
    txtpaysilp.pack(fill=t.X)
    
    t.Button(staff_salary,text="Back",width=8,height=1,font="arial 15 bold",bg="#cac9c5",bd=3,relief=t.RAISED,command=staff_salary.destroy).place(x=10,y=70)
    staff_salary.mainloop()

#Staff_Salary_Repo()