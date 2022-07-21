# import re
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
#
# # url = 'http://py4e-data.dr-chuck.net/comments_42.html'
# url = 'http://py4e-data.dr-chuck.net/comments_228869.html'
#
# soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
# s = sum(int(td.text) for td in soup.select('td:last-child')[1:])
#
# print(s)
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0

for tag in tags:
    #look for <span>
    tag = str(tag)
    num = re.findall("[0-9]+",tag)
    num = int(num[0])
    sum = sum + num
print(sum)
