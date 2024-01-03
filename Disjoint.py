

print("Implementing Disjoint set data structure")




list =["$",-1,1,-1,3,-1,5,-1,7]

# Forest 
# [1] <- [2] 
# [3] <- [4]
# [5] <- [6]
# [7] <- [8]


class DisjointSet :
    A = None   
    def __init__ (self, arr):
        self.A = arr

    # Have a disjoint forset set 
    def UNION(self, x,y):
        self.LINK(self.FIND_SET(x), self.FIND_SET(y))

    def MAKE_SET(self, x): 
        self.A[x] = 0

    def FIND_SET(self,x):
        # base case parent holds negative  
        if ( self.A[x] <= 0 ) : 
            return x
        else : 
            root = self.FIND_SET(self.A[x])
            self.A[x] = root
            return root

    def LINK(self,x, y) : 
        # compare larger rank
        if (-1 * self.A[x] > -1 * self.A[y]) : 
            self.A[y] = x
        elif (-1 * self.A[x] < -1 * self.A[y]) :
            self.A[x] = y  
        else : 
            self.A[x] = y
            self.A[y] = ( self.A[y] - 1 ) 
     

dsj = DisjointSet(list)

dsj.UNION(2,5) 
 
print(dsj.A)

dsj.FIND_SET(2)

print(dsj.A)
