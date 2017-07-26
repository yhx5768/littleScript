import urllib2
import hashlib
import time

url = 'https://bandwagonhost.com/cart.php'
test_url = 'http://www.soarx.cc/'
headers = {
            'authority' : 'bandwagonhost.com',
           'path' : '/cart.php',
           'referer' : 'https://bandwagonhost.com/clientarea.php',
           'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36'}

request = urllib2.Request(test_url)
for header in headers:
    request.add_header(header, headers[header])
response = urllib2.urlopen(request)
# print response.headers.dict
page = response.read()
hash_page = hashlib.md5(page)

time.sleep(60)

second_request = urllib2.Request(test_url)
second_response = urllib2.urlopen(second_request)
second_page = second_response.read()
hash_page2 = hashlib.md5(second_page)

if (hash_page.hexdigest() == hash_page2.hexdigest()):
    print 'no change'
else:
    print 'changed'
