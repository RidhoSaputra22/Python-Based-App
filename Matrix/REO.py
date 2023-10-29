# This file is use to find the determinant of some matrices
# Version: 1.0
# Author: Ridho Saputra
import os 
os.system('cls')

m = [
    [1,1,2,-5],
    [2,5,-1,3],
    [2,1,-1,3],
    [1,-3,2,7]
]

mx = [
    [3,1,2,-5],
    [-3,5,-1,3],
    [4,1,-1,3],
    [-5,-3,2,7]
]

my = [
    [1,3,2,-5],
    [2,-3,-1,3],
    [2,4,-1,3],
    [1,-5,2,7]
]

mz = [
    [1,1,3,-5],
    [2,5,-3,3],
    [2,1,4,3],
    [1,-3,-5,7]
]

mw = [
    [1,1,2,3],
    [2,5,-1,-3],
    [2,1,-1,4],
    [1,-3,2,-5]
]


m1 = []
k_arr = []
r_arr = []

def reo(m):
    m1.append(m[0])
    for j in range(1, len(m)):
        arr = []
        temp = []
        for i in range(len(m[0])):
            k = m[j][0]/m[0][0]
            arr.append(m[j][i] - (k * m[0][i]))
            temp.append(f"{m[j][i]} - ({k * m[0][i]})")
        m1.append(arr)
        r_arr.append(temp)
        k_arr.append(f"{m[j][0]}/{m[0][0]}")


def print_M(m):
    for i in range(len(m[0])):
        for j in range(len(m[0])):
            print(m[i][j], end='\t')
        print()



print_M(mx)
print()
reo(mx)


print_M(m1)
print()

print(k_arr)
# print_M(r_arr)
