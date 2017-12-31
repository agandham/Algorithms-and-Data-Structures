'''
Created on Jul 8, 2017

@author: Abhilash Gandham
'''
def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j]<=x:
            i = i + 1
            k = A[i]
            A[i] = A[j]
            A[j] = k
    l = A[i+1]
    A[i+1]=A[r]
    A[r] = l
    return i+1
def quicksort(A,p,r):
    if (p < r):
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    return A
A = [43,22,26,15,18,9,32]
print(quicksort(A,0,len(A)-1))