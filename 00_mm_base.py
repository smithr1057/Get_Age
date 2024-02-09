# Functions

# Check users have entered yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print(" **ERROR** please enter either yes / no")
            print()


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


# Main routine

# set maximum number of tickets below
max_tickets = 3
tickets_sold = 0

want_instructions = yes_no("Do you want instructions? ")


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

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == max_tickets:
    print("Congrats you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s. there is {max_tickets - tickets_sold} ticket/s remaining")

