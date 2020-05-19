'''
重点： 深度优先搜索，广度优先搜索
1、现实的图
    图用来表示很多现实生活中的系统
    道路系统，
    航空公司航班
    互联网连接
2、研究图的意义： 找到一个地方到另一个地方的最短或者最快，最简单的路径
3、图的定义和词汇
顶点： 顶点是图的基本部分，也可以叫做“键”，顶点可以you附加信息。这个附加信息就叫做“有效载荷”
边(弧)： 边连接两个顶点，已表明他们之间存在关系。边可以是单项的或者双向。如果途中的便是单向的。我们称该图是"有向图"
权重：边可以被加权仪表室从一个顶点到另一个顶点的成本

G表示图， G=(V,E)  V表示一组顶点  E表示一组边 每一个边是一个元祖(V,W)  V,W属于 V，可以添加第三个组件到边的元组来表示权重
V = {V0,V1,V2,V3,V4,V5}
E = {(V0,V1,V5),(V1,V2,4),(V2,V3,9),(V3,V4,7),(V4,V0,1),(V0,V5,2),(V5,V4,8),(V3,V5,3),(V5,V2,1)}

路径：图中的路径是由边连接的顶点序列，V3到V1的；路径的顶点序列  (V3, V4,V0,V1)  
    边   {(v3,v4,7),(v4,v0,1),(v5,v1,5)}
循环：有向图中的循环是在同一个顶点开始和结束的路径。没有循环的图像称为非循环图形，没有循环的有向图称为有向无环图或者DAG


4、图的抽象数据类型ADT
    Graph()   创建一个新的空图
    addVertex(vert)  向图中添加一个顶点实例
    addEdge(fromVert, toVert)  向连接两个顶点的图添加一个新的有向边
    addEdge(fromVert, toVert, weight)  相连接两个顶点的图添加一个新的加权的有向边
    getVertex(vertkey) 在图中找到名为vertKey的顶点
    getVertices()   返回途中所有顶点的列表
    in 但会True  如果vertex in graph 里给定的顶点在图中，否则返回False

5、图的实现：
邻接矩阵
    V0   V1   V2  V3  V4  V5
V0       5                 2
V1            4
V2                 9
V3                     7   3
V4  1
V5             1       8


矩阵中大多数单元格是空的，这样的矩阵叫做：稀疏矩阵
难度在于在python中药自建矩阵结构
 
邻接表(
https://www.cnblogs.com/cmusketeer/p/10331450.html
)
id = "V0"
adj = {V1:5,V5:2}
id = "V1"
adj = {V2:4}


优点：我们可以紧凑的表示稀疏图


6、邻接表的方式实现ADT(使用python中的字典)
   Graph(保存顶点的主列表)
   Vertex(表示图中的每个顶点)
   每个顶点有用字典来跟踪它连接的顶点和每个变得权重，我们定义connectedTo
'''

class Vertex:

    def __init__(self,key):

        self.id = key
        self.connectedTo = {}

    # 从这个顶点添加一个连接到另一个顶点
    def addNeighbor(self,nbr,weight=0):

        self.connectedTo[nbr] = weight

    # 返回邻接表中的所有顶点
    def getConnections(self):

        return self.connectedTo.keys()

    def getId(self):

        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:

    def __init__(self):

        self.vertList = {}
        self.numVertices = 0
    # 向图中添加一个顶点实例
    def addVertex(self, key):
        self.numVertices = self.numVertices +1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

    # 相连接两个顶点的图添加一个新的加权的有向边
    def addEdge(self,fromVert, toVert, weight=0):
        if fromVert not in self.vertList:
            nv = self.addVertex(fromVert)
        if toVert not in self.vertList:
            nv = self.addVertex(toVert)

        self.vertList[fromVert].addNeighbor(self.vertList[toVert],weight) 

    # 在图中找到名为vertKey的顶点
    def getVertex(self,vertkey):
        if vertkey in self.vertList:
            return self.vertList[vertkey]
        else:
            return None

    # 返回途中所有顶点的列表
    def getVertices():
        return self.vertList.keys()  


g = Graph()
for i in range(6):
    g.addVertex(i)

# print(g.vertList)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
    