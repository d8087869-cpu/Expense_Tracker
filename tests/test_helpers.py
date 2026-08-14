from expense_tracker.helpers import total, total_by_category

def test_total_empty_list():
    expenses = []

    assert total(expenses) == 0

def test_total_three_expenses():
    expenses = [
        {"category": "food", "amount": 10.0},
        {"category": "school", "amount": 20.0},
        {"category": "travel", "amount": 5.0}]
    assert total(expenses) == 35.0

def test_total_by_category():
    expenses = [
        {"category": "food", "amount": 10.0},
        {"category": "school", "amount": 20.0},
        {"category": "food", "amount": 5.0}]

    result = total_by_category(expenses)

    assert result == {
        "food": 15.0,
        "school": 20.0}

def test_total_by_category_empty_list():
    expenses = []

    assert total_by_category(expenses) == {}