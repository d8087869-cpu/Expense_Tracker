from expenses_list import *
from datetime import date
import questionary
from rich.console import Console
from rich.table import Table


def calculate_total(expenses: list) -> float:
    total = 0
    for expense in expenses:
        total+= expense['amount']
    return total 

def show_expenses(expenses: list) -> None: 
    table = Table()
    table.add_column('Date')
    table.add_column('Title')
    table.add_column('category')
    table.add_column('Amount')

    for expense in expenses:
        table.add_row(expense['date'], 
              expense['title'],
              expense['category'],
              f'{expense['amount']:.2f}')
    console.print(table)
    total = calculate_total(expenses)
    console.print(f"[bold green]Total: {total:.2f} ILS[bold green]")

def add_expense( 
    expenses: list, 
    title: str, 
    amount: float, 
    category: str ) -> None: 

    new_expense = {
        "date": str(date.today()),
        "title": title,
        "category": category,
        "amount": amount
    }
    expenses.append(new_expense)

def ask_for_expense(expenses: list) -> None:
    title = questionary.text('Expenses Title:').ask()
    amount = questionary.text("Amount:").ask()
    category = questionary.select('choose category:', 
                                  choices=['food', 'travel', 'school', 'entertainment', 'other' ]
                                  ).ask()
    amount = float(amount)
    add_expense(expenses, title, amount, category)

def main() -> None:
    show_expenses(expenses)
    answer = questionary.confirm(
        "Do you want to add an expense?"
    ).ask()
    if answer:
        ask_for_expense(expenses)
        print('\n Update expenses:')
        show_expenses(expenses)


console = Console()
main()