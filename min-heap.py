import numpy as np
path = 'data.txt'

#input data
def read_array(p):
    with open(p, 'r') as f:
        data = f.read().split(" ")

        return np.array(data, dtype=int)
    

def Heapify(i):
    
    l = 2*i+1
    r = 2*i+2
    k = i
    
    if r <= n and A[r] < A[k]:
        k = r
 
    if l <= n and A[l] < A[k]:
        k = l
           
    if (k != i):
        A[k],A[i] = A[i],A[k]
        Heapify(k)

def extract_root():
    global n
    A[0],A[n] = A[n],A[0]
    Heapify(0)
    n = n-1

def insert(x):
    global n,A
    n = n+1
    A = np.insert(A,n,x)
    for i in range(int(n/2),-1,-1):
        Heapify(i)




A = read_array(path)
N = 1000
n = N-1

for i in range(int(n/2),-1,-1):
    Heapify(i)

extract_root()
insert(1018)
insert(1021)
extract_root()
insert(1007)
extract_root()
extract_root()
insert(1026)
insert(1001)
extract_root()
extract_root()
insert(1014)
extract_root()


print(" Q2:","\n",A[0:20],"\n",A[n-19:n+1])



