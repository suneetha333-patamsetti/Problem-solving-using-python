def countways(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + countways(n // 2)
    else:
        return 1 + min(countways(n - 1), countways(n + 1))

# Corrected function call and output
n = 15
print("Minimum steps:", countways(n))
