# 3-9. 11/29/2023 Working with one of teh programs from Exercises 3-4 through 3-7 (pages 41-42), use len()
# to print a message indicating the number of people you're inviting to dinner.

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

guest.insert(0, 'papa bear') 

guest.insert(3, 'mama bear') 

guest.append('baby bear') 
print(guest)

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

print(len(guest))

message_6 = f"There are {len(guest)} guest comming to dinner."
print(message_6)