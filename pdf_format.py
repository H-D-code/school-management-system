from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import MySQLdb as db

def pdf_file():   
    #con=db.connect(host='localhost',user='root',password='',db='school')
    #cursor = con.cursor()
    #cursor.execute("SELECT stff_f_nm,stff_desig,stff_salary FROM staff_manage WHERE stff_id=%s", (selected_id,))
    #row = cursor.fetchall()

    
    
    # Define the data for the salary slip
    company_name = "Your Company Name"
    salary_month = "Mar 2023"
    employee_name = "John Doe"
    employee_department = "IT"
    employee_id = "EMP123"
    designation = "Software Engineer"
    earnings = {
        "Basic Salary": 25200,
        "House Rent Allowances": 9408,
        "Conveyance Allowances": 1493,
        "Medical Allowances": 1167,
        "Special Allowances": 18732,
    }
    deductions = {
        "EPF": 1800,
        "Health Insurance": 500,
        "Professional Tax": 200,
        "TDS": 0,  # You can set this based on your needs
    }
    gross_salary = sum(earnings.values())
    total_deductions = sum(deductions.values())
    net_pay = gross_salary - total_deductions
    
    # Create a PDF document
    doc = SimpleDocTemplate("Salary_Slip.pdf", pagesize=letter)
    
    # Define the content of the salary slip
    elements = []
    
    # Create a Paragraph for the company name and salary month
    styles = getSampleStyleSheet()
    company_name_para = Paragraph(company_name, styles['Title'])
    salary_month_para = Paragraph(f"Salary Slip for {salary_month}", styles['Heading1'])
    
    elements.extend([company_name_para])
    """
    # Create a table for the salary slip data
    data = [
         [salary_month_para],    
         ["Name"],["Emp. No"],
         [employee_name], [employee_id],
         ["Designation", designation],   
    ]"""
     # Create a table for the salary slip data
    data = [
    [salary_month_para],
    ["Emp. Name", " ",employee_name],  # Emp. Name label and data in the second column
    ["Designation","" ,designation],
        ["Emp. No"," ", employee_id],
    ]

    # Earnings table with colspan
    data.extend([["Earnings", "", "Deductions", ""]])
    for earning, amount in earnings.items():
        data.append([earning, f"${amount:,.2f}", "", ""])
    
    # Deductions table
    data.extend([["", "", "", ""]])
    data.extend([["Gross Salary", f"${gross_salary:,.2f}", "Total Deductions", f"${total_deductions:,.2f}"],
                 ["Net Pay", f"${net_pay:,.2f}", "", ""]])
    
    table = Table(data, colWidths=[120, 120, 120, 120])
    table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, 1), colors.beige),
                               ('BACKGROUND', (0, 3), (-1, 3), colors.beige),
                               ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                               ('ALIGN', (1, 6), (1, 7), 'RIGHT')]))
    
    # Apply colspan for "Earnings" section
    table_style = [
                   ('SPAN', (0, 0), (3, 0)),
                   ('SPAN', (3, 0), (3, 0)),            
        
                   ('SPAN', (0, 1), (1, 1)),
                   ('SPAN', (2, 1), (3, 1)),
                   
                   ('SPAN', (0, 2), (1, 2)),
                   ('SPAN', (2, 2), (3, 2)),
                   
                   ('SPAN', (0, 3), (1, 3)),
                   ('SPAN', (2, 3), (3, 3)),
                   
                   ('SPAN', (0, 4), (1, 4)),
                   ('SPAN', (2, 4), (3, 4)),
                   ('SPAN', (0, 12), (1, 12)),
                   ('SPAN', (2, 12), (3, 12))]
    table.setStyle(table_style)
    
    elements.append(table)
    
    # Amount in Words
    amount_in_words = "Fifty Three Thousand Five Hundred"  # Customize this based on your needs
    amount_in_words_para = Paragraph(f"Amount in Words: {amount_in_words}", styles['Normal'])
    elements.append(amount_in_words_para)
    
    # Build the PDF document
    doc.build(elements)
    
    print("Salary slip generated: Salary_Slip.pdf")
#pdf_file()