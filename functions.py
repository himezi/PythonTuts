# Functions = A block of reuseable code
# To invoke a function place a set of () before the function name 
# Let's imagine I want to sing "Happy birthday" three times, the following may be written
##print("Happy birthday to you")
##print("Happy birthday to you")
##print("Happy birthday, happy birthday")
##print("Happy birthday to you")
##print()

# Without using functions, one may write the code thrice or place it within a loop
# Thus, to define a function, we type "def" followed by a unique function name, a set of () and a colon. This is followed on a new line by the functions whih are indented, as follows

##def hbday():
##    print("Happy birthday to you")
##    print("Happy birthday to you")
##    print("Happy birthday, happy birthday")
##    print("Happy birthday to you")
##    print()

# To invoke the function, type the function name and a set of (), then run.
    
##hbday()

# Using arguements, data (values or variables) an be sent directly to a function
# This would require a matching set of parameters that are in order, a placeholder {} and n "f" string Using the example above:

##def hbday(name):
##    print(f"Happy birthday {name}")
##    print(f"Happy birthday {name}")
##    print("Happy birthday, happy birthday")
##    print(f"Happy birthday to you {name}")
##    print()

##hbday("Bro")

# When you invoke a function, you can pass in more than one arguement. There has to be a matching set of parameters, with both the "f" string and placeholder text used
# The order of the prameters does matter!
# Let's add age to the arguements, as follows, and call multiple functions

##def hbday(name, age): # note that the order of the parametrs matter
##    print(f"Happy birthday {name}")
##    print(f"You are {age}  years today")
##    print("Happy birthday, happy birthday")
##    print(f"Happy birthday to you {name}")
##    print()

##hbday("Bro", 20)
##hbday("Kay", 30)
##hbday("Joe", 40)

# Note that "name" and "age" above can be called anything, example "x" and "y"

# A function can be defined with multiple parameters. Example, let's define a display invoice as follows

##def display_invoice(username, amount, due_date):
##    print(f"Hello {username}")
##    print(f"Your bill of ${amount:.2f} is due: {due_date}")

##display_invoice("BroCode", 42.50, "01/01")

# Return statement: a statement used to end a function and send result back to the caller. See example below

##def add(x, y):
##    z = x + y
##    return z

##def subtract(x, y):
##    z = x - y
##    return z

##def multiply(x, y):
##    z = x * y
##    return z

##def divide(x, y):
##    z = x / y
##    return z

##print(add(1, 2))
##print(subtract(1, 2))
##print(multiply(1, 2))
##print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)