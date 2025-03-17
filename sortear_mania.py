import random

# Define a list of numbers
col1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
col2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
col3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
col4 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
col5 = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
col6 = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
col7 = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
col8 = [71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
col9 = [81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
col10 = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# Randomly select 2 unique numbers from the list
selected_col1 = random.sample(col1, 3)
selected_col2 = random.sample(col2, 5)
selected_col3 = random.sample(col3, 5)
selected_col4 = random.sample(col4, 3)
selected_col5 = random.sample(col5, 6)
selected_col6 = random.sample(col6, 6)
selected_col7 = random.sample(col7, 6)
selected_col8 = random.sample(col8, 6)
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