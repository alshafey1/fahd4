#Copy Right Naufal Agler 2k20

from time import sleep
import threading, requests, urllib.parse, time, json

HEADERS = {
	"android_lite": {
		"User-Agent": "LLA/2.12.0 SKR-H0 9",
		"X-Line-Application": "ANDROIDLITE\t2.16.0\tAndroid OS\t10;SECONDARY"
	},
	"clova_friends": {
		"User-Agent": "Line/5.5.1",
		"X-Line-Application": "CLOVAFRIENDS\t10.13.2\tCLOVABOOK\t1"
	},
	"android": {
		"User-Agent": "Line/10.6.2",
		"X-Line-Application": "ANDROID\t10.6.2\tAndroid OS\t10"
	},
	"ios_ipad": {
		"User-Agent": "Line/10.1.1",
		#"X-Line-Application": "IOSIPAD\t10.1.1\tiPhone 8\t11.2.5"
		"X-Line-Application": "IOSIPAD\t10.1.1\tiPhone X\t11.2.5"
	},
	"ios": {
		"User-Agent": "Line/10.1.1",
		"X-Line-Application": "IOS\t10.1.1\tiPhone 8\t11.2.5"
	},
    "chrome": {
        "User-Agent": "Line/2.4.0",
        "X-Line-Application": "CHROMEOS\t2.4.0\tChrome OS\t1",
        "X-Line-Carrier": "51089, 1-0",
        "x-lal": "en_EN"
    },
	"desktopwin": {
		"User-Agent": "Line/5.12.3",
		"X-Line-Application": "DESKTOPWIN\t5.21.3\tWindows\t10",
	},
	"desktopmac": {
        "User-Agent": "Line/2.4.0",
        "X-Line-Application": "DESKTOPMAC6.0.3MAC10.14.1",
        "X-Line-Carrier": "51089, 1-0",
        "x-lal": "en_EN"
	}
}

