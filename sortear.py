import random

# Define a list of numbers
numberspr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
numbersp = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]
numbersi = [1, 9, 15, 21, 25, 27, 33, 35, 39, 45, 49, 51, 55, 57]

# Randomly select 2 unique numbers from the list
selected_numbers = random.sample(numbers, 2)
selected_numbersp = random.sample(numbersp, 2)
selected_numbersi = random.sample(numbersi, 2)

print(f"Randomly selected numbers: {selected_numberspr}")
print(f"Randomly selected numbers: {selected_numbersp}")
print(f"Randomly selected numbers: {selected_numbersi}")