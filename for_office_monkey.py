# coding=utf-8

import urllib2
import sys
import re
from bs4 import BeautifulSoup
# from bs4.diagnose import diagnose

def run_baby(save_file, url, decoder='gb2312'):
    reload(sys)
    sys.setdefaultencoding('utf-8')

    type = sys.getfilesystemencoding()

    response = urllib2.urlopen(url)

    with open('test.html', 'w+') as f:
        f.write(response.read().decode(decoder).encode(type))

    # test all parse
    # data = open('test.html').read()
    # diagnose(data)

    soup = BeautifulSoup(open('test.html'), 'html.parser')

    for tag in soup.find_all(re.compile('^p'), string=re.compile('^[0-9]')):
        if tag.string is not None:
            # print tag.string
            save_file.write(tag.string+'\n')

def main():
    save_file = open('test.txt', 'a+')
    raw_url = raw_input()

    for i in range(5):
        if i != 0:
            url = raw_url[0:42]+'_%s' %(i+1) + raw_url[42:]
        else:
            url = raw_url
        run_baby(save_file, url)

    save_file.close()

if __name__ == '__main__':

    main()
