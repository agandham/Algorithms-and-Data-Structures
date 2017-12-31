'''
Created on Jul 10, 2017

@author: Abhilash Gandham
'''
def maxheapify(A,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
    if(l < n and A[l] > A[i]):
        largest = l
    else:
        largest = i
    if(r<n and A[r]>A[largest]):
        largest = r 
    if(largest != i):
        A[i],A[largest] = A[largest],A[i]
        maxheapify(A, n, largest)
def heapsort(A):
    n = len(A)
    for i in range(n//2,-1,-1):
        maxheapify(A, n, i)
    for i in range(n-1,0,-1):
        A[i],A[0] = A[0],A[i]
        maxheapify(A, i, 0)
    return A
A = [22,12,15,18,16,66]
B = [22,13,14,68,26,17,13,1,16,22,18,13]
C = [3,2,5,8,7,6,4,9]
print(heapsort(B))