import csv

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    with open('firstcol.csv', 'w', encoding='utf-8') as outfile:
        for row in reader:
            outfile.write(row[0] + ',\n')