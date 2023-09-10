class Graph:
    def __init__(self,vt):
        self.V = vt
        self.G = [[0 for C in range(vt)]
                    for R in range(vt)]
    
    def add_edge(self, S,D):
        self.G[S][D]=1
        self.G[D][S]=1
    def print_G(self):
        for i in range(self.V):
          for j in range(self.V):
              print(self.G[i][j],end=" ")
        print()

g = Graph(6)
g.add_edge(0,1)
g.add_edge(1,4)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,5)
g.print_G()
