def knapsack(weights,values,capacity):
    n=len(weights)
    dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1]<=w:
                dp[i][w]=max(values[i-1]+dp[i-1][w-weights[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]
if __name__=="__main__":
    weights=[10,12,13,16]
    values=[7,8,9,6]
    capacity=25
    optimal_cost=knapsack(weights,values,capacity)
    print("\nOptimal Cost = ",optimal_cost)