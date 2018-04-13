from templates import *
from simpleqrgenerator import SimpleQRGenerator

def get_info(template,fn,ln,addr,contact,github,linkedin):
		"""
			This is specific method for the AboutMe Template. The predefined fields are set.
			in this method.
		"""
		data = template.format(fn,ln,addr,contact,github,linkedin)
		return data    
	
if __name__ == "__main__":
    image = SimpleQRGenerator()
    
    image.create_file("test_me",get_info(aboutme_template,"Test","Me","","+91 99XXX XXXXX","https://github.com/testme","https://www.linkedin.com/in/test-me/"))
		