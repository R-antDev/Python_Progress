# 5. Write a program to find the smallest of three numbers.

print('Find out the smallest number.')

first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third number: '))

# using conditions

"""if first_num < second_num:
    smallest_num = first_num
else:
    smallest_num = second_num

if third_num < smallest_num:
    smallest_num = third_num

print(smallest_num)"""

if first_num < second_num and first_num < third_num:
    print(f'The smallest number is first number, which is :{first_num}')
elif second_num < first_num and second_num < third_num:
    print(f'The smallest number is second number, which is :{second_num}')
else:
    print(f'The smallest number is third number, which is :{third_num}')
