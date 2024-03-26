#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#define N 4
int min(int a,int b) 
{
    return (a<b)?a:b;
}
int tsp(int graph[N][N],int start_vertex,int visited_mask) 
{
    if (visited_mask==((1<<N)-1)) 
    {
        return graph[start_vertex][0];
    }
    int min_cost=INT_MAX;
    for (int i=0;i<N;i++) 
    {
        if (!(visited_mask&(1<<i))) 
        {
            int cost=graph[start_vertex][i]+tsp(graph,i,visited_mask|(1<<i));
            min_cost=min(min_cost,cost);
        }
    }
    return min_cost;
}
int main() 
{
    int graph[N][N]= 
    {
        {10,9,11,8},
        {7,8,9,10},
        {9,9,10,7},
        {8,10,9,10}
    };
    int start_vertex=0,min_cost=tsp(graph,start_vertex,1<<start_vertex);
    printf("\nMinimum cost of TSP starting from vertex %d = %d\n",start_vertex,min_cost);
}