# 5-1. 12/10/2023 You don't have to limit the number of tests you create to 10.
# If you want to try more comparisons, write more tests and add them to 
# conditional_tests.py Have atleast one True and one False result for each of
# the following:
# Tests for equality and inequality with strings
color = 'blue'
print(color == 'blue')
print(color == 'red')
calm_color = 'blue'
if calm_color != 'red':
    print("\nProceed with caution. The color is calm.\n")

# Tests using the lower() method
country = 'China'
print(country == 'china')
county = 'Jones'
print(county.lower() == 'jones')

# Numerical tests involving equality and inequality, greater than less than, 
# greater than or equal to, and less than or equal to
size = 14
print(size == 14)
room_number = 45
if room_number != 145:
    print("You're in the wrong room. Leave before something bad happens.")
age = 19
if age < 21:
    print("\nYOU CAN'T BUY THAT.")
age = 67
if age > 65:
    print("\nYou get a discount at the supermarket on Wednesdays.")
age = 34
if age >= 21:
    print("\nYou can buy that.")
age = 61
if age <= 64:
    print("\nYou don't get a discount at the supermarket on Wednesdays.\n")

# Tests using the and keyword and the or keyword
qty_1 = 8
qty_2 = 3
print(qty_1 <= 5 and qty_2 >= 3)
qty_1 = 8
qty_2 = 3
print(qty_1 >= 5 and qty_2 >= 3)
print((qty_1 <= 5) or (qty_2 >= 3))
print((qty_1 <= 5) or (qty_2 <= 2))

# Test whether an item is in a list 
requested_days_off = ['monday', 'tuesday', 'wednesday', 'saturday']
print('monday' in requested_days_off)
print('everday' in requested_days_off)

# Test wheter an item is not in a list
boycotted_companies = ['motorola mobility', 'ingram micro', 'riot games']
company = 'chick fil a'
if company not in boycotted_companies:
    print(f"\n{company.title()}, can take my money.")