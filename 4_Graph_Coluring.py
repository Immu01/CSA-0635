def is_safe(vertex,graph,color,c):
    for i in range(len(graph)):
        if graph[vertex][i]==1 and color[i]==c:
            return False
    return True
def graph_coloring_util(graph,m,color,v):
    if v==len(graph):
        return True
    for c in range(1,m+1):
        if is_safe(v,graph,color,c):
            color[v]=c
            if graph_coloring_util(graph,m,color,v+1):
                return True
            color[v]=0
    return False
def graph_coloring(graph,m):
    color=[0]*len(graph)
    if not graph_coloring_util(graph,m,color,0):
        print("\nNo solution exists")
        return False
    print("\nThe coloring : \n")
    for c in color:
        print(c,end=" ")
    print()
    return True
if __name__=="__main__":
    graph=[[0,1,1,1],
            [1,0,1,0],
            [1,1,0,1],
            [1,0,1,0]]
    m=3
    graph_coloring(graph,m)