import sys
def sum(freq,i,j):
    s=0
    for k in range(i,j+1):
        s+=freq[k]
    return s
def obst(keys,freq,n):
    cost=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        cost[i][i]=freq[i]
    for L in range(2,n+1):
        for i in range(n-L+1):
            j=i+L-1
            cost[i][j]=sys.maxsize
            for r in range(i,j+1):
                c = ((cost[i][r-1] if r>i else 0)+
                     (cost[r+1][j] if r<j else 0)+
                     sum(freq,i,j))
                if c<cost[i][j]:
                    cost[i][j]=c
    return cost[0][n-1]
def main():
    keys=[1,2,3,4]
    freq=[0.2,0.1,0.2,0.3]
    n=len(keys)
    print("Cost of OBST is",obst(keys,freq,n))
if __name__=="__main__":
    main()