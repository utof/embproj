import csv
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph, Table
from reportlab.pdfbase.ttfonts import TTFont
import tempfile

# Define constants
GAP = 0  # mm (No gap between squares)
QR_CODE_RATIO = 0.25  # Proportion of QR code size relative to square dimensions

# Read CSV data
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
                key_ascii = key.encode('ascii', 'ignore').decode('utf-8')
                value_ascii = value.encode('ascii', 'ignore').decode('utf-8')
                converted_row[key_ascii] = value_ascii

            data.append(converted_row)

    return data

# Generate QR code
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill_color='black', back_color='white')

# Create PDF page
def create_pdf_page(c, data, filename=None):
    # Get page size
    width, height = c._pagesize

    # Calculate square dimensions based on page size
    square_height = height / 4
    square_width = width / 3

    # Calculate QR code dimensions based on square size
    qr_code_width = square_height * QR_CODE_RATIO
    qr_code_height = qr_code_width

    x = 0
    y = height
    row_count = 0

    for i, row in enumerate(data):
        name = row['Name']
        customer = row['customer'] if row['customer'] else '?'

        # Draw square
        c.rect(x, y - square_height, square_width, square_height, fillColor='gray', strokeColor=None)

        # Wrap text if necessary
        if len(name) > 10:  # Adjust based on desired text length
            name_lines = name.split(' ')
            line_count = 0
            for line in name_lines:
                c.setFont('GolosText', 12)
                c.setFillColorRGB(0, 0, 0)
                c.drawString(x + 10, y - square_height + (line_count * 15), line)
                line_count += 1
        else:
            # Draw name if text length doesn't require wrapping
            c.setFont('GolosText', 12)
            c.setFillColorRGB(0, 0, 0)
            c.drawString(x + 10, y - square_height + 10, name)

        # Draw customer
        c.setFont('GolosText', 10)  # Adjust font size for customer text
        c.setFillColorRGB(0, 0, 0)
        c.drawString(x + 10, y - square_height + 30, customer)

        # Draw QR code
        qr_code_image = generate_qr_code(data)
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        qr_code_image.save(temp_file.name)
        c.drawImage(temp_file.name, x + square_width - qr_code_width - 10, y - square_height + 10, width=qr_code_width, height=qr_code_height)
        temp_file.close()

        # Move to next position
        x += square_width + GAP
        y -= square_height + GAP

        # Check if need to start a new row
        if x + square_width > width:
            x = 0
            y -= square_height + GAP
            row_count += 1

        # Check if need to start a new page
        if y < 0:
            c.showPage()
            y = height
            row_count = 0

        # Save PDF if specified
        if filename:
            c.save()
            c = canvas.Canvas(filename, pagesize=A4)
            pdfmetrics.registerFont(TTFont('GolosText', 'GolosText.ttf'))

# Read CSV data
data = read_csv_data('data.csv')

# Generate PDF document
create_pdf_page('output.pdf', data)
