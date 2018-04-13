"""

This program is the simple example of Google Image Chart API use case for QR code generation

"""

import urllib
import urllib.request
import urllib.parse
from urlinfo import *

class SimpleQRGenerator:

	def __init__(self):
		self.root_url = root_url
		self.size = querychs
		self.type = querycht
		self.link = querychl
	
	def create_query(self,imgsize,imglink,encoding='UTF-8'):
		"""
			This method is important for applying the parameters to the Google chart API.
		"""
		querydict = {}
		querydict[self.size]=imgsize
		querydict[self.type]='qr'
		querydict[self.link]=imglink
		return querydict
	
	def get_url_content(self,imgsize,imglink):
		"""
			Here is the place the actual Google Image Chart url is invoked.
		"""
		query = self.create_query(imgsize,imglink)
		url = self.root_url + urllib.parse.urlencode(query)
		content = urllib.request.urlopen(url)
		return content.read()
		
	def create_file(self, file_name, data, image_pixel=200, extn = "png"):
		"""
			This method created the qr file with gien name and extension and specified size.
			The file is generated in local directory.
		"""
		fil = open(file_name+"."+extn,"wb")
		fil.write(self.get_url_content(str(image_pixel)+"x"+str(image_pixel),data))
		fil.close()

		
		
	
	