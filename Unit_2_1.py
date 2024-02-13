def shipWithinDays(weights, days):
    min_capacity=max(weights)
    max_capacity=sum(weights)
    while min_capacity<max_capacity:
        mid_capacity=(min_capacity+max_capacity)//2
        current_load=0
        required_days=1
        for weight in weights:
            if current_load+weight>mid_capacity:
                required_days+=1
                current_load=0
            current_load+=weight
        if required_days>days:
            min_capacity=mid_capacity+1
        else:
            max_capacity=mid_capacity
    return min_capacity
weights=[1,2,3,4,5,6,7,8,9,10]
days=5
print("\nLeast weight capacity = ",shipWithinDays(weights,days))