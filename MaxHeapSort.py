'''
Created on Jul 9, 2017

@author: Abhilash Gandham
'''
def maxheapify(A,i):
    l = 2*i + 1
    r = 2*i + 2
    heapsize = len(A)-1
    if(l<=heapsize and A[i] < A[l]):
        largest = l
    else:
        largest = i
    if(r<=heapsize and A[r] > A[largest]):
        largest = r
    if(largest != i):
        k = A[i]
        A[i] = A[largest]
        A[largest] = k
        maxheapify(A, largest)
def buildmaxheapify(A):
    x = []
    while(len(A) > 0):  
        for j in range((len(A)//2)-1,-1,-1):
            maxheapify(A, j)
        A[0],A[len(A)-1] = A[len(A)-1],A[0]
        x.append(A[len(A)-1])
        A = A[0:len(A)-1]
        buildmaxheapify(A) 
    return x
A = [22,12,15,18,16,66]
B = [22,13,14,68,26,17,13,1,16,22,18,13]
C = [3,2,5,8,7,6,4,9]
print(buildmaxheapify(C))