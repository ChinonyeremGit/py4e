# import re
# hand = open('short')
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
#     if len(x) > 0:
#         print(x)
# import re
# hand = open('zx.txt')
# lst = list()
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('New Revision: ([0-9]+)', line)
#     if len(x) > 0:
#         num = int(x[0])
#         lst.append(num)
# ave = sum(lst)/len(lst)
# print(int(ave))
# import re
# hand = open('regex_sum_1427517.txt')
# lst = list()
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('([0-9]+)', line)
#     if len(x) > 0:
#         num = [int(a) for a in x]
#         for i in num:
#             lst.append(i)
# print(sum(lst))
# import socket
# url = input('enter url: ').split('/')
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((url[2], 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# count = 0
# while True:
#     data = mysock.recv(3000)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#     datas = data.decode()
#     num = datas.replace(' ','')
#     print(len(num))
#
# mysock.close()
# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# while True:
#     data = fhand.read()
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#     datas = data.decode()
#     num = datas.replace(' ','')
#     print(len(num))
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

