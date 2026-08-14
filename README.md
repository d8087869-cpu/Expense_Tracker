# Expense Tracker
Expense Tracker is a small Python command-line program for managing personal expenses.
It allows you to add expenses, display them in a table, filter expenses by category, and see a report with totals for each category.

## Installation
Clone the repository:
git clone https://github.com/d8087869-cpu/Expense_Tracker.git 
cd Expense-Tracker

### Create a virtual environment
python -m venv .venv

source .venv\Scripts\activate

# install the packages 
pip install -r requirements.txt


# and now how to use :

# to show all expense :
python main.py list 

# to add and expense :
python main.py add "Coffee" 12 food

# show expenses from one category:
python main.py list --category food

# Show a report with totals by category:
python main.py report

# to show all commands
python main.py --help

# ant to run the test use
python -m pytest -v

###
The project uses a .env file for settings.

create a .env file in the project folder

DATA_FILE=expenses.yaml
CURRENCY=ILS
MONTHLY_BUDGET=1500

# the .env file is not uploaded to github 

there is also a .env.example file in the repository that shows which settings are needed

if the .env file does not exist, the program uses default values.

# Packages:
Rich
PyYAML
Typer
python-dotenv
pytest