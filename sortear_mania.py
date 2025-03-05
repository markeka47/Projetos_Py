import random

# Define a list of numbers
col1 = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
col2 = [2, 12, 22, 32, 42, 52, 62, 72, 82, 92]
col3 = [3, 13, 23, 33, 43, 53, 63, 73, 83, 93]
col4 = [4, 14, 24, 34, 44, 54, 64, 74, 84, 94]
col5 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
col6 = [6, 16, 26, 36, 46, 56, 66, 76, 86, 96]
col7 = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97]
col8 = [8, 18, 28, 38, 48, 58, 68, 78, 88, 98]
col9 = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]
col10 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Randomly select 2 unique numbers from the list
selected_col1 = random.sample(col1, 3)
selected_col2 = random.sample(col2, 3)
selected_col3 = random.sample(col3, 3)
selected_col4 = random.sample(col4, 4)
selected_col5 = random.sample(col5, 3)
selected_col6 = random.sample(col6, 3)
selected_col7 = random.sample(col7, 3)
selected_col8 = random.sample(col8, 3)
selected_col9 = random.sample(col9, 5)
selected_col10 = random.sample(col10, 5)


print(f"Randomly selected numbers: {selected_col1}")
print(f"Randomly selected numbers: {selected_col2}")
print(f"Randomly selected numbers: {selected_col3}")
print(f"Randomly selected numbers: {selected_col4}")
print(f"Randomly selected numbers: {selected_col5}")
print(f"Randomly selected numbers: {selected_col6}")
print(f"Randomly selected numbers: {selected_col7}")
print(f"Randomly selected numbers: {selected_col8}")
print(f"Randomly selected numbers: {selected_col9}")
print(f"Randomly selected numbers: {selected_col10}")