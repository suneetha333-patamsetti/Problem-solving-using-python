s = input()            # Read input string
k = len(s) - 1         # Initialize k as the length of the string minus 1
res = 0                # Initialize result variable

for c in s:            # Iterate through each character in the string
    res += (10 ** k) * ord(c)
    k -= 1             # Decrease k with each iteration

print(res)
