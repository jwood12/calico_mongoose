# 4-10. Using one of the programs you wrote in this chapter, add several lines to the end of the 
# program that can do the following:

# Print the message The first three items in the list are:. Then use a slice to print the first three  
# items from that program’s list. 

animals = ['dog', 'cat', 'cow', 'goat', 'deer', 'gorilla', 'bear', 'moose', 'sloth']
print("The first three items in the list are:")
for animal in animals[:3]:
    print(animal) 

# Print the message Three items from the middle of the list are:. Then use a slice to print three  
# items from the middle of the list.

animals = ['dog', 'cat', 'cow', 'goat', 'deer', 'gorilla', 'bear', 'moose', 'sloth']
print("Three items from the middle of the list are:")
for animal in animals[3:6]:
    print(animal)

# Print the message The last three items in the list are:. Then use a slice to print three  
# items last three items in the list.

animals = ['dog', 'cat', 'cow', 'goat', 'deer', 'gorilla', 'bear', 'moose', 'sloth']
print("The last three items in the list are:")
for animal in animals[-3:]:
    print(animal)