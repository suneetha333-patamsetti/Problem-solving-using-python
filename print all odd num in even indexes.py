l = list(map(int, input().split()))
s = 0
for i in range(len(l)):
    if i % 2 == 0 and l[i] % 2 != 0:
        s += l[i]
print(s)

#input=4 3 5 8 7

#i = 0, l[i] = 4 → Skip (even number).
#i = 2, l[i] = 5 → Add 5 to s → s = 5.
#i = 4, l[i] = 7 → Add 7 to s → s = 12.






