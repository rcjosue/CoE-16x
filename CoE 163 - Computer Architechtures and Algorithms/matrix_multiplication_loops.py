from time import time
import random

random.seed(0)

n =  500

def init_rand(mat,n):
  for x in range(n):
    new = []
    for y in range(n):
      new.append(random.random())
    mat.append(new)

def init_matrix(mat,n,value):
  for x in range(n):
    new = []
    for y in range(n):
      new.append(value)
    mat.append(new)

def fill_zero(mat,n):
  for x in range(n):
    for y in range(n):
     mat[x][y] = 0

A = []
B = []
C = []
print("Matrix size is %d-by-%d" % (n,n))

init_rand(A,n)
init_rand(B,n)
init_matrix(C,n,0)

t = time()
for i in range(n):
  for j in range(n):
    for k in range(n):
      C[i][j] = C[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("ijk completed in %f seconds" % (runtime))

fill_zero(C,n) #reset matrix C

t = time()
for k in range(n):
  for j in range(n):
    for i in range(n):
      C[i][j] = C[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("kji completed in %f seconds" % (runtime))

fill_zero(C,n)
t = time()
for j in range(n):
  for i in range(n):
    for k in range(n):
      C[i][j] = C[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("jik completed in %f seconds" % (runtime))

fill_zero(C,n)
t = time()
for j in range(n):
  for k in range(n):
    for i in range(n):
      C[i][j] = C[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("jki completed in %f seconds" % (runtime))

fill_zero(C,n)
t = time()
for k in range(n):
  for i in range(n):
    for j in range(n):
      C[i][j] = C[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("kij completed in %f seconds" % (runtime))

fill_zero(C,n)
t = time()
for i in range(n):
  for k in range(n):
    for j in range(n):
      C[i][j] = C[i][j] + A[i][k]*B[k][j]
runtime = time() - t
print("ikj completed in %f seconds" % (runtime))
