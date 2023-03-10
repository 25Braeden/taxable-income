import time

while True:
    while True:
        try:
            income = int(input("Enter your taxable income: "))
            if income < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. You need to enter a number > 0")

    if income <= 10275:
        tax = income * 0.1
    elif income <= 20550:
        tax = 1027.50 + (income - 10275) * 0.12
    elif income <= 41775:
        tax = 3067.50 + (income - 20550) * 0.22
    elif income <= 164925:
        tax = 14605.50 + (income - 41775) * 0.24
    elif income <= 209425:
        tax = 33271.50 + (income - 164925) * 0.32
    elif income <= 539900:
        tax = 47367.50 + (income - 209425) * 0.35
    else:
        tax = 153798.50 + (income - 539900) * 0.37

    print(f"Your income tax is {round(tax, 2)}$")

    while True:
        try:
            go_again = input("Would you like to run this program again? (Y/N): ")
            if go_again.lower() in ['y', 'n']:
                break
            else:
                print("Invalid input. Enter either 'Y' or 'N'.")
        except ValueError:
            print("Invalid input. Enter either 'Y' or 'N'.")

    if go_again.lower() == 'n':
        break

for i in range(5):
    print(f"Closing program in {5 - i} seconds...")
    time.sleep(1)

print("Program closed.")
time.sleep(1)
