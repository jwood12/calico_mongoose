# 3-7. 11/27/2023 You just found out that your new dinner table will not arrive in time for dinner, 
# and now you have space for only two guests.

# Start with your program from exercise 3-6. Add a new line that prints a message saying that you can only invite  
# two people for dinner.

guest = ['sponge', 'bob', 'squarepants']

message_1 = f"Dear {guest[0].title()}, Please come over for dinner. We're having fish."
message_2 = f"Dear {guest[1].title()}, Please come over for dinner. We're having fish."
message_3 = f"Dear {guest[2].title()}, Please come over for dinner. We're having fish."

print(guest[1].title(), end=' ' + "can't make it.")

guest.remove('bob')
print(guest)

guest.insert(1, 'patrick')
print(guest)

message_1 = f"Dear {guest[0].title()}, Please come over for dinner. We're still having fish."
message_2 = f"Dear {guest[1].title()}, Please come over for dinner. We're having fish."
message_3 = f"Dear {guest[2].title()}, Please come over for dinner. We're still having fish."

print(message_1)
print(message_2)
print(message_3)

print("Good News! I've found a bigger table.")

guest.insert(0, 'papa bear') 

guest.insert(3, 'mama bear') 

guest.append('baby bear') 
print(guest)

message_1 = f"Dear {guest[0].title()}, Please come over for dinner. We're still having fish."
message_2 = f"Dear {guest[1].title()}, Please come over for dinner. We're having fish."
message_3 = f"Dear {guest[2].title()}, Please come over for dinner. We're still having fish."
message_4 = f"Dear {guest[3].title()}, Please come over for dinner. We're still having fish."
message_5 = f"Dear {guest[4].title()}, Please come over for dinner. We're having fish."
message_6 = f"Dear {guest[5].title()}, Please come over for dinner. We're having fish."

print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)

print('Change 47, I can only invite two of you to dinner.')

# Use pop() to remove guest from your list one at a time until only two names remain in your list. Each time you pop a name from your list,
# print a message to that person letting them know you're sorry you can't invite them to dinner. 

guest = ['papa bear', 'sponge', 'patrick', 'mama bear', 'squarepants', 'baby bear']

popped_guest_1 = guest.pop()
print(guest)
print(f"{popped_guest_1.title()}, you are no longer invited!!!")

popped_guest_2 = guest.pop()
print(guest)
print(f"{popped_guest_2.title()}, you are no longer invited!!!")

popped_guest_3 = guest.pop()
print(guest)
print(f"{popped_guest_3.title()}, you are no longer invited!!!")

popped_guest_4 = guest.pop()
print(guest)
print(f"{popped_guest_4.title()}, you are no longer invited!!!")

# Print a messages to each of the two people still on your list, letting them know they're still invited.

print(f"{guest[0].title()} and {guest[1].title()} you are still invited.")

# Use del to remove the last two names from your list, so you have an emplty list. Print your list to make sure you actually have an empty list at the end of your program.

del guest[0]
del guest[0]
print(guest)