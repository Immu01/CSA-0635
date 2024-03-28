#include <stdio.h>
#include <stdbool.h>
#include <limits.h>
#define N 3
int cost_matrix[N][N]= 
{
    {4,7,5},
    {6,9,6},
    {5,8,8}
};
int min_cost=INT_MAX;
int min_assignment[N];
bool is_valid(int assignment[],int task) 
{
    for (int i=0;i<task;i++) 
    {
        if (assignment[i]==assignment[task])
            return false;
    }
    return true;
}
void explore_assignments(int assignment[],int task,int current_cost) 
{
    if (task==N) 
    {
        if (current_cost<min_cost) 
        {
            min_cost=current_cost;
            for (int i=0;i<N;i++)
                min_assignment[i]=assignment[i];
        }
        return;
    }
    for (int i=0;i<N;i++) 
    {
        if (is_valid(assignment,task)) 
        {
            int new_cost=current_cost+cost_matrix[task][i];
            if (new_cost<min_cost)
            {
                assignment[task]=i;
                explore_assignments(assignment,task+1,new_cost);
                assignment[task]=-1;
            }
        }
    }
}
void assignment_branch_and_bound() 
{
    int assignment[N],i;
    for (i=0;i<N;i++)
        assignment[i]=-1;
    explore_assignments(assignment,0,0);
}
int main() 
{
    assignment_branch_and_bound();
    printf("\nMinimum Cost = %d\n",min_cost);
    printf("\nOptimal Assignment = ");
    for (int i=0;i<N;i++)
        printf("(%d,%d)",i,min_assignment[i]);
    printf("\n");
}