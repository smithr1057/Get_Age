# functions
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
tickets_sold = 0

while True:

    age = num_check("Enter your age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are to young for this movie")
        continue
    else:
        print("??? please enter you actual age")
        continue

    print("Valid age")
    tickets_sold += 1



