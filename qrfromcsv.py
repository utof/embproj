import csv
import qrcode

# Open CSV file
with open('firstcol.csv', encoding='utf-8') as f:
  # Read CSV file 
  csv_reader = csv.reader(f) 
  next(csv_reader) # Skip header row
  
  # Loop through rows
  for row in csv_reader:
    name = row[0]
    link = row[1]
    
    # Generate QR code
    img = qrcode.make(link)
    
    # Save QR code with name 
    qr_file_name = f'{name}.png'
    img.save(qr_file_name)

    print(f'Saved QR code for {name}.')