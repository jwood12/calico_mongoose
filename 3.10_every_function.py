# 3-10. 12/2/2023 Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter atleast once.

# Make a list and print the length of the list.
company = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot']

print(len(company))

# Print each item in the list.
print(company[0].title())
print(company[1].title())
print(company[2].title())
print(company[3].title())
print(company[4].title())
print(company[5].title())

# Write a message to each element in the list.

message_1 = f"Report to {company[0].title()} Company immediatley!"
print(message_1)

message_2 = f"Report to {company[1].title()} Company immediatley!"
print(message_2)

message_3 = f"Report to {company[2].title()} Company immediatley!"
print(message_3)

message_4 = f"Report to {company[3].title()} Company immediatley!"
print(message_4)

message_5 = f"Report to {company[4].title()} Company immediatley!"
print(message_5)

message_6 = f"Report to {company[5].title()} Company immediatley!"
print(message_6)

# Remove an element; add an elements to the beginning, middle, and end; and then resend the message.

del company[5]
print(company)

company[0] = 'apple'
print(company)

company.append('golf')
print(company)

company.insert(5, 'free')
print(company)

message_1 = f"Report to {company[0].title()} Company immediatley!"
print(message_1)

message_2 = f"Report to {company[1].title()} Company immediatley!"
print(message_2)

message_3 = f"Report to {company[2].title()} Company immediatley!"
print(message_3)

message_4 = f"Report to {company[3].title()} Company immediatley!"
print(message_4)

message_5 = f"Report to {company[4].title()} Company immediatley!"
print(message_5)

message_6 = f"Report to {company[5].title()} Company immediatley!"
print(message_6)

message_7 = f"Report to {company[6].title()} Company immediatley!"
print(message_7)

# Store the elements in a list. Make sure they are not in alphabetical order.

company = ['free', 'echo', 'bravo', 'delta', 'charlie', 'apple', 'golf']

# Print the origianl list in its original order. 

print(company)

# Use sorted to print your list in alphabetical order without modifying the actual list. 

print(sorted(company))

# Show that your list is still in its original order by printing it.

print(company)

# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.

print(sorted(company, reverse=True))  

# Show that your list is still in its original order by printing it.

print(company)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.

company.reverse()

print(company)

# Use reverse() to change the order of your list again. Print the list to show that its back to its original order.

company.reverse()

print(company)

# Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.

company.sort()

print(company)

# Use sort() to change your list so it's stored in reverse-alphabetical order. Print the list to show that its order has been changed.

company.sort(reverse=True)

print(company)

# Use pop() to remove a company from your list one at a time until only two companies remain in your list. Each time you pop a company from your list,
# print a message to that person letting them know their orders have been canceled. 

guest = ['free', 'echo', 'bravo', 'delta', 'charlie', 'apple', 'golf']

popped_company_0 = company.pop()
print(company)
print(f"{popped_company_0.title()}, your orders have been canceled!!!")

popped_company_1 = company.pop()
print(company)
print(f"{popped_company_1.title()}, your orders have been canceled!!!")

popped_company_2 = company.pop()
print(company)
print(f"{popped_company_2.title()}, your orders have been canceled!!!")

popped_company_3 = company.pop()
print(company)
print(f"{popped_company_3.title()}, your orders have been canceled!!!")

popped_company_4 = company.pop()
print(company)
print(f"{popped_company_4.title()}, your orders have been canceled!!!")

# Print a messages to each of the two companies still on your list, letting them know they're still required to report.

print(f"{company[0].title()} and {company[1].title()} you are still reuired to report!!!!")

# Use del to remove the last two companies from your list, so you have an emplty list. Print your list to make sure you actually have an empty list at the end of your program.

del company[0]
del company[0]
print(company)