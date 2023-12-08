# 4-5. 12/7/2023 Make a list of the numbers from one to one million, and then use min() 
# and max() to make sure your list actually starts at one and ends at one million. Also, use the  
# sum() function to see how quickly Python can add a million numbers.

digits = list(range(1, 1000001))
print(min(digits))
print(max(digits))
print(sum(digits))