class NB(object):
	def __init__(self):
		print('Success connected to NBCORP!')
		
	def getSquad(self):
		return 'NOOB CODER™'
	
	def getAppName(self, file=None):
		if file == 'androlite':
			return 'ANDROIDLITE\t2.16.0\tAndroid OS\t10;SECONDARY'
		elif file == 'desktopmac':
			return 'DESKTOPMAC6.0.3MAC10.14.1'
		elif file == 'iosipad':
			return 'IOSIPAD\t10.1.1\tiPhone 8\t11.2.5'
		elif file == 'ios':
			return 'IOS\t10.16.2\tIphone 8\t10.3.3'
			
	def getChannel(self, file=None):
		if file == 'chanliff':
			return '1643727178'
		elif file == 'chanview':
			return '1643727178-0XPGAaRX'
			
	def getFlex(self, flex=None):
		xx = ['withBackground', 'noBackground', 'kilo', 'mega']
		if flex == 'change flex1':
			return xx[0]
		elif flex == 'change flex2':
			return xx[1]
		elif flex == 'change footer1':
			return xx[0]
		elif flex == 'change footer2':
			return xx[1]
		elif flex == 'bubble kilo':
			return xx[2]
		elif flex == 'bubble mega':
			return xx[3]
			
	def API_URL(self):
		return "https://api.lrtt.icu/secondaryQrCodeLogin.do"
		
	def parseLog(self, loginInfo):
		return (loginInfo["token"], loginInfo["certificate"])
		
	def sendTemplate(self, noobcoder, to, data):
		xyz = LiffChatContext(to)
		xyzz = LiffContext(chat=xyz)
		view = LiffViewRequest(self.getChannel('chanview'), xyzz)
		token = noobcoder.liff.issueLiffView(view)
		url = 'https://api.line.me/message/v3/share'
		headers = {
		    'Content-Type': 'application/json',
		    'Authorization': 'Bearer %s' % token.accessToken
		}
		data = {"messages":[data]}
		requests.post(url, headers=headers, data=json.dumps(data))
	
	def loginsb(self, to, noobcoder, premium, msg, header, certificate=""):
		if msg._from in premium["myService"]:
			user = premium["myService"][msg._from]
			try:
				def frzky():
					contact = noobcoder.getContact(msg._from)
					LINKFOTO = "https://os.line.naver.jp/os/p/" + msg._from
					try:
						with open(f'{msg._from}.txt',"r") as a: toket = a.read()
						sleep(1)
						print(f'{toket} : Loggin ..')
						assert header in HEADERS, "invaild header"
						resp = requests.post(self.API_URL() + "/login?" + urllib.parse.urlencode({"custom_headers": HEADERS[header], "certificate": toket}))
						res = resp.json()
						if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
						#noobcoder.sendMessage(to, "Login URL: %s" % (res["url"]))
						data={"type":"flex","altText":"NOOB CODER™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                          }
                        ],
                        "width": "60px",
                        "height": "60px",
                        "borderWidth": "2px",
                        "borderColor": "#ffffff",
                        "cornerRadius": "100px"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Hello , {}".format(user),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True
                          },
                          {
                            "type": "text",
                            "text": "CLICK HERE FOR LOGIN",
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True,
                            "action": {
                                "type": "uri",
                                "uri": "{}".format(res["url"])
                            }
                          }
                        ],
                        "margin": "lg"
                      }
                    ]
                  }
        ],
        "paddingAll": "13px",
        "backgroundColor": "#000000",
        "cornerRadius": "2px",
        "margin": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}}
						self.sendTemplate(noobcoder, to, data)
						while "token" not in res:
							resp = requests.post(self.API_URL() + res["callback"])
							res = resp.json()
							if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
					except:
						assert header in HEADERS, "invaild header"
						resp = requests.post(self.API_URL() + "/login?" + urllib.parse.urlencode({"custom_headers": HEADERS[header], "certificate": certificate}))
						res = resp.json()
						if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
						#noobcoder.sendMessage(to, "Login URL: %s" % (res["url"]))
						data={"type":"flex","altText":"NOOB CODER™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                          }
                        ],
                        "width": "60px",
                        "height": "60px",
                        "borderWidth": "2px",
                        "borderColor": "#ffffff",
                        "cornerRadius": "100px"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Hello , {}".format(user),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True
                          },
                          {
                            "type": "text",
                            "text": "CLICK HERE FOR LOGIN",
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True,
                            "action": {
                                "type": "uri",
                                "uri": "{}".format(result["result"]["qr_link"])
                            }
                          }
                        ],
                        "margin": "lg"
                      }
                    ]
                  }
        ],
        "paddingAll": "13px",
        "backgroundColor": "#000000",
        "cornerRadius": "2px",
        "margin": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}}
						self.sendTemplate(noobcoder, to, data)
						while "token" not in res:
							resp = requests.post(self.API_URL() + res["callback"])
							res = resp.json()
							if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
							if "pin" in res: noobcoder.sendMessage(to, "Input PIN: %s" % (res["pin"]))
							token, cert = self.parseLog(res)
							with open(f'{msg._from}.txt',"w") as b: token = b.write(cert)
							sleep(1)
							print(f'{token} : Saved to data..')
						if msg._from not in premium['listLogin']:
							premium['listLogin'][msg._from] =  '%s' % user
							token, cert = self.parseLog(res)
							isi = "{}".format(token)
							os.system('cp -r percobaan {}'.format(user))
							os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
							os.system('screen -dmS {}'.format(user))
							os.system('screen -r {} -X stuff "cd {} && python3 staff.py \n"'.format(user, user))
							#noobcoder.sendMessage(to, "< Notification >\n\nFile : {}\nStatus : Login Success".format(user))
							data={"type":"flex","altText":"NOOB CODER™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                          }
                        ],
                        "width": "60px",
                        "height": "60px",
                        "borderWidth": "2px",
                        "borderColor": "#ffffff",
                        "cornerRadius": "100px"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "File : {}".format(user),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True
                          },
                          {
                            "type": "text",
                            "text": "SUCESS TO LOGIN",
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True
                          }
                        ],
                        "margin": "lg"
                      }
                    ]
                  }
        ],
        "paddingAll": "13px",
        "backgroundColor": "#000000",
        "cornerRadius": "2px",
        "margin": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}}
							self.sendTemplate(noobcoder, to, data)
					else:
						noobcoder.sendMention(msg.to, '「 Req Login 」\n• Status : Failed\n• User: @!',' ', [msg._from])
				thread = threading.Thread(target=frzky)
				thread.daemon = True
				thread.start()
			except:
				noobcoder.sendMention(to, '「 Reg Login 」\n• Status : Failed\n •User: @!',' ', [msg._from])