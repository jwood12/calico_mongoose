# 3-4. 11/26/2023 If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you'd like to invite to dinner. Then print a list to each person inviting them to dinner. 

guest = ['sponge', 'bob', 'squarepants']

message_1 = f"Dear {guest[0].title()}, Please come over for dinner. We're having fish."
message_2 = f"Dear {guest[1].title()}, Please come over for dinner. We're having fish."
message_3 = f"Dear {guest[-1].title()}, Please come over for dinner. We're having fish."

print(message_1) 
print(message_2)
print(message_3) 

