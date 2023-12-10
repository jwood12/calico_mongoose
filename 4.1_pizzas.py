# 4-1. 12/3/2023 Think of at least three kinds of yoru favorite pizza. Store these pizza names
# in a list, and then use a for loop to print the name of each pizza.

pizzas = ['sprite', 'coke', 'pepsi', 'water', 'milk', 'tea']

for pizza in pizzas:
    print(pizza)

# Modify your for loop to print a sentence using the name of the pizza, instead of printng just the name of the pizza.
# For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza. 

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the 
# kinds if pizza you like and then an additional sentence, such as I really love pizza!

print("\nI really love pizza.")