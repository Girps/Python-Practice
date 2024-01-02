
from enum import Enum 

class MODES(Enum): 
    MAX = 0 
    MIN = 1 

print("Implementent Heap Data Structure") 

list = [1,2,3,4,7,8,9,10,14,16] 


print(list)



class Heap: 
    # Build max heap
    def __init__(self,A, mode): 
       self.A = A
       self.mode = mode 
       match mode: 
           case MODES.MAX: 
                self.BUILD_MAX_HEAP()
           case MODES.MIN: 
               self.BUILD_MIN_HEAP()
               self.A.pop()

    
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
        list = ["Sentientel"]
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
        if ( l <= len(list)-1 and list[i] > list[l]) : 
            smallest =  l
        else : 
            smallest = i
        # Check right child 
        if ( r <= len(list)-1 and list[smallest] > list[r]) : 
            smallest = r
        # now check if largest is no longer root
        if (smallest != i) :
            # swap values
            self.SWAP(list,i,smallest)
            # check changed child is MAX-ROOT  
            self.MIN_HEAPIFY(list,smallest)

    # Build Max heap 
    def BUILD_MAX_HEAP(self):
        list = ["Sentientel"]
        list.extend(self.A)
        r = len(list)     
        for i in range (( r // 2 ) ,0, -1): 
            self.MAX_HEAPIFY(list,i)
        self.A = list 
    
    # Maintain min heap
    def MAX_HEAPIFY(self,list,i): 
        l =  self.LEFT(i) 
        r = self.RIGHT(i)
        largest = i; 
        # Get index with largest to swap and Heapify 
        if ( l <= len(list)-1 and list[i] < list[l]) : 
            largest =  l
        else : 
            largest = i
        # Check right child 
        if ( r <= len(list)-1 and list[largest] < list[r]) : 
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
        for i in range(0, len(self.A)-2) : 
            result += str(self.A[i]) + ","
        result += str(self.A[len(self.A)-1]) + "]"
        return result; 
heap  = Heap(list, MODES.MAX) 
print(heap)
list = [1,2,3,4,7,8,9,10,14,16] 
heap.HEAP_SORT(list,len(list))

print(heap)