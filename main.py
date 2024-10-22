def tailrecuse(n,num):
    if n>num:
        return
    print(n)
    tailrecuse(n+1,num)
n=int(input("Enter number of recursions: "))
tailrecuse(1,n)