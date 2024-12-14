n = int(input())  # Read input from the user
x = 0  # Initialize x

# XOR each number from 0 to n
for i in range(n+1):
    x = x ^ i

print(x)
