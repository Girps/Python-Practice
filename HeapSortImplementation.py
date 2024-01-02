
from enum import Enum 
import copy

class MODES(Enum): 
    MAX = 0 
    MIN = 1 

print("Implementent Heap Data Structure") 

list = [1,2,3,4,7,8,9,10,14,16] 


print(list)


class Heap:

    # Inner Node class
    class Node :
        __value = None
        __key = None 
        def __init__(self,v,k): 
            self.__value = v
            self.__key = k
        def __str__ (self):
            str = '(' + str(self.__key) + ',' + str(self.__value) + ')'
        def __eq__(self, other): 
            if (self.__value == other.__value) : 
                return True 
            else : 
                return False
        def __lt__(self,other):
            return (self.__key < other.__key)

        def __gt__(self,other):
            return (self.__key > other.__key)
        
        def getStr(self):
            return  '( v: ' + str(self.__value) + ',' + " k: "+  str(self.__key) + ')'
        def getKey(self):
            return self.__key
        def getValue(self):
            return self.__value
        def setKey(self, key):
            self.__key = key
        def setValue(self,value):
            self.__value = value

    __A = None
    __mode = None
    # Build heap
    def __init__(self,A, mode):

       # convert it into pairs, (key,value)
       nodeList = [None] * len(A)
       for i in range(0,len(A)): 
           nodeList[i] = self.Node(A[i],A[i])
       self.__A = nodeList
       self.__mode = mode 
       match mode: 
           case MODES.MAX: 
                self.BUILD_MAX_HEAP()
           case MODES.MIN: 
               self.BUILD_MIN_HEAP()
               

    # Remove Max
    def MAX_HEAP_EXTRACT_MAX(self): 
        max = self.ROOT() 
        n = len(self.__A) - 1 
        self.__A[1] = self.__A[n]
        self.__A.pop()
        # ensure property is mainted
        self.MAX_HEAPIFY(self.__A,1) 
        return max
    
    def MIN_HEAP_EXTRACT_MIN(self):
        min = self.ROOT() 
        n = len(self.__A) - 1 
        self.__A[1] = self.__A[n]
        self.__A.pop()
        # ensure property is mainted
        self.MIN_HEAPIFY(self.__A,1) 
        return min
    
    def ROOT(self):
        if (self.__A == None or len(self.__A) <= 1) : 
            raise Exception("Out of bounds")
        return self.__A[1] 

    # Heap sort given Array 
    def HEAP_SORT(self,A,n):
        self.__A = copy.deepcopy(A)
        result = []
        match self.__mode: 
            case MODES.MAX : 
                self.BUILD_MAX_HEAP()
                print(self)
                for i in range(n,2,-1):
                    self.SWAP(self.__A,1,i)
                    result.append(self.__A.pop())
                    self.MAX_HEAPIFY(self.__A,1)
                result.append(self.MAX_HEAP_EXTRACT_MAX())
                result.append(self.MAX_HEAP_EXTRACT_MAX())

            case MODES.MIN : 
                self.BUILD_MIN_HEAP()
                for i in range(n,2,-1):
                    self.SWAP(self.__A,1,i)
                    result.append(self.__A.pop())
                    self.MIN_HEAPIFY(self.__A,1) 
                result.append(self.MIN_HEAP_EXTRACT_MIN())
                result.append(self.MIN_HEAP_EXTRACT_MIN())
        result.append(self.__A.pop())
        self.__A = result

    # Build Min heap 
    def BUILD_MIN_HEAP(self):
        list = [ self.Node(0,"Senteniel") ] 
        list.extend(self.__A)
        r = len(list)     
        
        for i in range (( r // 2 ) ,0, -1): 
            self.MIN_HEAPIFY(list,i)
        self.__A = list

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
        list = [ self.Node(0,"Senteniel")]
        list.extend(self.__A)
        r = len(list)
       

        for i in range (( r // 2 ) ,0, -1): 
            self.MAX_HEAPIFY(list,i)
        self.__A = list 
    
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
        size = self.getSize()
        for i in range(0, size) :
            if (self.__A[i].getKey() == "Senteniel") : 
                continue
            result += self.__A[i].getStr() + ","
        result += self.__A[len(self.__A)-1].getStr() + "]"
        return result; 

    # Increase key of given node 
    def MAX_HEAP_INCREASE_KEY(self,x,key):
        if (key < x.getKey()):
            Exception("new key is smaller then node.key")
        x.setKey(key) 
        # find indice where x occurs
        indice = -1  
        for i in range(1,len(self.__A)) :
            # Found index  
            if(x == self.__A[i]) :
                indice = i 
        # update index
        self.__A[indice] = x
        # Now exchange with root
        while (indice > 1 and self.__A[indice//2] < self.__A[indice]) : 
            self.SWAP(self.__A,indice//2,indice)
            indice = (indice // 2) 

    def MIN_HEAP_DECREASE_KEY(self,x,key):
         if (key > x.getKey()):
            Exception("new key is bigger then node.key")
         x.setKey(key) 
         # find indice where x occurs
         indice = -1  
         for i in range(1,len(self.__A)) :
            # Found index  
            if(x == self.__A[i]) :
                indice = i 
        # update index
         self.__A[indice] = x
        # Now exchange with root
         while (indice > 1 and self.__A[indice//2] > self.__A[indice]) : 
            self.SWAP(self.__A,indice//2,indice)
            indice = (indice // 2) 

    def MIN_HEAP_INSERT(self,x):
            # x is a node 
            infinty = float('inf')
            key = x.getKey()
            x.setKey(infinty)
            self.__A.append(None)
            self.__A[len(self.__A)-1] = x
            self.MIN_HEAP_DECREASE_KEY(x,key)
    
    def MAX_HEAP_INSERT(self,x):
            # x is a node 
            infinty = float('-inf')
            key = x.getKey() 
            x.setKey( infinty)
            self.__A.append(None)
            self.__A[len(self.__A)-1] = x
            self.MAX_HEAP_INCREASE_KEY(x,key)
    
    def getSize(self) :
        return len( self.__A ) - 1
    
    def getList(self) : 
        return self.__A[1:] 



list =  [1,2,3,4,7,8,9,10,14,16] 

heap = Heap(list, MODES.MIN)

print(heap)

heap.MIN_HEAP_INSERT(Heap.Node(10,50))

print(heap)

heap.HEAP_SORT(heap.getList(), heap.getSize())

print("Heap Sort")
print(heap.getSize())
print(heap)