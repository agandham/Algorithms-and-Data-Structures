'''
Created on Jul 6, 2017

@author: Abhilash Gandham
'''
def InsertionSort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while(j>=0 and A[j]>key):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    return A

A = [22,12,15,18,16,66]
print(A)
print(InsertionSort(A))
            