n = int(input("enter the order of matrix:"))
A=[[[] for i in range(n)] for i in range(n)]
B=[[[] for i in range(n)] for i in range(n)]
C=[[[] for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        number=int(input("Please Enter Elements of Matrix A:"))
        A[i][j]=number

print('\n')
print('the matrix A is:')
for i in range(n):
    for j in range(n):
        print (A[i][j], end="  ")
    print('\n')


for i in range(n):
    for j in range(n):
        number=int(input("Please Enter Elements of Matrix B:"))
        B[i][j]=number

print('\n')
print('the matrix B is:')
for i in range(n):
    for j in range(n):
        print (B[i][j], end="  ")
    print('\n')

print('\n')
print('the sum of matrix  is:')
for i in range(n):
    for j in range(n):
        C[i][j]=A[i][j] + B[i][j]





for i in range(n):
    for j in range(n):
        print (C[i][j], end="  ")
    print('\n')
