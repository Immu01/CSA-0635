def knapsack(items,capacity):
    items.sort(key=lambda x:x[1]/x[2],reverse=True)
    total_value=0
    knapsack=[]
    for item in items:
        if capacity>=item[2]:
            knapsack.append(item)
            total_value+=item[1]
            capacity-=item[2]
        else:
            fraction=capacity/item[2]
            knapsack.append((item[0],item[1]*fraction,item[2]*fraction))
            total_value+=item[1]*fraction
            break
    return knapsack,total_value
items=[("item1",60,10),("item2",100,20),("item3",120,30)]
capacity=50
selected_items,total_value=knapsack(items,capacity)
print("\nSelected items = ",selected_items)
print("\nTotal value = ",total_value)