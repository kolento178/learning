import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
fout = open('liqiang.txt','w')
fout.write(response.read())
fout.close()


 # http://www.python.org/dev/peps/pep-0008/