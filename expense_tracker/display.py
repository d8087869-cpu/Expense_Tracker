from rich.console import Console
from rich.table import Table
from expense_tracker.config import *
from expense_tracker.helpers import *

console = Console()



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
    total_amount = total(expenses)
    console.print(
    f"[bold green]Total: {total_amount:.2f} {CURRENCY}[/bold green]")

def show_report(expenses: list) -> None:
    totals = total_by_category(expenses)

    total_amount = 0
    
    for category, amount in totals.items():
        console.print(f"{category}: {amount:.2f} {CURRENCY}")
        total_amount += amount

    if total_amount > MONTHLY_BUDGET:
        console.print(
            f"[bold red]Warning: You are over your monthly budget![/bold red]")