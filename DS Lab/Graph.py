class Graph:
  def __init__(self,vt):
    self.v=vt
    self.G=[[0 for C in range(vt)]
            for R in range(vt)]

  def add_edge(self,s,d):
      self.G[s][d]=1
      self.G[d][s]=1
  def print_G(self):
    for i in range(self.v):
      for j in range(self.v):
        print(self.G[i][j] ," ",end='')
      print()

  def BFS(self,st):
    Vs=[False]*self.v
    Q=[]
    Q.append(st)
    Vs[st]=True
    while Q:
      F=Q.pop(0)
      print(F,end=" ")
      for i in range(self.v):
        if self.G[F][i]==1 and not Vs[i]:
            Q.append(i)
            Vs[i]=True

g=Graph(6)
g.add_edge(0,1)
g.add_edge(1,4)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)
print("Matrix representation of graph:")
g.print_G()
print("BFS Traversal is: ")
g.BFS(0)
