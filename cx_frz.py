import urllib.request
import urllib.parse
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
