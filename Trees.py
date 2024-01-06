

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