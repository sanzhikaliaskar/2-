import csv

# Sample data
data = [
    ['Johnny', 87770000000],
    ['Jane', 87770000001],
    ['Bob', 87770000002]
]

# Open the CSV file in write mode
with open('sample.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['first_name', 'phone_number'])

    # Write the data rows
    for row in data:
        writer.writerow(row)
