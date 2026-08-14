def total(expenses: list) -> float:
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total

def total_by_category(expenses: list) -> dict:
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in totals:
            totals[category] = 0

        totals[category] += amount
    return totals