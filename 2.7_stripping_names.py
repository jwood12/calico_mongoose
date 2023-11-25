# 2-7. 11/24/2023 Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combinatio, "\t" and "\n", at least once. 
# Print the name once, so teh whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

name = ' r2d2 '
formated_name = f'{name.upper()}'
print(formated_name)  

name = ' r2d2 '
formated_name = f'{name.upper().lstrip()}'
print(formated_name)  

name = ' r2d2 '
formated_name = f'{name.upper().rstrip()}'
print(formated_name)  

name = ' r2d2 '
formated_name = f'{name.upper().strip()}'
print(formated_name)  