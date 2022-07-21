# celsius =int(input("enter a temperature in celsius: \n"))
# fah = 1.8 * celsius + 32
# print(str(celsius) + " deg celsius equals " + str(fah) + " deg fahrenheit.")

# print("pay calculator")
# try:
#   hour = float(input("enter the hours worked: "))
#   rate = float(input("enter the rate: "))
#
#   if hour > 40:
#      pay = (hour * rate + (1.5 * (hour - 40) * rate))
#   else:
#       pay = hour * rate
#   print(pay)
# except:
#     print("enter numeric values only")

# try:
#     n = float(input("enter a number within 0.0 - 1.0: "))
#     if 0.9 <= n <= 1.0:
#         print("A")
#     elif 0.8 <= n < 0.9:
#         print("B")
#     elif 0.7 <= n < 0.8:
#         print("C")
#     elif 0.6 <= n < 0.7:
#         print("D")
#     elif 0.0 <= n < 0.6:
#         print("F")
#     else:
#         print("Bad score")
# except:
#     print("numerical values only")

# name = input("enter your name: ")
# def print_twice(bruce):
#     bruce = "you're welcome " + name
#     print(bruce)
#     print(bruce)
# print_twice("sam")

# n = float(input("enter a number between 0.0 to 1.0: "))
# def compute_score(n):
#     if 0.9 <= n <= 1.0:
#         return "A"
#     elif 0.8 <= n < 0.9:
#         return "B"
#     elif 0.7 <= n < 0.8:
#         return "C"
#     elif 0.6 <= n < 0.7:
#         return "D"
#     elif 0.0 <= n < 0.6:
#         return "F"
#     else:
#         return "Bad score"
# print(compute_score(n))

# def func(x):
#     print(x)
# func(10)
# func(20)
# def stuff():
#     print("hello")
#     return
# stuff()

# count = 0
# total = 0
# while True:
#     n = input("enter a num: ")
#     if str(n).lower() == "done":
#         break
#     try:
#         total = total + int(n)
#         count = count + 1
#     except:
#         print("bad num")
#         continue
# try:
#     ave = total / count
#     print(total, count, ave)
# except:
#     print("hmmm... no work yet.\nThank You")

# m = []
# while True:
#     n = input("enter a num: ")
#     if str(n).lower() == "done":
#         break
#     try:
#         m.append(int(n))
#         k = max(m)
#         l = min(m)
#     except:
#         print("bad num")
#         continue
# try:
#     print("max", k, "min", l)
# except:
#     print("Done!")

# fruit = "banana"
# index = -1
# while index > -len(fruit) - 1:
#     letter = fruit[index]
#     print(letter)
#     index -= 1
# m = fruit.count("a")
# print(m)

# str = 'X-DSPAM-Confidence:0.8475'
# fin = str.find(":")
# print(float(str[fin + 1:]))
# print(str)

# hand = input("enter a file name: ")
# fhand = open(hand, "r")
# for line in fhand:
#     line = line.upper().rstrip()
#     print(line)
# '''
# t = ['a', 'b', 'c', 'd']
# def middle(a):
#     return a[1:len(a)-1]
# def middl(b):
#     return b[0] + b[-1]
#
# print(middle(t))
# print(list(middl(t)))

# fhand = input("enter a file: ").strip()
# ffhanbd = open(fhand, 'r')
# for line in ffhanbd:
#     words = line.split()
# if len(words) == 0: continue
# try:
#     if words[0].lower() != 'from': continue
#     print(words[2])
# except: continue

# if len(words) == 0 or words[0].lower() != 'from': continue
# print(words[2])
# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     #line = line.rstrip()
#     line = line.split()
#     for word in line:
#         if word not in lst:
#             lst.append(word)
# lst.sort()
# print(lst)


# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# su = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     words = line.split()
#     count = count +1
#     su = float(words[1]) + su
# ave = su / count
# print('Average spam confidence:', ave)
# fhame = open("words.txt", 'r')
# di = dict()
# for line in fhame:
#     words = line.rstrip()
#     for word in words.split():
#         if word not in di:
#             di[word] = 1
#         else: di[word] += 1
# print(di)
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#   if counts[key] > 10 :
#    print(key, counts[key])
# fhand = open(input("enter a file:"))
# di = dict()
# for line in fhand:
#     line = line.split()
#     if len(line) < 1 or line[0].lower() != "from": continue
#     val = line[2]
#     di[val] = di.get(val, 0) + 1
# print(di)

# fhand = open(input("enter a file:"))
# di = dict()
# high = None
# word = None
# for line in fhand:
#     line = line.split()
#     if len(line) < 1 or line[0].lower() != "from": continue
#     val = line[1]
#     di[val] = di.get(val, 0) + 1
# for wor, num in list(di.items()):
#     if high is None or num > high:
#         high = num
#         word = wor
# print(word, high)
#
# fhand = open(input("enter a file: "))
# di = dict()
# li = []
# for line in fhand:
#     line = line.split()
#     if len(line) < 1 or line[0].lower() != "from": continue
#     add = line[1]
#     li.append(add)
# for nec in li:
#     nec = nec.split('@')
#     req = nec[1]
#     di[req] = di.get(req, 0) +1
# print(di)

# fhand = open(input("enter a file: "))
# di = {}
# for line in fhand:
#     line = line.split()
#     if len(line) < 1 or line[0].lower() != "from": continue
#     fresh = line[5].split(':')
#     hour = fresh[0]
#     di[hour] = di.get(hour, 0) + 1
# for hou, fre in sorted(list(di.items())):
#     print(hou, fre)
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    print(name)
    print(line)
    scores = list(map(float, line))
    print(scores)
    student_marks[name] = scores
print(student_marks)
