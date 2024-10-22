'''
Name: Guoming Liao
Date: 10/22/24
Description: Unit 4 Lesson 1 - while loops

'''

start_number = 10
while start_number >= 0:
    print(start_number)
    start_number = start_number - 1
print("Blastoff!") # always prints

while True:
    user_age = int(input("Enter age or -1 to quit: "))
    if user_age == -1:
        break
    else:
        continue