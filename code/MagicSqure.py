n = int(input("Enter the value of n: "))
L = [[0 for j in range(n)] for i in range(n)]
c=1
i=n//2
j=n-1
upper = n*n
while c<=upper:
    if i==-1 and j==n:  #
        i=0
        j=n-2
    elif i==-1:
        i=n-1
    elif j==n:
        j=0
    if [i][j] !=0:
        i=i+1
        j=j-2
        continue
        pass
    else:
        [i][j] = c
    c=c+1

for i in range(n):
    for j in range(n):
        print(L[i][j],end=' ')
    print()