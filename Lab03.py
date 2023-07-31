# Print a list of random numbers
import random
random_list = random.sample(range(1,100), 7)
print(random_list)

# Print odd numbers
minimum = int(input("Please enter a lower limit for the range of odd numbers: "))
maximum = int(input("Please enter an upper limit for the range of odd numbers: "))
for i in range(minimum, maximum + 1):
    if (i % 2 != 0):
        print(i)

# Print even numbers
minimum1 = int(input("Please enter a lower limit for the range of even numbers: "))
maximum1 = int(input("Please enter an upper limit for the range of even numbers: "))
for i in range(minimum1, maximum1 + 1):
    if (i % 2 == 0):
        print(i)

# Count how many S there are in "Mississippi"
word = "Mississippi"
count = 0
for i in word:
    if i == "S" or i == "s":
        count = count + 1
print(f"There are {count} S's in the word Mississippi")
