i = 0
numbers = []

while i  < 6:
    print(f'At the top i is {i}')
    numbers.append(i)

    i +=1
    print('Numbers now: ', numbers)
    print(f' at the bottom i is {i}')


print('The numbers: ')

for num in numbers:
    print(num)

# while loops



def range(nums, increment):
    i = 0
    numbers = []
    while i  < int(nums):
        print(f'At the top i is {i}')
        numbers.append(i)

        i += int(increment)
        print('Numbers now: ', numbers)
        print(f' at the bottom i is {i}')
    print('The numbers: ')

    for num in numbers:
        print(num)

range(input("enter number: "), input('Enter increament: '))
