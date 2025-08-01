username = 'akifkplan'

a = input("Please enter a username: ")

# Check if the entered username matches the correct one
print(username == a)  

# Ask the user for the first exam score
exam1 = int(input("Please enter first exam: "))

# Ask the user for the second exam score
exam2 = int(input("Please enter second exam: "))

# Calculate the weighted average
# First exam counts 40%, second exam counts 60%
result = ((exam1 * 40) + (exam2 * 60)) / 100

# Check if the student passes (average >= 50)
print(f"Do you pass class? {result >= 50}")
