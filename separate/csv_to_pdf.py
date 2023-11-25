import csv
import qrcode
from fpdf import FPDF
import os
# import cairosvg

pdf = FPDF() 
pdf.set_auto_page_break(auto=True, margin=0)

with open('data.csv', 'r', encoding="utf-8") as f:
  reader = csv.DictReader(f)
  quadrants_per_page = 12
  pages = {}
  # print(reader.fieldnames)
  y = 10 
  for row in reader:
    name = row['\ufeffName']
    customer = row['заказчик '] or '?'
    stage = row['стадия']
    
    if stage not in pages:
      pages[stage] = FPDF()
      pages[stage].add_page() # Add first page
      pages[stage].set_auto_page_break(auto=True, margin=0)
    
    pdf = pages[stage]
    pdf.set_font('Times', '', 16)  
    pdf.text(10, y, name)
    y += 10 

    if y > 297 - 74.25: 
      pdf.add_page()
      y = 10
    
    pdf.text(10, 10, name)

    
    qr = qrcode.QRCode()
    qr.add_data(str(123)) 

    qr.make_image().save('qrcode.png')
    pdf.image('qrcode.png', 10, 210-10, 60, 60)
      
    pdf.set_xy(140, 210-10) 
    pdf.cell(w=60, h=60, txt=customer, border=1, ln=0)
    os.remove('qrcode.png')
    
import string

for stage in pages:

  # Allow only ascii chars in stage name
  ascii_letters = string.ascii_letters + string.digits
  cleaned_stage = "".join(l for l in stage if l in ascii_letters)

  # Encode string as utf-8 when making filename
  filename = f'{cleaned_stage}.pdf'.encode('utf-8') 

  pages[stage].output(filename)