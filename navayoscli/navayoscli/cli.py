import click
import requests
from PIL import Image
from StringIO import StringIO
from bs4 import BeautifulSoup

@click.command()
@click.argument('name', required=False)
def main(name):
    	URL='http://math.sci.ubu.ac.th/staffs/academic'
	html=requests.get(URL)
	b=BeautifulSoup(html.content,'html.parser')
	search=b.find_all('div',{'class','col-md-3 news-item'})
	#chk = b.find_all('search',{'class','thumb'})
	
	for x in range(len(search)):
		
		S=search[x].img['alt']
		print(format(S))
		if format(name)==format(S):
			url=search[x].img['src']
			break	
		
	req=requests.get(url)
    	img = Image.open(StringIO(req.content))
    	img.show()
