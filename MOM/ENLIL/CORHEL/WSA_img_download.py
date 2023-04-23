import csv,os
import itertools
from simplified_scrapy import Spider, SimplifiedMain, utils
class ImageSpider(Spider):
  name = 'images'
  start_urls = []
  def __init__(self):
      with open('/home/dev/Desktop/ENLIL/CORHEL/URL_WSA_anim.csv') as csvDataFile:
          csvReader = csv.reader(csvDataFile)
          for elem in itertools.islice(csvReader, 0, 170):
              self.start_urls.append(elem[0])
      Spider.__init__(self,self.name) # Necessary
      if(not os.path.exists('images/')):
          os.mkdir('images/')
          
  def afterResponse(self, response, url, error=None, extra=None):
    try:
        utils.saveResponseAsFile(response,'images/','image')
    except Exception as err:
        print (err)
    return None 

SimplifiedMain.startThread(ImageSpider()) # Start download
