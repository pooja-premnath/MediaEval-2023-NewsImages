import csv

# Specify the input text file and CSV file names
input_file = "captions_combined.txt"
csv_file = "captions_combined.csv"

# Open the input text file and read lines
with open(input_file, 'r') as infile:
    lines = infile.readlines()

# Open the CSV file in write mode
with open(csv_file, 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)  

    # Write the data
    for line in lines:
        # Split each line into image and caption using the tab character
        image, caption = line.strip().split('\t')
        writer.writerow([image, caption])

print(f"CSV file '{csv_file}' created successfully.")
