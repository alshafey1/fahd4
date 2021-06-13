#Copy Right Naufal Agler 2k20

class NB(object):
	def __init__(self):
		print('Success connected to NBCORP!')
	
	def getAppName(self, file=None):
		if file == 'androlite':
			return 'ANDROIDLITE\t2.15.0\tAndroid OS\t5.1.1'
		elif file == 'desktopmac':
			return 'DESKTOPMAC\t6.4.0\tMAC\t10.14.1'
		elif file == 'iosipad':
			return 'IOSIPAD\t10.1.1\tiPhone 8\t11.2.5'
		elif file == 'ios':
			return 'IOS\t10.16.2\tIphone 8\t10.3.3'
			
	def getChannel(self, file=None):
		if file == 'chanliff':
			return '1655688537'
		elif file == 'chanview':
			return '1655688537-GydYA2yn'
			
	def getFlex(self, flex=None):
		xx = ['withBackground', 'withBackground1', 'noBackground','noBackground1', 'kilo', 'mega', 'footer3', 'flex3']
		if flex == 'change flex1':
			return xx[0]
		elif flex == 'change flex2':
			return xx[1]
		elif flex == 'change flex3':
			return xx[7]
		elif flex == 'change footer1':
			return xx[0]
	    
		elif flex == 'change footer2':
			return xx[1]
		elif flex == 'bubble kilo':
			return xx[2]
		elif flex == 'change footer3':
			return xx[6]

