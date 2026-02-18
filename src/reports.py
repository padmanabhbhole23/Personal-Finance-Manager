from collections import defaultdict

def category_summary(expenses):
    summary = defaultdict(float)
    for e in expenses:
        summary[e.category] += e.amount
    return summary

def monthly_report(expenses):
    summary = defaultdict(float)
    for e in expenses:
        month = e.date[:7]
        summary[month] += e.amount
    return summary
