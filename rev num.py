def rev(n, res=0):
    if n == 0:
        return res
    else:
        d = n % 10
        res = res * 10 + d
        return rev(n // 10, res)

# Input from the user
n = int(input("Enter a number: "))
print("Reversed number:", rev(n))

    
