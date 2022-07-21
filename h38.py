ten_things = "Apples Oranges Crows Telephonr Light Sugar"

print("Wait there are not 10 things in that list. let's fix that.")

stuff = ten_things.split()
more_stuff = ["Day", "Night", "song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
#doing things to list
# def nextSquare():
#     i = 1
#
#     # An Infinite loop to generate squares
#     while True:
#         yield i*i
#         i += 1 # Next execution resumes
#                 # from this point
#
# # Driver code
# for num in nextSquare():
#     if num > 100:
#         break
#     print(num)
