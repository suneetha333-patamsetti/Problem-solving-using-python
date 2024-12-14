def fun(n,m):
    if n==0:
        return 0
    print(m)
    fun(n-1,m+1)
    print(m-1)
x,y=5,1
fun(x,y)
