# Take N as input and calculate the sum the of 1 + 4 + 7 + 10 + 13 etc

N = int(input('Enter the value of N: '))

sumOfN = 0
i = 1
while i <= N:
    sumOfN += i
    i += 3
print(f'The sum of N is: {sumOfN}')
