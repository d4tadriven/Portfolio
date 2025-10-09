
import json

def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, amount: {amount}")

def get_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += float(expense["amount"])
    return sum

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"Total budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense["description"]}: {expense["amount"]}")
    print(f"Total spent: {get_total_expenses(expenses)}")
    print(f"Remaining budget: {get_balance(budget, expenses)}")

def load_budget_data(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except(FileNotFoundError, json.JSONDecodeError):
        return 0, []
    
def save_budget_details(filepath, initial_budget, expenses):
    data = {
        "initial_budget": initial_budget,
        "expenses": expenses
    }
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

def main():
    print("Welcome to styn budgetting app!")
    filepath = "budget_data.json" # path to json file
    initial_budget, expenses = load_budget_data(filepath) # Get info from json file
    if initial_budget == 0:
        initial_budget = float(input("Please enter your initial budget: "))
    budget = initial_budget
    print(f"Your balance is {get_balance(budget, expenses)}")

    while True:
        print("\nWhat would you like to do?")
        print("option 1: Add an expense")
        print("option 2: Show budget details.")
        print("option 3: Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = input("Enter amount: ")
            add_expense(expenses, description, amount)
        elif choice == "2":
            show_budget_details(budget, expenses)
        elif choice == "3":
            save_budget_details(filepath, initial_budget, expenses)
            print("Exitting styn budgetting app... Bye!")
            break
        else:
            print("selected option invalid. Please select a different option.")

if __name__ == "__main__":
    main()