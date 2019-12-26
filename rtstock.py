# -*- coding: utf-8 -*-

import urllib2
response = urllib2.urlopen('https://www.pythonforbeginners.com/')
print response.info()
html = response.read()
# do something
print html
response.close()  # best practice to close the file

