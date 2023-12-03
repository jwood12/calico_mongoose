# 3-6. 11/26/2023 You just found a bigger dinner table, so now more apace is available. 
# Think of more guest to invite to dinner.

# Start with your program from exercise 3-4 or 3-5. Add a print() call at the end of your program, informing people that 
# you've found a bigger table. 

guest = ['sponge', 'bob', 'squarepants']

message_1 = f"Dear {guest[0].title()}, Please come over for dinner. We're having fish."
message_2 = f"Dear {guest[1].title()}, Please come over for dinner. We're having fish."
message_3 = f"Dear {guest[-1].title()}, Please come over for dinner. We're having fish."

print(guest[1].title(), end=' ' + "can't make it.")

guest.remove('bob')
print(guest)

guest.insert(1, 'patrick')
print(guest)

message_1 = f"Dear {guest[0].title()}, Please come over for dinner. We're still having fish."
message_2 = f"Dear {guest[1].title()}, Please come over for dinner. We're having fish."
message_3 = f"Dear {guest[-1].title()}, Please come over for dinner. We're still having fish."

print(message_1)
print(message_2)
print(message_3)

print("Good News! I've found a bigger table.")

# Use insert() to add one new guest to the beginning of your list.

guest.insert(0, 'papa bear') 

# Use insert() to add one new guest to the middle of your list.

guest.insert(3, 'mama bear') 

# Use append() to add one new guest to the end of your list.

guest.append('baby bear') 
print(guest)

# Print a new set of invitation messages, one for each person on your list. 

message_1 = f"Dear {guest[0].title()}, Please come over for dinner. We're still having fish."
message_2 = f"Dear {guest[1].title()}, Please come over for dinner. We're having fish."
message_3 = f"Dear {guest[-1].title()}, Please come over for dinner. We're still having fish."
message_4 = f"Dear {guest[-2].title()}, Please come over for dinner. We're still having fish."
message_5 = f"Dear {guest[-3].title()}, Please come over for dinner. We're having fish."

print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)