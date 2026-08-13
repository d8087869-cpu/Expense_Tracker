import yaml
from datetime import date

def load_expenses(filename: str) -> list:
    try:
        with open(filename, "r") as file:
            expenses = yaml.safe_load(file)
            if expenses is None:
                return []

            return expenses
    except FileNotFoundError:
        return []

def save_expenses(filename: str, expenses: list) -> None:
    with open(filename, "w") as file:
        yaml.safe_dump(expenses, file)


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