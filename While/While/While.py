# Create an empty list to store products
products = []

# Ask how many products to add
i = int(input('How much do you want to add to list?\n'))

# Loop to collect product name and price
while i > 0:
    name = input('Name:')
    Price = input('Price:')
    print('\n')
    products.append({
        'Name': name, 'Price': Price  # Add product to the list
    })
    i -= 1

# Print products in reverse order
x = len(products) - 1
while x >= 0:
    print(products[x])
    x -= 1


# ------------------------------
# Collect 5 numbers and sort them
numbers = []

i = 1
while i < 6:
    num = int(input(f'Please enter {i}. number: '))
    numbers.append(num)  # Add number to the list
    i += 1

numbers.sort()  # Sort the list in ascending order
print(numbers)


# ------------------------------
# Ask for name until user enters something
name = ''

while not name:  # Loop until a non-empty name is entered
    name = input('Please enter your name:')
print(f'Hello, {name}')  # Greet the user
