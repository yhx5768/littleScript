import urllib2

request = urllib2.Request('http://www.soarx.cc/index.html')
opener = urllib2.build_opener()
firstdatastream = opener.open(request)
firstdatastream.add_header('If-Modified-Since',
            firstdatastream.headers.get('Last-Modified'))
seconddatasteam = opener.open(request)
