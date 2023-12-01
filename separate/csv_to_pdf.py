import csv
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph, Table
from reportlab.pdfbase.ttfonts import TTFont
import tempfile

QR_CODE_SIZE = 30 # mm (Increase QR code size)

# Read CSV file
def read_csv_data(filename):
    with open(filename, encoding='utf-8') as csvfile:
        # Strip BOM from the CSV file
        csvfile.seek(0)
        first_line = csvfile.readline()
        if first_line.startswith('\ufeff'):
            csvfile.seek(0)

        reader = csv.DictReader(csvfile)
        data = []

        for row in reader:
            converted_row = {}
            for key, value in row.items():
                converted_row[key] = value

            data.append(converted_row)

    return data

# Generate QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=QR_CODE_SIZE,
        border=0
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill_color='black', back_color='white')

# Create PDF page
def create_pdf_page(c):
    # Draw squares
    width, height = c._pagesize
    SQUARE_HEIGHT = height / 4
    SQUARE_WIDTH = width / 3 
    NUM_COLS = 3
    row_count = 0

    for i, row in enumerate(data):
        col = i % NUM_COLS
        x = col * SQUARE_WIDTH  
        y = (i // NUM_COLS) * SQUARE_HEIGHT  

        name = row['\ufeffName']
        customer = row['customer'] if row['customer'] else '?'
        
        paragraphs = []
        line = ""
        for word in name.split(' '):
            test_line = line + ' ' + word if line else word
            if c.stringWidth(test_line) < SQUARE_WIDTH - 20:
                line = test_line 
            else:
                paragraphs.append(line)
                line = word
        
        if line: 
            paragraphs.append(line)

        # Draw paragraphs
        for j, para in enumerate(paragraphs):
            c.drawString(x + 10, y + 10 + j*14, para)

        # Draw customer ###################################################
        c.drawString(x + 10, y + SQUARE_HEIGHT - 20, customer)

        # Draw QR code
        qr_code_image = generate_qr_code(data)
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
          qr_code_image.save(temp_file.name)
          temp_file.close()

        c.drawImage(temp_file.name, x + SQUARE_WIDTH - 50, y + 10, width=QR_CODE_SIZE, height=QR_CODE_SIZE)

        row_count += 1

        # Check if need to start a new page
        if row_count == 12:
            c.showPage()
            row_count = 0

# Generate PDF document
def generate_pdf(filename, data):
    c = canvas.Canvas(filename, pagesize=A4) 
    pdfmetrics.registerFont(TTFont('GolosText', 'GolosText.ttf'))
    
    while data:
        create_pdf_page(c)        
        c.showPage()
        data = data[12:] # display 12 per page
        
    c.save()

# Read CSV data
data = read_csv_data('data.csv')

# Generate PDF document
generate_pdf('output.pdf', data)


