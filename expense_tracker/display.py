from rich.console import Console
from rich.table import Table
from expense_tracker.config import *

console = Console()

def calculate_total(expenses: list) -> float:
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total

def show_expenses(expenses: list) -> None: 
    table = Table()
    table.add_column('Date')
    table.add_column('Title')
    table.add_column('Category')
    table.add_column('Amount')

    for expense in expenses:
        table.add_row(expense['date'], 
              expense['title'],
              expense['category'],
              f"{expense['amount']:.2f}")
    console.print(table)
    total = calculate_total(expenses)
    console.print(f"[bold green]Total: {total:.2f} {CURRENCY}[/bold green]")

def show_report(expenses: list) -> None:
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in totals:
            totals[category] = 0
        totals[category] += amount

    total = 0
    for category, amount in totals.items():
        console.print(f"{category}: {amount:.2f} {CURRENCY}")
        total += amount

    if total > MONTHLY_BUDGET:
        console.print(
            f"[bold red]Warning: You are over your monthly budget![/bold red]")