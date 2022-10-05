a=[]
# for row
for i in range(3):
    b=[]
# for column
    for j in range(3):
        j= input("Enter Number: ")
        # adding vlaue of j in b.
        b.append(j)
    #adding the vlave of b in a to create 2D matrix
    a.append(b)
print("matrix is.... ")
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
