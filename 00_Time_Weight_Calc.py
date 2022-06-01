

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

def 