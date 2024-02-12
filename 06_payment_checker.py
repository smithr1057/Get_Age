# Functions

# Check users have entered yes / no to a question
def cash_credit(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            response = "cash"
            return response

        elif response == "credit" or response == "cr":
            response = "credit"
            return response
        else:
            print(" **ERROR** please enter either cash or credit")
            print()


# Main routine
while True:
    payment_method = cash_credit("Choose a payment method (cash or credit): ")
    print(f"You chose {payment_method}")

