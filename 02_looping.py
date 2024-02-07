# Main routine

# set maximum number of tickets below
max_tickets = 3

# Loop to sell tickets
tickets_sold = 0
while tickets_sold < max_tickets:
    name = input("Please enter you name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == max_tickets:
    print("Congrats you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s. there is {max_tickets - tickets_sold} ticket/s remaining")

