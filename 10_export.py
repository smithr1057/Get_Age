import pandas
import random
from datetime import date


# Functions
# Currency formatting function
def currency(x):
    return f"${x:.2f}"


# Main routine

# dictionaries to hold ticket details
all_names = ['a', 'b', 'c', 'd', 'e']
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

tickets_sold = 3
max_tickets = 5

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket (ticket price - 5)
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Choose a winner from our name list
winner_name = random.choice(all_names)

# Get position of winner name in list
win_index = all_names.index(winner_name)

# Look up total amount won (ticket price + surcharge
total_won = mini_movie_frame.at[win_index, 'Total']

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

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

# list holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# print output
for item in to_write:
    print(item)

# Write output to file
# Create file to hold data (add.txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close file
text_file.close()
