'''
Created on Jul 12, 2017

@author: Abhilash Gandham
'''
def BubbleSort(A):
    x = len(A)
    for k in range(1,x):
        for j in range(0,x-k):
            if(A[j] > A[j+1]):
                A[j],A[j+1] = A[j+1],A[j]
    return A
A = [13,22,8,14,18]
B = [22,13,14,68,26,17,13,1,16,22,18,13,13,12,13]
C = [3,2,5,8,7,6,4,9]
print(BubbleSort(C))