# 4-6. 12/7/2023 Use the third argument of the range() function to make a list of the odd 
# numbers from 1 to 20. Use a for loop to print each number. 

odd_numbers = [value for value in range(1, 21, 2)]
for number in odd_numbers:
    print(number)