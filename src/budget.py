def set_budget():
    category = input("Enter category: ")
    amount = float(input("Enter monthly budget: "))
    return category, amount

def check_budget(expenses, category, budget):
    total = sum(e.amount for e in expenses if e.category == category)
    if total > budget:
        print("⚠ Budget exceeded!")
    else:
        print(f"Remaining Budget: ₹{budget-total}")
