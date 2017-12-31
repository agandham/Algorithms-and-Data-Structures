'''
Created on Jul 7, 2017

@author: Abhilash Gandham
'''

def Merge(L,R,A):
    m = len(L)
    n = len(R)
    i,j,k = 0,0,0
    while(i<m and j < n):
        if(L[i] < R[j]):
            A[k] = L[i]
            i = i+1
            k = k+1
        elif(R[j] < L[i]):
            A[k] = R[j]   
            j = j+1
            k = k+1
    while(i < m):
        A[k] = L[i]
        i = i+1
        k = k+1
    while(j< n):
        A[k] = R[j]
        j = j+1
        k = k+1
    return A

def MergeSort(A):
    x = len(A)
    if(x>1):
        mid = x//2
        left = A[0:mid]
        right = A[mid:x]
        MergeSort(left)
        MergeSort(right)
        Merge(left,right, A)
    return A

A = [22,12,15,18,16,66]
print(MergeSort(A))
            