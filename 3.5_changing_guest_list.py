# 3-5. 11/26/2023 You just heard that one of your guest can't make the dinner, so you need to send out a new
# set of invitations. You'll have to think of someone else to invite.

# Start with your program from exercise 3-4. Add a print() call at the end of your program, stating the name of
# the guest who can't make it. 

guest = ['sponge', 'bob', 'squarepants']

message_1 = f"Dear {guest[0].title()}, Please come over for dinner. We're having fish."
message_2 = f"Dear {guest[1].title()}, Please come over for dinner. We're having fish."
message_3 = f"Dear {guest[-1].title()}, Please come over for dinner. We're having fish."

print(guest[1].title(), end=' ' + "can't make it.")

# Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.

guest.remove('bob')
print(guest)

guest.insert(1, 'patrick')
print(guest)

# Print a second set of invitation messages, one for each person who is still in your list. 

message_1 = f"Dear {guest[0].title()}, Please come over for dinner. We're still having fish."
message_2 = f"Dear {guest[1].title()}, Please come over for dinner. We're having fish."
message_3 = f"Dear {guest[-1].title()}, Please come over for dinner. We're still having fish."

print(message_1)
print(message_2)
print(message_3)