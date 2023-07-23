'''
You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.
Minor diagonal of a N X N matrix A is a collection of elements A[i, j] such that i + j = N + 1 (where i, j are 1-based).

Input
[  [1, -2, -3],
   [-4, 5, -6],
   [-7, -8, 9]  ]

Output
-5

Input
[  [3, 2],
   [2, 3]  ]

Output
4
'''
row = int(input())
col = int(input())
matrix = [[int(input()) for x in range(col)] for y in range(row)]
sum = 0
for j in range(col):
    sum += matrix[j][col-1-j]

print(sum)