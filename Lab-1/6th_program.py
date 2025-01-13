# Create a list of fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Orange"]
print("Accessing elements using indexing:")
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")
print(f"Last fruit: {fruits[-1]}")

# Access elements using indexing
fruits[1] = "Kiwies"
print(f"Modified list is: {fruits}")

# Add and remove elements from the list
fruits.append("Watermelon")
print(f"List after addition: {fruits}")
fruits.remove("Watermelon")
print(f"List after removal: {fruits}")

# Find the length of the list
length = len(fruits)
print(f"Length of the list: {length}")

# Sort the list in ascending and descending order
fruits.sort()
print(f"Sorted fruits list in ascending order: {fruits}")
fruits.sort(reverse=True)
print(f"Sorted fruits list in descending order: {fruits}")
