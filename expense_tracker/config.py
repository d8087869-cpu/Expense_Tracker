import os
from dotenv import load_dotenv

load_dotenv()

DATA_FILE = os.getenv("DATA_FILE", "expenses.yaml")
CURRENCY = os.getenv("CURRENCY", "ILS")
MONTHLY_BUDGET = float(os.getenv("MONTHLY_BUDGET", "1500"))