# 4-15. 12/9/2023 Choose three of the programs you’ve written in this 
# chapter and modify each one to comply with PEP 8.
# Use for spaces for each indentation level. Set your text editor to insert 
# four spaces every time you press the TAB key, if you haven't already done so
# (see Appendix B for instructions on how to do this).
# Use less than 80 characters on each line, adn set your editor to show a 
# vertical guideline at the 80th character position.
# Don't use blank lines excessively in your program files.

# 4-1. 12/3/2023 Think of at least three kinds of yoru favorite pizza. Store 
# these pizza names in a list, and then use a for loop to print the name of 
# each pizza.
pizzas = ['sprite', 'coke', 'pepsi', 'water', 'milk', 'tea']
for pizza in pizzas:
    print(pizza)
# Modify your for loop to print a sentence using the name of the pizza, instead 
# of printng just the name of the pizza. For each pizza, you should have one 
# line of output containing a simple statement like I like pepperoni pizza. 
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
# Add a line at the end of your program, outside the for loop, that states how 
# much you like pizza. The output should consist of three or more lines about 
# the kinds if pizza you like and then an additional sentence, such as I really 
# love pizza!
print("\nI really love pizza.") 

# 4-2. 12/3/2023 Think of atleast three different animals that have a common 
# characteristic. Store the name of these animals in a list,
# and then use a for loop to print out the name of each animal.
animals = ['dog', 'cat', 'cow', 'goat', 'deer']
for animal in animals:
    print(animal)
# Modify your program to print a statement about each animal, such as A dog 
# would make a great pet. 
for animal in animals:
    print(f"A {animal} would make a great pet.")
# Add a line at the end of yoru program, stating what these animals have in 
# common. You could print a sentence, such as Any of these animals would make a 
# great pet. 
print("\nAny of these animals would make a great pet.")    

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 
# 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do 
# the following:
pizzas = ['sprite', 'coke', 'pepsi', 'water', 'milk', 'tea']
friend_pizzas = pizzas[:]
# Add a new pizza to the original list.
pizzas.append('kefir')
# Add a different pizza to the list friend_pizzas.
friend_pizzas.append('coffee')
# Prove that you have two separate lists. Print the message My favorite pizzas 
# are:, and then use a for loop to print the first list.
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
# Print the message My friend’s favorite pizzas are:, and then use a for loop 
# to print the second list. Make sure each new pizza is stored in the 
# appropriate list.
print("\nMy friend\'s favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)