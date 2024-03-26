def binomialcoeff(n,k):
    c=[[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                c[i][j]=1
            else:
                c[i][j]=c[i-1][j-1]+c[i-1][j]
    return c[n][k]
def main():
    n=7
    k=3
    print(binomialcoeff(n,k))
if __name__=="__main__":
    main()