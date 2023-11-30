import os

# Specify the directories to scan for fonts
font_directories = [
    'C:\\Windows\\Fonts',
    'C:\\Program Files\\Common Files\\Microsoft Shared\\Fonts',
]

for font_directory in font_directories:
    for filename in os.listdir(font_directory):
        if filename.endswith('.ttf') or filename.endswith('.otf'):
            print(filename[:-4])  # Remove extension
