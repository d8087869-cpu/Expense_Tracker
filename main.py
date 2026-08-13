import typer
from expense_tracker.config import *
from expense_tracker.storage import *
from expense_tracker.display import *

app = typer.Typer()

@app.command()
def add(title: str, amount: float, category: str) -> None:
    expenses = load_expenses(DATA_FILE)
    add_expense(expenses, title, amount, category)
    save_expenses(DATA_FILE, expenses)
    print(f"Added: {title} - {amount:.2f} {CURRENCY}")


@app.command()
def list(category: str = None) -> None:
    expenses = load_expenses(DATA_FILE)

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"] == category]
    show_expenses(expenses)

@app.command()
def report() -> None:
    expenses = load_expenses(DATA_FILE)
    show_report(expenses)

    
if __name__ == "__main__":
    app()