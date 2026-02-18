import csv
import os
from src.expense import Expense

FILE_PATH = "data/expenses.csv"

def load_expenses():
    expenses = []
    if not os.path.exists(FILE_PATH):
        return expenses

    with open(FILE_PATH, newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            expenses.append(Expense(row[2], row[1], row[0], row[3]))
    return expenses

def save_expenses(expenses):
    with open(FILE_PATH, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for expense in expenses:
            writer.writerow(expense.to_list())

def backup_data():
    import shutil
    shutil.copy(FILE_PATH, "data/backup_expenses.csv")
