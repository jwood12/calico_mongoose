# 4-12. 12/8/2023 All versions of foods.py in this section have avoided using for loops when printing, to save space. 
# Choose a version of foods.py, and write two for loops to print each list of foods.

foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_foods = foods[0:3]
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in foods:
    print(food)

print("\nMy friend\'s favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)
