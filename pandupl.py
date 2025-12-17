import pickle

# A list of numbers
numbers = [10, 20, 30, 40, 50]

# Save (dump) the list to a file
with open("numbers.txt", "wb") as f:
    pickle.dump(numbers, f)

# Load (read) the list back
with open("numbers.txt", "rb") as f:
    loaded_numbers = pickle.load(f)

# Display the numbers
print("Loaded list:", loaded_numbers)

# Loop through the list
for num in loaded_numbers:
    print(num)