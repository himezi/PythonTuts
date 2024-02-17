# COLLECTIONS IN PYTHON: single "vaiable" used to store multiple values. Types of general pupose collections include list [], set {}, tuple() and dictionaries.

# Let's imagine there is a variable called "fruit" who's value is "apple"
##fruit = "apple"
##print(fruit)
# The variable "fruit" can be turned into a collection by surrounding the values with the appropriate bracket for the desired type of collection. 

# Let us consider the list.
    # LIST: these use square brackets[]. They are ordered and changeable. Duplicates ok. Using the variable "fruits",
##fruits=["apple", "orange", "banana", "mango", "coconut", "cashew", "avocado"]
##print(fruits)

    # To access one of the elements within the collection the index operator can be used like so:
##print(fruits[2])
    # Note that the first element will have an index of 0, the next, 1, 2 etc, up to n-1, where n is the total number of elements within the collection. Each value within a collection is known as an element.
    # With the "index" operator, one could set a beginning index and an ending index. This would print the number of elements specified. For example
##print(fruits[0:3]) # This would print elements 0 , 1 and 2, excluding 3. The ending index is treated as n-1 and usually excluded.
    # The index operator can be written without the 0 as follows
##print(fruits[:3])   
    # The index operator can be written to print in a stepwise fashion by using the double colon :: as follows 
##print(fruits[::2])     # This will print every second element beginning from index 0
##print(fruits[::3])     # This will print every third element beginnning from index 0, etc
    # To print the collections backwards, the negative sign is used with the end index as follows
##print(fruits[:-1])
##print(fruits[::-3])

# One can also iterate over collections with the "for loop"
##for fruit in fruits:
    ##print(fruit)

# Various methods to use with collections
    # To list the different methods available to a collection, the "dir" function can be used with "print"
##print(dir(fruits))  
    # For a description of the various methods, the "help" function is used
##print(help(fruits))
    # To determine the length of how many elements within a collection, the "len" function is used
##print(len(fruits))
#   To find out if  value is within a collection, the "in" operative is used.
##print("apple" in fruits)
##print("pineapple" in fruits)
    # To change any of the values within the list, select the required index and assign new value
##fruits[0] = "pineapple"  # Remember lists are ordered and can be changed.
##for fruit in fruits:
    ##print(fruit)    # We notice that the 0 index is now pineapple, rather than apple
    # Using index, one can reassign any of the variables
##fruits[1] = "pineapple"
##for fruit in fruits:
# Other methods available for lists:
    # Append: To add an element to the end of a list, use the ".append" operative
##fruits.append("pear")
    # Remove: This removes an element from a list
##fruits.remove("apple")
    # Insert: To insert a value at a given index
##fruits.insert(0, "pineapple")
    # Sort: To sort a list in order
##fruits.sort()     # This sorts in alphabetical order.
    # Reverse: To reverse a list
##fruits.reverse()    # This reverses the order in which the list was written, not alphabetical order
    # To reverse the alphabetical order, first sort, then reverse
##fruits.sort() 
##fruits.reverse()
    # Clear: To clear a list
##fruits.clear()
    # To return an index of say, apple
##print(fruits.index("apple"))
    # Count: To count the amount of times that a value is found in a list, since duplication is allowed
##print(fruits.count("apple"))


# Let us consider the set.
    # SET: These use curly brackets {}. They are unordered and immutable. but add/remove are ok. No duplicates allowed. Using the variable "fruits",
##fruits={"apple", "orange", "banana", "mango", "coconut", "cashew", "avocado"}
    # Printing the set will list all the items in the set, but not in the order they were listed. Running the "print" function multiple times will produce a different order each time 

    # The "dir", "help", "len" and "in" functions can be used in the same way as for lists with similar results.
    # The "index" function cannot be used for set because they are unordered and unsubscriptible
    # The "add" and "remove" and "clear" methods can be used much in the ssame way as for lists. 
    # Pop: Removes whatever element is first, in a random manner
##fruits.pop()
    # Sets work well when dealing with constants.


#Let us consider tuples
    # TUPLE: These use parennthesis. They are ordered and unchangeable. Duplicates are possible. They are faster than lists. Using the variable "fruits",
##fruits=("apple", "orange", "banana", "mango", "coconut", "cashew", "avocado")

    # The "dir", "help" and "len" functions are possible.
    # The "in" operator is also possible.
    # Only "count" and "index" methods are available for tuple.
    # Tuples are iterable using the "for loop"

##print(fruits)


# Let us consider dictionaries.
    # DICTIONARY: These are  collection of {key:value} pairs. They are ordered and changeable. Duplicates are not allowed. Let's create a dictionary of countries and capitals.
capitals = {"USA": "Washington DC", "India":"New Delhi", "China":"Beijing", "Russia":"Moscow" }

    # The "dir" and "help" functions may be used.
    
# The following methods are possible:
    # Get method: This is used to check if a key is within a dictionary
##print(capitals.get("USA"))
##print(capitals.get("Nigeria"))
    # Get may be used with an "if" statement
##if capitals.get("USA"):
    ##print("That capital exists")
##else:
    ##print("That capital does not exist")

    # Update method: Inserts a new key value pair, or update an existing one
##capitals.update({"Germany":"Berlin"})

    # Pop: removes a key value pair
##capitals.pop("China")

    # Popitem: removes the latest key value pair that was added.
##capitals.popitem()

    # Clear: This clears the dictionary
##capitals.clear()

    # Keys: To get all of the keys within a dictionary but not the values 
##capitals.keys()     # This may also be inserted within a variable
keys = capitals.keys()
##print(keys)     # This is iterable and can be used within a "for loop"
##for key in capitals.keys():
   ## print(key)

    # Values method: To get all of the values within a dictionary
values = capitals.values()
##print(values)       # Using a "for loop" to iterate,
##for value in capitals.values():
    ##print(value)

    # Items method: Returns a dictionary object which resembles a 2-D list of tuples
items = capitals.items()
##print(items)   # Using a "for loop" to iterate "key, value";
for key, value in capitals.items():
    print(f"{key}: {value}")

##print(capitals)