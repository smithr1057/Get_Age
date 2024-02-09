# Functions
# Calculate ticket price based on age
def calc_ticket_price(var_age):

    # Ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.50

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.50

    # ticket price is $6.50 for 65+
    else:
        price = 6.50
    return price


# Main Routine
while True:

    # get age (assume user input is a valid int)
    age = int(input("Age: "))

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print(f"Age: {age}, Ticket price: ${ticket_cost:.2f}")
