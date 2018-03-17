import urllib.request
import urllib.parse
'''
url = 'http://www.pythonprogramming.net'
values = {'s':'basic','submit':'search'}

data=urllib.parse.urlencode(values)
data=data.encode('utf-8')
req=urllib.request.Request(url,data)
resp=urllib.request.urlopen(req)
respData=resp.read()

print(respData)
'''

try:
	x=urllib.request.urlopen('http://www.google.com/search?q=text')
	print(x.read())

except Exception as e:
	print(str(e))

try:
	url='http://www.google.com/search?q=test'
	headers={}
	headers = {"User-Agent":"Mozilla/4.0"}	
	req=urllib.request.Request(url,headers=headers)
	resp=urllib.request.urlopen(req)
	respData=resp.read()

	saveFile=open('withheaders.txt','w')
	saveFile.write(str(respData))
	saveFile.close()
except Exception as e:
	print(str(e))
