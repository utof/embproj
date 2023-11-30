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
SQUARE_WIDTH = 70 # mm
SQUARE_HEIGHT = 74.25 # mm
GAP = 0 # mm (No gap between squares)
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
                key_ascii = key.encode('ascii', 'ignore').decode('utf-8')
                value_ascii = value.encode('ascii', 'ignore').decode('utf-8')
                converted_row[key_ascii] = value_ascii

            data.append(converted_row)

    return data

# Group data by stage
def group_data_by_stage(data):
    grouped_data = {}
    for row in data:
        stage = row['stage']
        if stage not in grouped_data:
            grouped_data[stage] = []
        grouped_data[stage].append(row)
    return grouped_data

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
def create_pdf_page(c, stage_data, one_page=False):
    # Draw squares
    row_count = 0
    for i, row in enumerate(stage_data):
        name = row['Name']
        customer = row['customer'] if row['customer'] else '?'

        x = i % 3 * SQUARE_WIDTH
        y = row_count * SQUARE_HEIGHT

        c.rect(x, y, SQUARE_WIDTH, SQUARE_HEIGHT) # Remove outline/border

        # Draw name
        c.setFont('GolosText', 12)  # Use Cyrillic-compatible font
        c.setFillColorRGB(0, 0, 0)
        c.drawString(x + 10, y + 10, name)

        # Draw customer
        c.drawString(x + 10, y + SQUARE_HEIGHT - 20, customer)

        # Draw QR code
        qr_code_image = generate_qr_code(data)
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
          qr_code_image.save(temp_file.name)
          temp_file.close()

        c.drawImage(temp_file.name, x + SQUARE_WIDTH - 50, y + 10, width=QR_CODE_SIZE, height=QR_CODE_SIZE)

        row_count += 1

        # Check if need to start a new page
        if one_page and row_count == 12:
            c.showPage()
            row_count = 0

# Generate PDF document
def generate_pdf(filename, data, one_page=False):
    c = canvas.Canvas(filename, pagesize=A4)
    pdfmetrics.registerFont(TTFont('GolosText', 'GolosText.ttf'))

    # Group data by stage
    grouped_data = group_data_by_stage(data)

    # Create pages for each stage
    page_count = 1
    for stage, stage_data in grouped_data.items():
        c.setFont('GolosText', 14)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(10, 280, f'Стадия: {stage}')

        create_pdf_page(c, stage_data, one_page)

        if not one_page:
            c.showPage()
            page_count += 1

            # Check if need to start a new file
            if page_count % 10 == 0:
                c.save()
                c = canvas.Canvas(filename + f"_page{page_count}.pdf", pagesize=A4)

    c.save()

# Read CSV data
data = read_csv_data('data.csv')

# Generate PDF document
generate_pdf('output.pdf', data, one_page=True)