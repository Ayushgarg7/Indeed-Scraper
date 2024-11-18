# jobs/calculate_salary.py
import numpy as np
from pymongo import MongoClient

def calculate_average_salary():
    client = MongoClient('localhost', 27017)
    db = client['indeed_scraper']
    collection = db['jobs']

    salaries = []
    for job in collection.find():
        if job['salary']:
            try:
                salary = int(job['salary'].replace('$', '').replace(',', ''))
                salaries.append(salary)
            except ValueError:
                continue

    if salaries:
        average_salary = np.mean(salaries)
        print(f"The average salary for Python developers is ${average_salary:.2f}")
    else:
        print("No salary data available.")

if __name__ == "__main__":
    calculate_average_salary()