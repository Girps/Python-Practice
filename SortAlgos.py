# basic insertion 



print("Start of testing insertion sort") 

list = [5,1,6,69,-1]; 

# in python lists are 0 indexed based 
print(list[1]);  

# iteration in python 

size = len(list)
i = 0
while i < size :
    print(list[i])
    list[i]
    i = i + 1

print("Iteration complete")

# for loops in python 

list=  [5] 

for e  in list : 
    print(e) 

print("Iteration complete")

# insert sort implementation in python 
def INSERTION_SORT(A) : 
    print("Insertion_Sort() called")
    # i represents current unsorted card
    # j represents last sorted card
    for i in range(1,len(A)):
        key = A[i] 
        j = i - 1
        # only sort when key is less then sorted card
        while j > -1  and A[j] > key : 
            A[j+1] = A[j] 
            j = j - 1 
            A[j+1] = key

# call function
list = [5]
INSERTION_SORT(list); 
list = [5,1,2,4 ,6 ,- 1, 10]
INSERTION_SORT(list)
# print list 
print(list)

# Merge sort A for array and indexs from p to r
def MERGE_SORT(A, p, r):
    # Only call when p is not 1 or less
    if p < r :  
        q = (p + r) // 2 # ensure results in an integer
        MERGE_SORT(A,p,q)   # Divide
        MERGE_SORT(A,q+1,r) # Divide
        # Merge A[p:q] and A[q+1 : r] into A[p : r]
        MERGE(A, p , q , r) # Conquer 
    else:
        return # base case 1
    
def MERGE(A, p , q , r):
    Ln = q - p + 1 
    Rn = r - q  
    # left array 
    Left = []
    for i in range(0,Ln):
         Left.insert(i,A[p + i])
    # Right array
    Right = []
    for i in range(0,Rn): 
        Right.insert(i,A[q + i + 1])    

    # Now merge the sorted arrays 
    i = 0 # beginning of Left
    j = 0 # beginning of Right 
    k = p # insert position A

    while (i < Ln and j < Rn) : 
        if (Left[i] <= Right[j]): 
            A[k] = Left[i]
            i = i + 1
        else: 
            A[k] = Right[j]
            j = j + 1
        k = k + 1 

    # Insertion done for one side now copy the rest 
    # Left side case 
    while (i < Ln) : 
        A[k] = Left[i]
        i = i + 1
        k = k + 1 
    # Right side case
    while (j < Rn) : 
        A[k] = Right[j]
        j = j + 1
        k = k + 1

list = [4, 2]

MERGE_SORT(list,0,1) 

print(list)

list = [5,4,3,2,1] 

MERGE_SORT(list ,0 , len(list)-1)

print(list)

def QUICKSORT(A,p,r): 
    # A array indice inital 1, n
    if (p < r ) : 
        q = PARTITION(A,p,r) 
        QUICKSORT(A, p, q-1)  # sort lower side
        QUICKSORT(A,q + 1, r ) # sort higher side
    return 


def PARTITION(A, p, r):
    # pivot is last element 
    x = A[r]
    i =  p - 1 
    for j in range(p,r) : 
        if(A[j] <= x) :
            i = i + 1
            SWAP(A, i, j)
            j = j + 1
    # Termination swap right of low-side with x 
    SWAP(A, i + 1, r)
    return i + 1 
         

# Swap array indices 
def SWAP(A, i , j) : 
    a = A[i]
    b = A[j]
    A[i] = b 
    A[j] = a

list = [0,3,2,1]
QUICKSORT(list, 0, len(list) - 1)

print(list) 