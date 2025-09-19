import csv
# we will read a CSV file with student records and perform some operations 
file_path = input("Enter the path to the CSV file: ")
records = []
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        records.append(row)


def calculate_average(records):
    "Calculate and print the average grade from the records"
    total = sum(float(record['Grade']) for record in records)
    average = total / len(records)
    print(f"Average Grade: {average}")
    print("--------------------")



def filter_record(records):
    """Return student with grade >= 80"""
    filtered_records = [record for record in records if float(record['Grade']) >= 80.0]
    print("Student Report")
    print("--------------")

for record in filtered_records:
    print(f"Name: {record['Name']}")
    print(f"Grade: {record['Grade']}")
    print("--------------------")
