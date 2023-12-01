import csv
import qrcode
import tempfile
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
# import os

# Create the temporary directory if it doesn't exist
# if not os.path.exists('\\temp'):
#     os.makedirs('\\temp')

# Define constants
QR_CODE_SIZE = 30  # mm (Increase QR code size)
TEMPLATE_WIDTH = 70  # mm
TEMPLATE_HEIGHT = 74.25  # mm

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
                converted_row[key] = value if value else '?'

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
    return "123"  # Replace QR code image with "123" text

# Create PDF page
def create_pdf_page(data):
    # Create HTML template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Render HTML template with data
    encoded_data = {key: value.encode('utf-8') for key, value in data.items()}
    html = template.render(data=encoded_data)

    # Create temporary HTML file
    with tempfile.NamedTemporaryFile(mode='w', dir='.\\temp') as f:
        f.write(html.decode('utf-8'))
        f.flush()

        # Generate PDF from temporary HTML file
        HTML(f.name).write_pdf('page.pdf')

# Generate PDF document
def generate_pdf(filename, data):
    # Create PDF document
    with open(filename, 'wb') as f:
        # Split data into chunks for multiple pages
        chunks = [data[i:i + 12] for i in range(0, len(data), 12)]

        # Create a new page for each chunk of data
        for chunk in chunks:
            create_pdf_page(chunk)

            # Append page to PDF document
            with open('page.pdf', 'rb') as page_file:
                f.write(page_file.read())

            # Delete temporary HTML file
            import os
            os.remove('page.pdf')

# Read CSV data
data = read_csv_data('data.csv')

# Generate PDF document
generate_pdf('output.pdf', data)
