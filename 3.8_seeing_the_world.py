# 3-8. 11/29/2023 Seeing the World: Think of at least five places you would like to visit.

# Store the locations in a list. Make sure that the list is not in alphabetical order.

places = ['east', 'west', 'north', 'south', 'up', 'down']

# Print your list in its original order. Don't worry about printing the list neatly; just print it as a raw Python list.

print(places)

# Use sorted() to print your list in alphabetical order without modifying the actual list.

print(sorted(places))

# Show that your list is still in its original order by printing it. 

print(places)

# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list. 

print(sorted(places, reverse=True))

# Show your list is still in its original order by printing it again.

print(places)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.

places.reverse()

print(places)

# Use reverse() to change the order of your list again. Print the list to show that its back to its original order.

places.reverse()

print(places)

# Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.

places.sort()

print(places)

# Use sort() to change your list so it's stored in reverse-alphabetical order. Print the list to show that its order has been changed.

places.sort(reverse=True)

print(places)