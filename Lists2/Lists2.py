numbers = [1, 5, 3, 7, 6, 11, 9, 11, 12, 0]  # Initial list of numbers

print(numbers)               # Print the original list

print(min(numbers))          # Print the smallest number
print(max(numbers))          # Print the largest number

numbers.append(22)           # Add 22 at the end of the list
print(numbers)               # Print updated list

numbers.insert(2, 47)        # Insert 47 at index 2
print(numbers)               # Print updated list

numbers.pop()                # Remove the last element
print(numbers)               # Print updated list

numbers.pop(5)               # Remove the element at index 5
print(numbers)               # Print updated list

numbers.remove(5)            # Remove the first occurrence of 5
print(numbers)               # Print updated list

res = numbers.count(11)      # Count how many times 11 appears
print(res)                   # Print the count

numbers.sort()               # Sort the list in ascending order
print(numbers)               # Print sorted list

numbers.reverse()            # Reverse the list
print(numbers)               # Print reversed list

numbers.insert(5, 33)        # Insert 33 at index 5
print(numbers)               # Print updated list

res = numbers.index(33)      # Find the index of 33
print(res)                   # Print the index

numbers.clear()              # Remove all elements from the list
print(len(numbers))          # Print the length of the list (should be 0)

res = 5 in numbers           # Check if 5 is in the list
print(res)                   # Print the result (True/False)

markalar = []                # Create an empty list for brands
marka = input("Enter a car brand: ")  # Get a car brand from user input
markalar.append(marka)       # Add the entered brand to the list
print(markalar)              # Print the list of brands
