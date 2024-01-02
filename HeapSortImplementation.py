
from enum import Enum 

class MODES(Enum): 
    MAX = 0 
    MIN = 1 

print("Implementent Heap Data Structure") 

list = [1,2,3,4,7,8,9,10,14,16] 


print(list)


class Heap:

    class Node : 
        def __init__(self,v,k): 
            self.value = v
            self.key = k
        def __str__ (self):
            str = '(' + str(self.key) + ',' + str(self.value) + ')'
        def __eq__(self, other): 
            if (self.value == other.value) : 
                return True 
            else : 
                return False
        def getStr(self):
            return  '(' + str(self.key) + ',' + str(self.value) + ')'
    # Build heap
    def __init__(self,A, mode):

       # convert it into pairs, (key,value)
       for i in range(0,len(A)): 
           A[i] = self.Node(A[i],A[i])
       self.A = A
       self.mode = mode 
       match mode: 
           case MODES.MAX: 
                self.BUILD_MAX_HEAP()
           case MODES.MIN: 
               self.BUILD_MIN_HEAP()
               

    # Remove Max
    def MAX_HEAP_EXTRACT_MAX(self): 
        max = self.ROOT 
        n = len(self.A) - 1 
        self.A[1] = self.A[n]
        self.A.pop()
        # ensure property is mainted
        self.MAX_HEAPIFY(self.A,1) 
        return max
    
    def MAX_HEAP_INSERT(self,x,n): 
        pass
    
    def ROOT(self):
        if (self.A == None or len(self.A) <= 1) : 
            raise Exception("Out of bounds")
        return self.A[1] 

    # Heap sort given Array 
    def HEAP_SORT(self,A,n):
        self.A = A
        result = []
        match self.mode: 
            case MODES.MAX : 
                self.BUILD_MAX_HEAP()
                for i in range(n,2,-1):
                    self.SWAP(self.A,1,i)
                    result.append(self.A.pop())
                    self.MAX_HEAPIFY(self.A,1)
                
            case MODES.MIN : 
                self.BUILD_MIN_HEAP()
                for i in range(n,2,-1):
                    self.SWAP(A,1,i)
                    result.append(self.A.pop())
                    self.MIN_HEAPIFY(self.A,i) 
        result.append(self.A.pop())
        result.append(self.A.pop())
        result.append(self.A.pop())
        self.A = result

    # Build Min heap 
    def BUILD_MIN_HEAP(self):
        list = [ self.Node(0,"Senteniel") ] 
        list.extend(self.A)
        r = len(list)     
        for i in range (( r // 2 ) ,0, -1): 
            self.MIN_HEAPIFY(list,i)
        self.A = list

    # Maintain min heap
    def MIN_HEAPIFY(self,list,i): 
        l =  self.LEFT(i) 
        r = self.RIGHT(i)
        smallest = i; 
        # Get index with largest to swap and Heapify 
        if ( l <= len(list)-1 and list[i].key > list[l].key) : 
            smallest =  l
        else : 
            smallest = i
        # Check right child 
        if ( r <= len(list)-1 and list[smallest].key > list[r].key) : 
            smallest = r
        # now check if largest is no longer root
        if (smallest != i) :
            # swap values
            self.SWAP(list,i,smallest)
            # check changed child is MAX-ROOT  
            self.MIN_HEAPIFY(list,smallest)

    # Build Max heap 
    def BUILD_MAX_HEAP(self):
        list = [ self.Node(0,"Senteniel")]
        list.extend(self.A)
        r = len(list)
       
        for i in range(0,len(list)):
            print(list[i].getStr())

        for i in range (( r // 2 ) ,0, -1): 
            self.MAX_HEAPIFY(list,i)
        self.A = list 
    
    # Maintain min heap
    def MAX_HEAPIFY(self,list,i): 
        l =  self.LEFT(i) 
        r = self.RIGHT(i)
        largest = i; 
        # Get index with largest to swap and Heapify 
        if ( l <= len(list)-1 and list[i].key < list[l].key) : 
            largest =  l
        else : 
            largest = i
        # Check right child 
        if ( r <= len(list)-1 and list[largest].key < list[r].key) : 
            largest = r
        # now check if largest is no longer root
        if (largest != i) :
            # swap values
            self.SWAP(list,i,largest)
            # check changed child is MAX-ROOT  
            self.MAX_HEAPIFY(list,largest) 

    def RIGHT(self,i): 
        return   (2*i)  + 1 

    def LEFT(self,i):
        return 2*i  

    def SWAP(self,list, i, j) : 
        a = list[i]
        b = list[j]
        list[i] = b 
        list[j] = a 

    def __str__(self) :
        result = '[';  
        for i in range(0, len(self.A)-1) : 
            result += self.A[i].getStr() + ","
        result += self.A[len(self.A)-1].getStr() + "]"
        return result; 

    # Increase key of given node 
    def MAX_HEAP_INCREASE_KEY(self,x,key):
        if (key < x.key):
            Exception("new key is smaller then node.key")
        x.key = key 
        # find indice where x occurs
        indice = -1  
        for i in range(1,len(self.A)) : 
            indice = i
        # Now exchange with root
        while (i > 1 and self.A[i//2].key < self.A[i].key) : 
            self.SWAP(self.A,i//2,i)
            i = (i // 2) 

    def MAX_HEAP_INSERT(self,x):
            # x is a node 
            infinty = float('-inf')
            key = x.key 
            x.key = infinty
            self.A.append(None)
            self.A[len(self.A)-1] = x
            self.MAX_HEAP_INCREASE_KEY(x,key)

            
        

heap  = Heap(list, MODES.MAX) 
print(heap)

heap.MAX_HEAP_EXTRACT_MAX()
heap.MAX_HEAP_INSERT(heap.Node(16,16))
print(heap)
