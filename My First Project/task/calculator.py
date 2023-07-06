# Write your code here
prices = {
    "Bubblegum": 2,
    "Toffee": 0.2,
    "Ice cream": 5,
    "Milk chocolate": 4,
    "Doughnut": 2.5,
    "Pancake": 3.2,
}

earned_amount = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80,
}


def view_prices():
    print("Prices:")
    for key, value in prices.items():
        print(f"{key}: ${value}")


def calculate_income():
    income = sum(earned_amount.values())
    return income


def view_earned_amount():
    print("Earned amount:")
    for key, value in earned_amount.items():
        print(f"{key}: ${value}")

    print(f"\nIncome: ${calculate_income()}")


def calculate_net_income():
    income = calculate_income()
    print("Staff expenses:")
    staff_expenses = int(input())
    print("Other expenses:")
    other_expenses = int(input())
    net_income = income - staff_expenses - other_expenses
    print(f"Net income= ${net_income}")


if __name__ == "__main__":
    view_earned_amount()
    calculate_net_income()
