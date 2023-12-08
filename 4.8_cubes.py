# 4-8. 12/7/2023 A number raised to the third power is called a cube. For example, the cube of 2 is 
# written as 2**3 in Python. Make a list of the first 10 cubes (that is, the first integer from 1         
# through 10), and use a for loop to print the value of each cube. 

cubes = [ ]
for value in range(1, 11):
	cube = value **3
	cubes.append(cube)

print(cubes)
