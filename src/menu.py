from src.expense import Expense
from src.file_manager import load_expenses, save_expenses, backup_data
from src.reports import category_summary, monthly_report
from src.charts import generate_category_chart
from src.budget import set_budget, check_budget
from src.utils import validate_date, validate_amount
import pandas as pd

def start_application():
    expenses = load_expenses()

    while True:
        print("\n====== PERSONAL FINANCE MANAGER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Monthly Report")
        print("5. Generate Chart")
        print("6. Budget Planning")
        print("7. Export to Excel")
        print("8. Backup Data")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = input("Amount: ")
            if not validate_amount(amount):
                print("Invalid amount")
                continue

            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            if not validate_date(date):
                print("Invalid date")
                continue

            description = input("Description: ")
            expenses.append(Expense(amount, category, date, description))
            save_expenses(expenses)
            print("Expense added!")

        elif choice == "2":
            for e in expenses:
                print(e)

        elif choice == "3":
            summary = category_summary(expenses)
            for k, v in summary.items():
                print(k, ":", v)

        elif choice == "4":
            report = monthly_report(expenses)
            for k, v in report.items():
                print(k, ":", v)

        elif choice == "5":
            generate_category_chart(expenses)

        elif choice == "6":
            category, budget = set_budget()
            check_budget(expenses, category, budget)

        elif choice == "7":
            df = pd.read_csv("data/expenses.csv")
            df.to_excel("data/expenses_export.xlsx", index=False)
            print("Exported to Excel!")

        elif choice == "8":
            backup_data()
            print("Backup created!")

        elif choice == "9":
            break
