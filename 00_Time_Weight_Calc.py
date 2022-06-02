
# Statement generator
def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)

    return ""

# Displays instructions / Information
def instructions():
    
    print()
    print("Please choose a number and its unit")
    print()
    print("This program finds the entered number and its unit and converts it into a unit of your choice")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    return ""

# checks the number whether if it isn't a integer
def num_check(question, low):
    
    valid = False
    while not valid:

        error = "Please enter a number that contains a measurement unit:  "
    
        print()

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
        
# Gives the user a choice if they want to convert into distance, time, and, weight
def user_choice():
    
    # Lists of valid responses
    distance_ok = ["distance,", "dist", "feet", "d"]
    time_ok = ["time", "oclock", "t"] 
    weight_ok = ["weight", "kg", "w", "mg", "g"]
   
    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("Measurement type (distance / time / weight): ").lower()

        # Checks for valid response and returns text, integer or image

        if response in distance_ok:
            return "distance"
            
        elif response in time_ok:
            return "time"
            
        elif response in weight_ok:
            return "weight"
            
        else:
            # if response is not valid, output an error
            print("Please choose a valid file type!")
            print()

# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)
    
    print()
    