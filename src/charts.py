import matplotlib.pyplot as plt
from src.reports import category_summary

def generate_category_chart(expenses):
    summary = category_summary(expenses)
    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.figure()
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Category-wise Expense Distribution")
    plt.show()
