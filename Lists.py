list1 = ['one', 2, 3]       
list2 = [4, 'five', 'six']  

numbers = list1 + list2     # Concatenate list1 and list2 into numbers
print(numbers)              
print(numbers[0:2])         # Print the first two elements of numbers

numbers = numbers + ['7', 'eight']  # Add two more elements to numbers
print(numbers)                      

del numbers[-1]            # Delete the last element from numbers
print(numbers)             

print(numbers[::-1])       # Print numbers in reversed order

numbers2 = [list1, list2]  # Create a nested list containing list1 and list2
print(numbers2)            
print(len(numbers2))       # Print how many lists are inside numbers2

print(numbers2[1])         # Print the second inner list (list2)
print(numbers2[1][2])      # Print the third element of the second inner list

numbers2[-1][-1] = 6       # Change the last element of the last inner list to 6
print(numbers2)            

result = 'six' in numbers  # Check if 'six' is in numbers
print(result)              

result = 'six' in numbers2 # Check if 'six' is in numbers2 (anywhere inside)
print(result)              
