
from enum import Enum
import copy
print("Graph data structure adjancey list")

class Color (Enum) :
     WHITE = 0 
     GREY = 1 
     BLACK = 2 

class Direction (Enum):
    DIRECTED = 0 
    UNDIRECTED = 1

# Represent vertex, position is field poistiion in min array ,  pi is parent , 
class Vertex: 
    index = None
    COLOR = None
    key = None
    pi = None
    f = None

    position = None # 
    def __init__(self, index , Color, key, pi, position): 
        self.index = index
        self.COLOR = Color
        self.key = key
        self.pi = pi 
        self.position = position

    def __str__(self): 
        result = 'ADJ[' + str(self.index)+ ']'
        return result
    
    def getString(self):
        result = 'ADJ[' + str(self.index)+ ']'
        return result

# Represent edges , u and v are indice of Vertex , w is weight , next reference
class Edge:
    index = None
    u = None
    v = None
    w = None
    next = None

    def __init__(self, index, u, v, w, next) : 
       self.index = index
       self.u = u
       self.v = v
       self.w = float(w)
       self.next = next

    def __str__(self): 
        result = '[' + str(self.u) +" " + str(self.v) + ": " + "%.2f" % self.w + ']'
        return result

    def getString(self): 
        result = '[' + str(self.u) +" " + str(self.v) + ": " + "%.2f" % self.w + ']'
        return result

class LinkedList: 
    __Head = None
    __size = 0


    # Insert edge to the list 
    def push(self,e): 
        if(self.getSize() == 0):
            self.__Head = e
        else : 
            head = self.getHead()
            e.next = head
            self.__Head = e
        self.__size += 1 

    def pop(self):
        if(self.getSize() <= 0): 
            Exception("Out of bounds linked list")
        else: 
            self.__Head = self.__Head.next
            self.setSize(self.getSize() - 1)

    def getSize(self): 
        return self.__size

    def setSize(self,size):
        self.__size = size

    def print(self):
        cursor = self.getHead()
        while(cursor is not None): 
            print(str(cursor) + "-->" ,end='') 
            cursor = cursor.next

    def __str__(self):
        cursor = self.getHead()
        result = ''
        while(cursor is not None): 
            result += "--->" + str(cursor)   
            cursor = cursor.next
        return result

    def getHead(self): 
        return self.__Head


# Ajs list hold a list of V and E 
class AdjListGraph: 

    __time = 0
    __V = None
    __E = None
    __D = Direction.DIRECTED
    def __init__(self, D ,V, E): 
        self.__D = D
        self.__V = ["Dummy"]
        self.__V.extend(V)
        self.__E = ["Dummy"]
        list = []
        for i in range(len(self.__V)-1):
            LL = LinkedList()
            list.append(LL)
        self.__E.extend(list)

        # Iterate array of edges add them to respective vertices 
        match D:
            case Direction.DIRECTED: 
                for i in range(0,len(E)): 
                    self.__E[E[i].u].push(E[i])
            case Direction.UNDIRECTED:
                for i in range(0,len(E)): 
                    self.__E[E[i].u].push(E[i])
                    self.__E[E[i].v].push(Edge(E[i].index,E[i].v,E[i].u,E[i].w,None))
       
    def __str__(self):
        result = ''
        for i in range(1,len(self.__V)):
              result += str(self.__V[i]) + ":" + str(self.__E[i]) + "\n"
        return result
    
    def BFS_PATH(self, s , v):
        if s is v : 
            print(s)
        elif v.pi is None : 
            print(f"No path {s} to {v}")
        else: 
            self.BFS_PATH(s,self.__V[v.pi])
            print(v)

    def BFS(self,s):
        for i in range(1,len(self.__V)):
            if(self.__V[i] is not s): 
                self.__V[i].COLOR = Color.WHITE
                self.__V[i].key = float('inf')
                self.__V[i].pi = None
        que = []
        que.append(s)
        while ( len(que) != 0 ):
            u = que.pop()
            # now check in Adj list 
            head =  self.__E[u.index]
            cursor = head.getHead()
            while (cursor is not None):
                # turn grey all nodes push them to que
                i = cursor.v
                n = self.__V[i]
                if (n.COLOR == Color.WHITE) :  
                    n.COLOR = Color.GREY 
                    n.key = u.key + 1 
                    n.pi = u.index
                    que.append(n)
                cursor = cursor.next 
            u.COLOR = Color.BLACK


    def DFS(self): 
        for i in range(1,len(self.__V)): 
            self.__V[i].COLOR = Color.WHITE
            self.__V[i].pi = None
        self.__time = 0
        for i in range(1,len(self.__V)):
            if self.__V[i].COLOR == Color.WHITE:
                self.DFS_VISIT(self.__V[i])

    def DFS_VISIT(self,u):
        self.__time = self.__time + 1 
        u.key = self.__time 
        u.COLOR = Color.GREY
        # explore adj list of vertex 
        adj = self.__E[u.index]
        cursor = adj.getHead()
        while (cursor is not None):
            if (self.__V[cursor.v].COLOR == Color.WHITE ):
                self.__V[cursor.v].pi = u.index
                self.DFS_VISIT(self.__V[cursor.v])
            cursor = cursor.next  
        self.__time = self.__time + 1
        u.f = self.__time 
        u.COLOR = Color.BLACK

    def getVertices(self):
        return self.__V



# Utility function modifies arrays passed into the function 
def utility(V,E, str):
    file = open(str)
    V.clear()
    E.clear() 
    vertices = []
    edges = []

    flag = file.readline() 

    firstLine = flag.split(" ")

    n = int(firstLine[0])

    # Create the vertices 
    for i in range(1,n+1): 
        vertices.append(Vertex(i,Color.WHITE,0,0,0))

    flag = file.readline() 

    while (flag != ''): 
        curr = flag.split(" ")

        # Input vertices first 
        e = Edge(0,int(curr[1]), int(curr[2]),int(curr[3]),None)
        edges.append(e)
        flag = file.readline() 
       
    file.close()
    V.extend(vertices)
    E.extend(edges)

V = []
E = []

# Function return Vertices and edges of the graph 
utility(V,E,"case2.txt")


G = AdjListGraph(Direction.UNDIRECTED,V,E)

print(G)

Vertices = G.getVertices()

S = Vertices[1]
V = Vertices[7]

G.DFS()


print("DFS operation completed")
