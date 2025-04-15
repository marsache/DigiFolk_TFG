import csv

# Function to read the input CSV, process the data, and generate the output CSV
def process_csv(input_csv, output_csv):
    # Reading the input CSV
    with open(input_csv, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

    # Initialize variables to hold the data for the output CSV
    result = []
    current_name = None
    verses = []
    letra = []

    # Loop through the rows in the input CSV
    for row in rows:
        # If the 'Nombre Obra' (name) field is not empty, we have a new entry
        if row['Nombre Obra']:
            # If there was a previous entry, add it to the result
            if current_name:
                result.append({
                    'Nombre': current_name,
                    'Letra': ' '.join(letra),
                    'Versos': '\n'.join(verses)
                })

            # Reset for the new entry
            current_name = row['Nombre Obra']
            verses = []
            letra = []
        
        # Add the verse to the verses list
        if row['Versos']:
            verses.append(row['Versos'])
            letra.append(row['Versos'])

    # Add the last entry if any exists
    if current_name:
        result.append({
            'Nombre': current_name,
            'Letra': ' '.join(letra),
            'Versos': '\n'.join(verses)
        })

    # Writing the output CSV
    with open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['Nombre', 'Letra', 'Versos']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result)

# Input and output file paths
input_csv = 'Coplas.csv'  # Replace with the path to your input CSV
output_csv = 'output.csv'  # Replace with the desired output file path

# Process the CSV files
process_csv(input_csv, output_csv)

print(f"CSV has been processed and saved to {output_csv}.")
