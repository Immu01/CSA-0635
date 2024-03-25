def find_min_max(nums):
    min_num=nums[0]
    max_num=nums[0]
    for num in nums:
        if num<min_num:
            min_num=num
        if num>max_num:
            max_num=num
    return min_num,max_num
def main():
    numbers=list(map(int,input("\nEnter the numbers :").split()))
    min_num,max_num=find_min_max(numbers)
    print(f"\nsmallest number = {min_num}")
    print(f"\nlargest number = {max_num}")
if __name__=="__main__":
    main()