import pandas
import random
from datetime import date
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


# Currency formatting function
def currency(x):
    return f"${x:.2f}"


# Displays instructions
def instructions():
    print('''\n
        ***** Instructions *****
        
        For each ticket, enter ...
        - The person's name (can't be blank)
        - Age (between 12 and 12)
        - Payment method (cash / credit)
        
        When you have entered all the users, press 'xxx' to quit.
        
        The program will then display the ticket details 
        including the cost of each ticket, the total cost
        and the total profit.
        
        This information will also be automatically written to 
        a text file.
        
        **************************''')

    return ""


# Main routine

yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

# dictionaries to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# set maximum number of tickets below
max_tickets = 5
tickets_sold = 0

# Dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

want_instructions = string_checker("Do you want instructions? ", 1, yes_no_list)


if want_instructions == "yes":
    instructions()
print()

# Loop to sell tickets
while tickets_sold < max_tickets:
    name = not_blank("Enter you name (or 'xxx' to quit): ")

    if name == 'xxx' and len(all_names) > 0:
        print()
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

    age = num_check("Age: ")

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

    print()

    if pay_method == "cash":
        surcharge = 0
    else:
        # Calculate 5% surcharge if users are paying by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # add ticket name, cost and surcharge it lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket (ticket price - 5)
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Choose a winner from our name list
winner_name = random.choice(all_names)

# Get position of winner name in list
win_index = all_names.index(winner_name)

# Look up total amount won (ticket price + surcharge
total_won = mini_movie_frame.at[win_index, 'Total']

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (using function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)


# *** Get current date for heading and filename ***
# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = f"----- Mini Movie Fundraiser Ticket Data ({day}/{month}/{year}) -----\n"
filename = f"MMF_{year}_{month}_{day}"

# Change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Create strings for printing....
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = f"Total Ticket Sales: {currency(total)}"
total_profit = f"Total Profit: {currency(profit)}"

if tickets_sold == max_tickets:
    sales_status = "\nCongrats you have sold all the tickets"
else:
    sales_status = f"\nYou have sold {tickets_sold} ticket/s. there is {max_tickets - tickets_sold} ticket/s remaining"

winner_heading = '\n---- Raffle Winner ----'
winner_text = f"Congratulations {winner_name}. You have won {currency(total_won)} " \
              f"ie: your ticket is free!"

print("---- Ticket Data ----")
print()

# Output table with ticket data and set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')
print(mini_movie_frame)

print()

print(ticket_cost_heading)

# Output total ticket sales and profit
print(total_ticket_sales)
print(total_profit)

print()

# Output raffle winner
print(winner_heading)
print(winner_text)

# Output number of tickets sold
print(sales_status)


