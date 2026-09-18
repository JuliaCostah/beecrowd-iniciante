def verify_odd_or_even(numeros):
    
    for num in numeros:
        if num == 0:
            print('NULL')
        elif num % 2 == 0 and num > 0:
            print('EVEN POSITIVE')
        elif num % 2 == 0 and num < 0:
            print('EVEN NEGATIVE')
        elif num % 2 != 0 and num > 0:
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')

n = int(input())
nums = []
for i in range(n):
    choice = int(input())
    nums.append(choice)

verify_odd_or_even(nums)