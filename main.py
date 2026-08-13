from expenses_list import *
from datetime import date

def calculate_total(expenses: list) -> float:
    total = 0
    for expense in expenses:
        total+= expense['amount']
    return total 

def show_expenses(expenses: list) -> None: 
    for expense in expenses:
        print(expense['date'], 
              '|',
              expense['title'],
              '|',
              expense['category'],
              '|',
              f'{expense['amount']:.2f}')
    total = calculate_total(expenses)
    print(f"Total: {total:.2f} ILS")

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
    title = input('Enter your Title: ')
    amount = float(input('Enter the amount: '))
    category = input('Enter the category: ')
    add_expense(expenses, title, amount, category)

def main() -> None:
    show_expenses(expenses)
    clinet= input('\n Do you want to add an expense? (yes/no): ')
    if clinet.lower()== 'yes':
        ask_for_expense(expenses)
        print('\n Update expenses:')
        show_expenses(expenses)



main()