class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0]*vertices for _ in range(vertices)]
    def is_safe(self,v,pos,path):
        if self.graph[path[pos-1]][v]==0 or v in path:
            return False
        return True
    def ham_util(self,path,pos):
        if pos==self.V:
            if self.graph[path[pos-1]][path[0]]==1:
                return True
            else:
                return False
        for v in range(1,self.V):
            if self.is_safe(v,pos,path):
                path[pos]=v
                if self.ham_util(path,pos+1):
                    return True
                path[pos]=-1
        return False
    def hamiltonian(self):
        path=[-1]*self.V
        path[0]=0
        if not self.ham_util(path,1):
            print("\nHamiltonian cycle does not exist")
            return False
        self.print_solution(path)
        return True
    def print_solution(self,path):
        for vertex in path:
            print(vertex,end=" ")
        print(path[0])
if __name__=="__main__":
    g=Graph(5)
    g.graph=[
        [0,1,1,0,0],
        [1,0,1,1,1],
        [1,1,0,1,0],
        [0,1,1,0,1],
        [0,1,0,1,0]
    ]
    g.hamiltonian()