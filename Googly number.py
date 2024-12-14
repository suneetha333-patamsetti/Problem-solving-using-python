# Check if a number is a Googly Number
n = int(input("Enter a number: "))

# Convert the number to a string and check if '9' is present
if '9' in str(n):
    print(f"{n} is a Googly Number")
else:
    print(f"{n} is not a Googly Number")
