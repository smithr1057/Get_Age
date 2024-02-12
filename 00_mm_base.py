# Functions

# Checks that users response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")

        else:
            return response


# checks users enter an integer
def num_check(question):

    while True:
        try:
            # Ask the question
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter your age")


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


# checks user answers with valid answer
def string_checker(question, num_letters, valid_list):

    error = f"Please choose {valid_list[0]} or {valid_list[1]}"

    while True:

        # Ask user for choice (and put it in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[:num_letters] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# Main routine

yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

# set maximum number of tickets below
max_tickets = 3
tickets_sold = 0

want_instructions = string_checker("Do you want instructions? ", 1, yes_no_list)


if want_instructions == "yes":
    print("***Instructions***")
print()

# Loop to sell tickets
while tickets_sold < max_tickets:
    name = not_blank("Enter you name (or 'xxx' to quit): ")

    if name == 'xxx':
        break

    age = num_check("Enter your age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are to young for this movie")
        continue
    else:
        print("??? please enter you actual age")
        continue

    ticket_cost = calc_ticket_price(age)

    pay_method = string_checker("Choose a payment method (cash / credit): ",
                                2, payment_list)

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == max_tickets:
    print("Congrats you have sold all the tickets")
    print("")
else:
    print(f"You have sold {tickets_sold} ticket/s. there is {max_tickets - tickets_sold} ticket/s remaining")
