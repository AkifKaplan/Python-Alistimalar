# Check if a number is positive and even
number = int(input("Enter a number:"))  # Take a number as input
if number <= 0:
    print(f'{number} is not a positive number')  # Number is not positive
else:
    if number % 2 != 0:
        print(f'{number} is not an even number')  # Number is positive but odd
    else:
        print(f'{number} is both even and positive number')  # Number is positive and even


# Vehicle maintenance year calculator
import datetime

date = input('When was your vehicle in traffic (YYYY/MM/DD)?')  # Get vehicle start date
date = date.split('/')  # Split the date into year, month, day

exittraffic = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))  # Convert to datetime object
Now = datetime.datetime.now()  # Get current date and time

Substract = Now - exittraffic  # Calculate the difference
day = Substract.days  # Get total number of days

# Check which maintenance year the vehicle is in
if day <= 365:
    print(f'your vehicle has been on the street for {day} days and you are in the 1st maintenance year')
elif day > 365 and day <= 365 * 2:
    print(f'your vehicle has been on the street for {day} days and you are in the 2nd maintenance year')
elif day > 365 * 2 and day <= 365 * 3:
    print(f'your vehicle has been on the street for {day} days and you are in the 3rd maintenance year')
elif day > 365 * 3 and day <= 365 * 4:
    print(f'your vehicle has been on the street for {day} days and you are in the 4th maintenance year')
else:
    print("ERROR!")  # If the number of days exceeds the expected range
