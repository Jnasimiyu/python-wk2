# Create an empty list called my_list
my_list = []

# Append elements 10, 20, 30, 40 to my_list
my_list.extend([10, 20, 30, 40])

# Insert value 15 at the second position in the list
my_list.insert(1, 15)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print("Index of 30 in my_list:", index_30)

# Print the updated my_list
print("Updated my_list:", my_list)
