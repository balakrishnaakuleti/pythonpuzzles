import random
import sys

N = 3
M = 4
K = 4
W = 3

def printSeq(num):
    print((str(num)+' ') * W) 

random.randint(0,K)
arr = [[random.randint(0,K) for i in range(M)] for j in range(N)]
for i in range(N):
    print(arr[i])
#check columns
for j in range(M):
    for i in range(N):
        reference = arr[i][j]
        if i+W-1<N:
            for w in range(W):
                if reference != arr[i+w][j]:
                    break
                else :
                    if w == W-1:
                        printSeq(reference)
                        sys.exit(0)               
#check rows
for i in range(N):
    for j in range(M):
        reference = arr[i][j]
        if j+W-1<M:
            for w in range(W):
                if reference != arr[i][j+w]:
                    break
                else :
                    if w == W-1:
                        printSeq(reference)
                        sys.exit(0)
#check diagonal left to right
for i in range(N):
    for j in range(M):
        reference = arr[i][j]
        if i+W-1<N and j+W-1<M:
            for w in range(W):
                if reference != arr[i+w][j+w]:
                    break
                else :
                    if w == W-1:
                        printSeq(reference)
                        sys.exit(0)
#check diagonal right to left
for i in range(N):
    for j in range(M):
        reference = arr[i][j]
        if i-(W-1)>=0 and j+W-1<M:
            for w in range(W):
                if reference != arr[i-w][j+w]:
                    break
                else :
                    if w == W-1:
                        printSeq(reference)
                        sys.exit(0)                        
print("-1")
            

