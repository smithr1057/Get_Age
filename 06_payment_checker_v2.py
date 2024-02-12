# Functions

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

while True:
    payment_method = string_checker("Choose a payment method (cash or credit): ",
                                    2, payment_list)
    print(f"You chose {payment_method}")
