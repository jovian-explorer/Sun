from bs4 import BeautifulSoup


# Reading the data inside the xml
# file to a variable under the name
# data

url = '/home/dev/Sun/zds_olrconfig.xml'
with open(url, 'r') as f:
	data = f.read()
	print(data)
