#Copy Right Naufal Agler 2k20

class NB(object):
	def __init__(self):
		print('Success connected to NBCORP!')
	
	def getAppName(self, file=None):
		if file == 'androlite':
			return 'ANDROIDLITE\t2.15.0\tAndroid OS\t5.1.1'
		elif file == 'desktopmac':
			return 'DESKTOPMAC\t5.24.1\tMac_OS\t10.15.2'
		elif file == 'ios':
			return 'IOS\t10.16.2\tIphone 8\t10.3.3'
			
	def getChannel(self, file=None):
		if file == 'chanliff':
			return '1643727178'
		elif file == 'chanview':
			return '1643727178-0XPGAaRX'