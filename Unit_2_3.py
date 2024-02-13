def minimumCostEqualBaskets(basket1,basket2):
    total_cost=sum(basket1)+sum(basket2)
    n=len(basket1)
    min_cost=float('inf')
    for i in range(n):
        for j in range(n):
            swap_cost=min(basket1[i],basket2[j])
            new_total_cost=total_cost-basket1[i]-basket2[j]+swap_cost+swap_cost
            if new_total_cost<total_cost:
                total_cost=new_total_cost
                if total_cost<min_cost:
                    min_cost=total_cost
    basket1.sort()
    basket2.sort()
    if basket1!=basket2:
        return -1
    return min_cost
basket1=[1,3,5]
basket2=[2,4,6]
print("\nMinimum cost to make both baskets equal = ",minimumCostEqualBaskets(basket1,basket2))