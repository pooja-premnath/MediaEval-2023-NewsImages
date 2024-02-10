import csv
import json

def csv_to_json(csv_file, json_file, encoding='utf-8'):
    # Open the CSV file with the specified encoding
    with open(csv_file, 'r', encoding=encoding) as csv_input:
        # Create a CSV reader
        csv_reader = csv.DictReader(csv_input)
        
        # Convert the CSV data to a list of dictionaries
        data = [row for row in csv_reader]
        
        # Open the JSON file
        with open(json_file, 'w') as json_output:
            # Write the JSON data to the file
            json.dump(data, json_output, indent=2)

# Example usage
csv_to_json('rt-train-textImg.csv', 'rt-train-textImg.json')
