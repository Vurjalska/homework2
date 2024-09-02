def sum_numbers():
    with open('numbers.txt', 'r') as file:
        total = sum(int(line) for line in file if line.strip())
    print(f"The sum is: {total}")

sum_numbers()
def count_words():
    with open('words.txt', 'r') as file:
        words = file.read().split()
    print(f"The number of words is: {len(words)}")

count_words()
import csv

def store_student_scores():
    with open('student_scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Score"])
        while True:
            name = input("Enter student name (or 'exit' to finish): ")
            if name.lower() == 'exit':
                break
            score = input("Enter student score: ")
            writer.writerow([name, score])

store_student_scores()
import csv

def calculate_total_salaries():
    with open('employee_data.csv', 'r') as infile, open('total_salaries.csv', 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Total Salary']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            total_salary = float(row['Base Salary']) + float(row['Bonus'])
            row['Total Salary'] = total_salary
            writer.writerow(row)

calculate_total_salaries()
import json

def calculate_total_cost():
    with open('products.json', 'r') as file:
        products = json.load(file)
    total_cost = sum(product['price'] for product in products)
    print(f"The total cost of all products is: {total_cost}")

calculate_total_cost()
import json

def read_contacts():
    with open('contacts.json', 'r') as file:
        contacts = json.load(file)
    for contact in contacts:
        print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")

read_contacts()
import csv
import json

def calculate_average_scores():
    with open('student_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, scores_json = row
            scores = json.loads(scores_json)
            average_score = sum(scores) / len(scores)
            print(f"Student: {name}, Average Score: {average_score}")

calculate_average_scores()
