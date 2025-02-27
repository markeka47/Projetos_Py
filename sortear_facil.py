import random

# Define a list of numbers
numberss = [1, 2, 7, 9, 10, 12, 13, 14, 15, 18, 21, 22, 23, 24, 25]
numbersns = [3, 4, 5, 6, 8, 11, 16, 17, 19, 20]

# Randomly select 2 unique numbers from the list
selected_numberss = random.sample(numberss, 9)
selected_numbersns = random.sample(numbersns, 6)

print(f"Randomly selected numbers: {selected_numberss}")
print(f"Randomly selected numbers: {selected_numbersns}")