#include <stdio.h>
void pascals(int rows) 
{
    int triangle[rows][rows],i,j,space;
    for (i=0;i<rows;i++) 
    {
        for (j=0;j<=i;j++) 
        {
            if (j==0||j==i)
                triangle[i][j]=1;
            else
                triangle[i][j]=triangle[i-1][j-1]+triangle[i-1][j];
        }
    }
    for (i=0;i<rows;i++) 
    {
        for (space=0;space<rows-i-1;space++) 
        {
            printf(" ");
        }
        for (j=0;j<=i;j++) 
        {
            printf("%d ",triangle[i][j]);
        }
        printf("\n");
    }
}
int main() 
{
    int row;
    printf("\nEnter the number of rows = ");
    scanf("%d",&row);
    pascals(row);
}