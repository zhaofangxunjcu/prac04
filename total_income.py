"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()

# You can add values to a list using the .append() method.
# two for loop