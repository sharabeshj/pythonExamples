import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time


try:
	url='http://www.primevideo.com'
	headers = {"User-Agent":"Mozilla/4.0"}	
	req = urllib.request.Request(url,headers=headers)
	resp = urllib.request.urlopen(req)
	respData = resp.read()
	soup = BeautifulSoup(respData,'lxml')

	links = soup.find_all('img', src=True)
	for link in links:
		timeStamp = time.asctime()
		saveFile=open('%s.jpg'%timeStamp,'wb')
		link = link["src"].split("src=")[-1]
		downloadImg = urllib.request.urlopen(link)
		saveFile.write(downloadImg.read())
		saveFile.close()
except Exception as e:
	print(str(e))