def digit_sum(num):
    digits_sum=0
    while num>0:
        digit=num%10
        digits_sum+=digit
        num//=10
    return digits_sum
num=int(input("\nEnter a number = "))
print("Sum of digits = ",digit_sum(num))