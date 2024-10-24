'''
Name:
Date: 10/24/24
Description: For loops
'''

# this prints 0, 1, 2, 3, 4, each on their own line
# the number in range(stop) is how many nums are printed
# starting at 0 and ending at stop-1

# common use: doing a known number of things
for i in range(5):
    print(i)

# nums on same line
for i in range(5):
    print(i, end=" ")
print()
for i in range(5):
    print(i,end=", ")

# for loop style 2 - for i in range(start, stop)
# this prints start start+1, ...., stop-1
# loop runs stop-start number of times
print()
for num in range(2,6):
    print("*"*num)

for num in range(2,6):
    print(num, end=" ")

print()
print(f"------")
print(f"x | x^2")
for num_to_square in range(1,6):
    print(f"{num_to_square} | {num_to_square**2}")
print(f"------")

# for loop style 2 - for i in range(start, stop)
# this prints start start+1, ...., stop-1 but counts by step
# loop runs ceiling((stop-start)/step) times

for number in range(10,40,4): # want: 10 to 40 counting by 4s
    print(number, end= " ")

for number in range(12,93,7):
    print(number, end= " ")

print()
user_num = int(input("Give me a number: "))
sum = 0
for num in range(1, user_num+1):
    sum = sum + num

print(f"The sum is {sum} ")

# ask the user to enter 5 numbers (hint: use a loop)
# find the average of those numbers (hint: use a loop)
# print "The average of your numbers is -----"


un1 = int(input("Give me a number: "))
un2 = int(input("Give me a number: "))
un3 = int(input("Give me a number: "))
un4 = int(input("Give me a number: "))
un5 = int(input("Give me a number: "))
average = un1+un2+un3+un4+un5
print(f"The average of your numbers is: {average/5}")

user_sum = 0
num_values = 5
for i in range(num_values):
    user_num = int(input("Enter a number: "))
    user_sum = user_sum + user_num

average_ = user_sum/num_values
print(f"The average of your numbers is {average_}")