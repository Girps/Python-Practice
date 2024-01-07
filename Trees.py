

# Implementing a BST data structure 

class BST : 
    __root = None 

    class BST_NODE:
        
        key = None
        value = None
        left = None
        right = None
        p = None
        def __init__(self,key,value):
            self.key = key
            self.value = value 

        def __str__(self):
            return f'({self.key},{self.value})'

    def Insertion(self,z):
        x = self.__root
        y = None
          # find none with x 
        while (x is not None) :
            y = x
            if (x.key < z.key):
                x = x.right
            else : 
                x = x.left
        # check if empty
        if (y is None):
            self.__root = z
        elif (y.key < z.key):
            z.p = y
            y.right = z
        else:
            z.p = y
            y.left = z

    def deletion(self,z):
        x = self.__root
        y = None
        # Find node to be deleted
        while (x is not None and x != z):
            y = x
            if (x.key < x.z):
                x = x.left
            else:
                x = x.right
        # Empty list case 
        if (x is None):
            Exception("Empty BST")
        
        # Case 1 no children  
        if (x.left is None and x.right is None):
            pass
    
    
    def Min(self,x):
        while (x is not None and x.left is not None): 
            x = x.left
        return x
    
    
    def Max(self,x):
        while (x is not None and x.right is not None):
            x = x.right
        return x
    
    def Search(self,key):
        z  = self.__root  
        # z traverse compare with x key  
        while (z is not None ): 
            if (key < z.key): 
                z = z.left
            elif (key == z.key):
                return z
            else : 
                z = z.right
        return None

    def Successor(self,x):
        if (x.right is not None):
            return self.Min(x.right)
        else:
            # get parent 
            y = x.p
            while (y is not None and y.right.key == x.key):
                 x = y
                 y = x.p 
        return y
    
    def Predesccor(self,x):
        if (x.left is not None):
            return self.Max(x.left)
        else:
            # get parent 
            y = x.p
            while (y is not None and y.left.key == x.key):
                 x = y
                 y = x.p 
        return y
             
    def Transplant(self,u,v):
        # case u is root
        if (u.p is None):
            self.__root = v
        elif (u.p.left.key == u.key):
            u.p.left = v
        elif ( u.p.right.key == u.key):
            u.p.right = v
        if(v is not None):
            v.p = u.p

    def __Delete(self, z):
        if (z.left is None):
            self.Transplant(z,z.right)
        elif (z.right is None):
            self.Transplant(z,z.left)
        else: 
            y = self.Min(z.right)
            # y is lower in the tree if so tran
            if (y is not z.right ): 
                self.Transplant(y,y.right)
                y.right = z.right 
                y.right.p = y
            self.Transplant(z,y) # replace z with y
            y.left = z.left
            y.left.p = y

    def Remove(self, u):
        z = self.Search(u)
        self.Remove(z)            
            

    def PrintInOrder(self): 
        self.__INORDER(self.__root)

    
    def PrintPostOrder(self): 
        self.__POSTORDER(self.__root)

    
    def PrintPreOrder(self): 
        self.__PREORDER(self.__root)


    def __INORDER(self,x):
        if (x is not None):
            self.__INORDER(x.left)
            print(x,end='')
            self.__INORDER(x.right)
    
    def __POSTORDER(self,x):
        if (x is not None):
            self.__POSTORDER(x.left)
            self.__POSTORDER(x.right)
            print(x,end='')
    
    def __PREORDER(self, x):
        if(x is not None):
            print(x,end='')
            self.__PREORDER(x.left)
            self.__PREORDER(x.right)

Tree = BST()

root = Tree.BST_NODE(10,"Jesse")

right = Tree.BST_NODE(15,"Bob")

left = Tree.BST_NODE(5,"Goku")


Tree.Insertion(root)
Tree.Insertion(right)
Tree.Insertion(left)

Tree.PrintInOrder()
print("\n")
Tree.PrintPostOrder()
print("\n")
Tree.PrintPreOrder()

print("\n")

print(Tree.Predesccor(root))