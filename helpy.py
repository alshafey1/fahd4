# HELPER
#  ☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜
# ☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜
from linepy import *
from akad.ttypes import Message
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from Jeckybot.thrift.protocol import TCompactProtocol
from Jeckybot.thrift.transport import THttpClient
from Jeckybot.ttypes import LoginRequest
from Naked.toolshed.shell import execute_js
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
import platform
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
from threading import Thread, activeCount
from nbcorp import NB
import LineService
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import time, random, sys, json, null, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
nbcorp = NB()
noobcoder = LINE("ahmedalshafey123456@gmail.com","Agalshafey91",appName=nbcorp.getAppName('chrome'))
Channel(noobcoder, nbcorp.getChannel('chanliff')).getChannelResult().channelAccessToken
#=======================================================
waitOpen = codecs.open("settings/wait.json","r","utf-8")
settingsOpen = codecs.open("settings/temp.json","r","utf-8")
premiumOpen = codecs.open("settings/kontol.json","r","utf-8")
betaOpen = codecs.open("settings/ajs.json","r","utf-8")
javaOpen = codecs.open("settings/java.json","r","utf-8")
#=====================================================================
#=====================================================================
noobcoderProfile = noobcoder.getProfile()
noobcoderSettings = noobcoder.getSettings()
noobcoderPoll = OEPoll(noobcoder)
noobcoderMID = noobcoder.getProfile().mid
#=====================================================================
loop = asyncio.get_event_loop()
myAdmin = ["u29c4bb607fb8476b1ee77d0f1f7f14a2","ue553118bead484cf8a529217056f0689","ufe4acfc1c51725d653385efbd331b9ed","u081b18974bf84d72b13aad6eae865f9d"]
botStart = time.time()
msg_dict = {}
temp_flood = {}
steals = []
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
premium = json.load(premiumOpen)
java = json.load(javaOpen)
betamaker = json.load(betaOpen)

hoho = {
    "savefile": False,
    "namefile": "",
}

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

read = { 
    "readMember": {},
    "readPoint": {}
}

wmin = {
    "wMessage": False,
    "textnya": "Enjoying in this group",
}

lvin = {
    "lMessage": False,
    "textnya": "See u next time",
}

tailah = {
    "siderTemp": {},
    "siderTemp2": {},
    "siderTemp3": {},
    "siderTemp4": {},
    "siderPesan": "up call my frinds",
}

setbot = {
    "background": "#000000",
    "text": "#ffffff",
    "separator": "#ffffff"
}

gwcool = {
    "squad": "☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜",
}

javascript = {
    "jskick": "bypass",
    "jskick1": "cleanse",
    "cancels": "cancel",
}

peler = { 
    "receivercount": 0,
    "sendcount": 0
}
#=====================================================================
#=====================================================================
settings["myProfile"]["displayName"] = noobcoderProfile.displayName
settings["myProfile"]["statusMessage"] = noobcoderProfile.statusMessage
settings["myProfile"]["pictureStatus"] = noobcoderProfile.pictureStatus
cont = noobcoder.getContact(noobcoderMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = noobcoder.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
#=====================================================================
#=====================================================================
with open("noobcoder/temp.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("noobcoder/wait.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
    
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
        "X-Line-Application": "DESKTOPWIN\t5.21.3\tWindows\t10"
    },
    "desktopmac": {
        "User-Agent": "Line/2.4.0",
        "X-Line-Application": "DESKTOPMAC6.0.3MAC10.14.1",
        "X-Line-Carrier": "51089, 1-0",
        "x-lal": "en_EN"
	}
    
}
def inSteals(from_):
    global steals
    if from_ in steals:
        return True
    return False
def appendSteals(from_):
    try:
        global steals
        if from_ in steals:
            return
        return steals.append(from_)
    except:
        return False
def clearSteals():
    global steals
    steals = []
    return
def API_URL():
    return "https://api.lrtt.icu/secondaryQrCodeLogin.do"
    
def parseLog(loginInfo):
    return (loginInfo["token"], loginInfo["certificate"])
def loginajs(to, msg, header, certificate=""):
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
                    resp = requests.post(API_URL() + "/login?" + urllib.parse.urlencode({"custom_headers": HEADERS[header], "certificate": toket}))
                    print(resp.text)
                    res = resp.json()
                    if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                    noobcoder.sendMessage(to, "Login URL: %s" % (res["url"]))
                    while "token" not in res:
                        resp = requests.post(API_URL() + res["callback"])
                        res = resp.json()
                        if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                except:
                    assert header in HEADERS, "invaild header"
                    resp = requests.post(API_URL() + "/login?" + urllib.parse.urlencode({"custom_headers": HEADERS[header], "certificate": certificate}))
                    res = resp.json()
                    if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                    noobcoder.sendMessage(to, "Login URL: %s" % (res["url"]))
                    while "token" not in res:
                        resp = requests.post(API_URL() + res["callback"])
                        res = resp.json()
                        if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                        if "pin" in res: noobcoder.sendMessage(to, "Input PIN: %s" % (res["pin"]))
                    token, cert = parseLog(res)
                    with open(f'{msg._from}.txt',"w") as b: token = b.write(cert)
                    sleep(1)
                    print(f'{token} : Saved to data..')
                if msg._from not in premium['listLogin']:
                    premium['listLogin'][msg._from] =  '%s' % user
                    token, cert = parseLog(res)
                    isi = "{}".format(token)
                    os.system('cp -r percobaan {}'.format(user))
                    os.system('cd {} && echo -n "{}" > tokenajs.txt'.format(user, isi))
                    os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                    os.system('screen -dmS {}'.format(user))
                    os.system('screen -r {} -X stuff "cd {} && python3 hamzhajs.py \n"'.format(user, user))
                    noobcoder.sendMessage(to, "< Notification >\n\nFile : {}\nStatus : Login Success".format(user))
                else:
                    noobcoder.sendMention(msg.to, '「 Req Login 」\n• Status : Failed\n• User: @!',' ', [msg._from])
            thread = threading.Thread(target=frzky)
            thread.daemon = True
            thread.start()
        except:
            noobcoder.sendMention(to, '「 Reg Login 」\n• Status : Failed\n •User: @!',' ', [msg._from])    
def loginsb(to, msg, header, ajs=None, certificate="", file=None):
    if msg._from in premium["myService"]:
        user = premium["myService"][msg._from]
        try:
            def frzky():
                contact = noobcoder.getContact(msg._from)
                LINKFOTO = "https://ga2.line.naver.jp/ti/p/~jekdaniel." + msg._from
                #try:
                if 1 == 2:
                    with open(f'{msg._from}.txt',"r") as a: toket = a.read()
                    sleep(1)
                    print(f'{toket} : Loggin ..')
                    assert header in HEADERS, "invaild header"
                    resp = requests.post(API_URL() + "/login?" + urllib.parse.urlencode({"custom_headers": HEADERS[header], "certificate": toket}))
                    res = resp.json()
                    if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                    noobcoder.sendMessage(to, "Login URL: %s" % (res["url"]))
                    
                    
                    data={"type":"flex","altText":"LOGIN SB\n"+res["url"],"contents": {
        "direction": "ltr",
        "hero": {
            "backgroundColor": "#00000Cac",
            "borderColor": "#ffffff",
            "borderWidth": "2px",
            "contents": [
                {
                    "aspectMode": "cover",
                    "position": "absolute",
                    "size": "full",
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
                },
                {
                    "backgroundColor": "#00000Cac",
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "size": "full",
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                        },
                        {
                            "contents": [
                                {
                                    "type": "separator"
                                }
                            ],
                            "layout": "vertical",
                            "type": "box"
                        }
                    ],
                    "layout": "vertical",
                    "position": "absolute",
                    "type": "box"
                },
                {
                    "backgroundColor": "#00000Cac",
                    "contents": [
                        {
                            "text": " ",
                            "type": "text"
                        }
                    ],
                    "height": "200px",
                    "layout": "vertical",
                    "position": "absolute",
                    "type": "box",
                    "width": "1000px"
                },
                {
                    "borderColor": "#ffffff",
                    "borderWidth": "3px",
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "size": "full",
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                        }
                    ],
                    "cornerRadius": "100px",
                    "height": "60px",
                    "layout": "vertical",
                    "offsetStart": "10px",
                    "offsetTop": "30px",
                    "spacing": "xl",
                    "type": "box",
                    "width": "60px"
                },
                {
                    "contents": [
                        {
                            "action": {
                                "label": "☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜",
                                "type": "uri",
                                "uri": "{}".format(res["url"])
                            },
                            "style": "secondary",
                            "type": "button"
                        }
                    ],
                    "layout": "vertical",
                    "offsetBottom": "25px",
                    "offsetStart": "80px",
                    "type": "box"
                },
                {
                    "type": "separator"
                },
                {
                    "contents": [
                        {
                            "align": "center",
                            "color": "#ffffff",
                            "text": "Hello , {}".format(contact.displayName),
                            "type": "text",
                            "wrap": True, 
                        }
                    ],
                    "layout": "vertical",
                    "type": "box"
                }
            ],
            "cornerRadius": "16px",
            "layout": "vertical",
            "type": "box"
        },
        "size": "mega",
        "styles": {
            "header": {
                "backgroundColor": "#00000Cac"
            }
        },
        "type": "bubble"
    },
    "type": "flex"
}
                    sendTemplate(to, data)
                    while "token" not in res:
                        #resp = requests.post(API_URL() + res["callback"])
                        #res = resp.json()
                        if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                #except:
                else:
                    assert header in HEADERS, "invaild header"
                    apikey = "HkcxIBZefS"
                    resp = requests.get("https://fgmlogin.cf/qrv2/getlink.php?header=desktopmac&apikey="+apikey)
                    #resp = requests.post(API_URL() + "/login?" + urllib.parse.urlencode({"custom_headers": HEADERS[header], "certificate": certificate}))
                    res = resp.json()
                    if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                    noobcoder.sendMessage(to, "Login URL: %s" % (res["get_link"]))
                    data={"type":"flex","altText":"LOGIN SB\n"+res["get_link"],"contents": {
        "direction": "ltr",
        "hero": {
            "backgroundColor": "#00000Cac",
            "borderColor": "#ffffff",
            "borderWidth": "2px",
            "contents": [
                {
                    "aspectMode": "cover",
                    "position": "absolute",
                    "size": "full",
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
                },
                {
                    "backgroundColor": "#00000Cac",
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "size": "full",
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                        },
                        {
                            "contents": [
                                {
                                    "type": "separator"
                                }
                            ],
                            "layout": "vertical",
                            "type": "box"
                        }
                    ],
                    "layout": "vertical",
                    "position": "absolute",
                    "type": "box"
                },
                {
                    "backgroundColor": "#00000Cac",
                    "contents": [
                        {
                            "text": " ",
                            "type": "text"
                        }
                    ],
                    "height": "200px",
                    "layout": "vertical",
                    "position": "absolute",
                    "type": "box",
                    "width": "1000px"
                },
                {
                    "borderColor": "#ffffff",
                    "borderWidth": "3px",
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "size": "full",
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                        }
                    ],
                    "cornerRadius": "100px",
                    "height": "60px",
                    "layout": "vertical",
                    "offsetStart": "10px",
                    "offsetTop": "30px",
                    "spacing": "xl",
                    "type": "box",
                    "width": "60px"
                },
                {
                    "contents": [
                        {
                            "action": {
                                "label": "☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜",
                                "type": "uri",
                                "uri": "{}".format(res["get_link"])
                            },
                            "style": "secondary",
                            "type": "button"
                        }
                    ],
                    "layout": "vertical",
                    "offsetBottom": "25px",
                    "offsetStart": "80px",
                    "type": "box"
                },
                {
                    "type": "separator"
                },
                {
                    "contents": [
                        {
                            "align": "center",
                            "color": "#ffffff",
                            "text": "Hello , {}".format(contact.displayName),
                            "type": "text",
                            "wrap": True, 
                        }
                    ],
                    "layout": "vertical",
                    "type": "box"
                }
            ],
            "cornerRadius": "16px",
            "layout": "vertical",
            "type": "box"
        },
        "size": "mega",
        "styles": {
            "header": {
                "backgroundColor": "#00000Cac"
            }
        },
        "type": "bubble"
    },
    "type": "flex"
}
                    sendTemplate(to, data)
                    #while "token" not in res:
                    get_token = res["get_token"]
                    resp = requests.get(res["get_pin"])
                    res = resp.json()
                    if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                    if "pincode" in res: noobcoder.sendMessage(to, "Input PIN: %s" % (res["pincode"]))

                    resp = requests.get(get_token)
                    res = resp.json()
                    print(res)
                    token = res["authToken"]
                    #token, cert = parseLog(res)
                    #with open(f'{msg._from}.txt',"w") as b: token = b.write(cert)
                    sleep(5)
                    print(f'{token} : Saved to data..')
                if msg._from not in premium['listLogin']:
                    premium['listLogin'][msg._from] =  '%s' % user
                    #token, cert = parseLog(res)
                    token = res["authToken"]
                    isi = "{}".format(token)
                    if ajs == None:
                        os.system('cp -r hamzh {}'.format(user))
                        os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                        os.system('screen -dmS {}'.format(user))
                        os.system('screen -r {} -X stuff "cd {} && python3 staff.py \n"'.format(user, user))

                    else:
                        os.system('cp -r hamzh {}'.format(user))
                        os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                        os.system('screen -dmS {}'.format(user))
                        os.system('screen -r {} -X stuff "cd {} && python3 {}.py -t {}\n"'.format(user, user, file, ajs))
                    #noobcoder.sendMessage(to, "< Notification >\n\nFile : {}\nStatus : Login Success".format(user))
                    data={"type":"flex","altText":"☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜™","contents":{
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
                    sendTemplate(to, data)
                else:
                    noobcoder.sendMention(msg.to, '「 Req Login 」\n• Status : Failed\n• User: @!',' ', [msg._from])
            thread = threading.Thread(target=frzky)
            thread.daemon = True
            thread.start()
        except:
            noobcoder.sendMention(to, '「 Reg Login 」\n• Status : Failed\n •User: @!',' ', [msg._from])
def loginar(to, msg, header, certificate=""):
    if msg._from in premium["myService"]:
        user = premium["myService"][msg._from]
        try:
            def frzky():
                contact = noobcoder.getContact(msg._from)
                LINKFOTO = "https://ga2.line.naver.jp/ti/p/~jekdaniel." + msg._from
                #try:
                if 1 == 2:
                    with open(f'{msg._from}.txt',"r") as a: toket = a.read()
                    sleep(1)
                    print(f'{toket} : Loggin ..')
                    assert header in HEADERS, "invaild header"
                    resp = requests.post(API_URL() + "/login?" + urllib.parse.urlencode({"custom_headers": HEADERS[header], "certificate": toket}))
                    res = resp.json()
                    if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                    noobcoder.sendMessage(to, "Login URL: %s" % (res["url"]))
                    
                    
                    data={"type":"flex","altText":"LOGIN SB\n"+res["url"],"contents": {
        "direction": "ltr",
        "hero": {
            "backgroundColor": "#00000Cac",
            "borderColor": "#ffffff",
            "borderWidth": "2px",
            "contents": [
                {
                    "aspectMode": "cover",
                    "position": "absolute",
                    "size": "full",
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
                },
                {
                    "backgroundColor": "#00000Cac",
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "size": "full",
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                        },
                        {
                            "contents": [
                                {
                                    "type": "separator"
                                }
                            ],
                            "layout": "vertical",
                            "type": "box"
                        }
                    ],
                    "layout": "vertical",
                    "position": "absolute",
                    "type": "box"
                },
                {
                    "backgroundColor": "#00000Cac",
                    "contents": [
                        {
                            "text": " ",
                            "type": "text"
                        }
                    ],
                    "height": "200px",
                    "layout": "vertical",
                    "position": "absolute",
                    "type": "box",
                    "width": "1000px"
                },
                {
                    "borderColor": "#ffffff",
                    "borderWidth": "3px",
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "size": "full",
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                        }
                    ],
                    "cornerRadius": "100px",
                    "height": "60px",
                    "layout": "vertical",
                    "offsetStart": "10px",
                    "offsetTop": "30px",
                    "spacing": "xl",
                    "type": "box",
                    "width": "60px"
                },
                {
                    "contents": [
                        {
                            "action": {
                                "label": "☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜",
                                "type": "uri",
                                "uri": "{}".format(res["url"])
                            },
                            "style": "secondary",
                            "type": "button"
                        }
                    ],
                    "layout": "vertical",
                    "offsetBottom": "25px",
                    "offsetStart": "80px",
                    "type": "box"
                },
                {
                    "type": "separator"
                },
                {
                    "contents": [
                        {
                            "align": "center",
                            "color": "#ffffff",
                            "text": "Hello , {}".format(contact.displayName),
                            "type": "text",
                            "wrap": True, 
                        }
                    ],
                    "layout": "vertical",
                    "type": "box"
                }
            ],
            "cornerRadius": "16px",
            "layout": "vertical",
            "type": "box"
        },
        "size": "mega",
        "styles": {
            "header": {
                "backgroundColor": "#00000Cac"
            }
        },
        "type": "bubble"
    },
    "type": "flex"
}
                    sendTemplate(to, data)
                    while "token" not in res:
                        resp = requests.post(API_URL() + res["callback"])
                        #res = resp.json()
                        if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                #except:
                else:
                    assert header in HEADERS, "invaild header"
                    apikey = "HkcxIBZefS"
                    resp = requests.get("https://fgmlogin.cf/qrv2/getlink.php?header=desktopmac&apikey="+apikey)
                    #resp = requests.post(API_URL() + "/login?" + urllib.parse.urlencode({"custom_headers": HEADERS[header], "certificate": certificate}))
                    res = resp.json()
                    if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                    noobcoder.sendMessage(to, "Login URL: %s" % (res["get_link"]))
                    data={"type":"flex","altText":"LOGIN SB\n"+res["get_link"],"contents": {
        "direction": "ltr",
        "hero": {
            "backgroundColor": "#00000Cac",
            "borderColor": "#ffffff",
            "borderWidth": "2px",
            "contents": [
                {
                    "aspectMode": "cover",
                    "position": "absolute",
                    "size": "full",
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
                },
                {
                    "backgroundColor": "#00000Cac",
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "size": "full",
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                        },
                        {
                            "contents": [
                                {
                                    "type": "separator"
                                }
                            ],
                            "layout": "vertical",
                            "type": "box"
                        }
                    ],
                    "layout": "vertical",
                    "position": "absolute",
                    "type": "box"
                },
                {
                    "backgroundColor": "#00000Cac",
                    "contents": [
                        {
                            "text": " ",
                            "type": "text"
                        }
                    ],
                    "height": "200px",
                    "layout": "vertical",
                    "position": "absolute",
                    "type": "box",
                    "width": "1000px"
                },
                {
                    "borderColor": "#ffffff",
                    "borderWidth": "3px",
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "size": "full",
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                        }
                    ],
                    "cornerRadius": "100px",
                    "height": "60px",
                    "layout": "vertical",
                    "offsetStart": "10px",
                    "offsetTop": "30px",
                    "spacing": "xl",
                    "type": "box",
                    "width": "60px"
                },
                {
                    "contents": [
                        {
                            "action": {
                                "label": "☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜",
                                "type": "uri",
                                "uri": "{}".format(res["get_link"])
                            },
                            "style": "secondary",
                            "type": "button"
                        }
                    ],
                    "layout": "vertical",
                    "offsetBottom": "25px",
                    "offsetStart": "80px",
                    "type": "box"
                },
                {
                    "type": "separator"
                },
                {
                    "contents": [
                        {
                            "align": "center",
                            "color": "#ffffff",
                            "text": "Hello , {}".format(contact.displayName),
                            "type": "text",
                            "wrap": True, 
                        }
                    ],
                    "layout": "vertical",
                    "type": "box"
                }
            ],
            "cornerRadius": "16px",
            "layout": "vertical",
            "type": "box"
        },
        "size": "mega",
        "styles": {
            "header": {
                "backgroundColor": "#00000Cac"
            }
        },
        "type": "bubble"
    },
    "type": "flex"
}
                    sendTemplate(to, data)
                    #while "token" not in res:
                    #resp = requests.post(API_URL() + res["callback"])
                    get_token = res["get_token"]
                    resp = requests.get(res["get_pin"])
                    res = resp.json()
                    if resp.status_code != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                    if "pincode" in res: noobcoder.sendMessage(to, "Input PIN: %s" % (res["pincode"]))

                    resp = requests.get(get_token)
                    res = resp.json()
                    token = res["authToken"]
                    #token, cert = parseLog(res)
                    #with open(f'{msg._from}.txt',"w") as b: token = b.write(cert)
                    sleep(1)
                    print(f'{token} : Saved to data..')
                if msg._from not in premium['listLogin']:
                    premium['listLogin'][msg._from] =  '%s' % user
                    #token, cert = parseLog(res)
                    token = res["authToken"]
                    isi = "{}".format(token)
                    os.system('cp -r hamzh {}'.format(user))
                    os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                    os.system('screen -dmS {}'.format(user))
                    os.system('screen -r {} -X stuff "cd {} && python3 hamzh.py\n"'.format(user, user))
                    #noobcoder.sendMessage(to, "< Notification >\n\nFile : {}\nStatus : Login Success".format(user))
                    data={"type":"flex","altText":"☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜™","contents":{
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
                    sendTemplate(to, data)
                else:
                    noobcoder.sendMention(msg.to, '「 Req Login 」\n• Status : Failed\n• User: @!',' ', [msg._from])
            thread = threading.Thread(target=frzky)
            thread.daemon = True
            thread.start()
        except:
            noobcoder.sendMention(to, '「 Reg Login 」\n• Status : Failed\n •User: @!',' ', [msg._from])
def sendFooter(to, text):
    true=True
    contact = noobcoder.getContact(noobcoderMID)
    a = contact.displayName
    b = "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus)
    data = {
    "type": "flex",
    "altText": text,
    "contents": {
    "type": "bubble",
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
        "size": "full",
        "aspectMode": "cover",
        "position": "absolute",
        "aspectRatio": "5:10"
      },
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
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "{}".format(b),
                    "aspectMode": "cover"
                  }
                ],
                "width": "20px",
                "height": "20px",
                "cornerRadius": "100px",
                "borderWidth": "1px",
                "borderColor": "{}".format(setbot["separator"])
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(a),
                    "align": "center",
                    "gravity": "center",
                    "wrap": True,
                    "size": "md",
                    "color": "{}".format(setbot["text"])
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "{}".format(b),
                    "aspectMode": "cover"
                  }
                ],
                "width": "20px",
                "height": "20px",
                "cornerRadius": "100px",
                "borderColor": "{}".format(setbot["separator"]),
                "borderWidth": "1px"
              }
            ],
            "paddingAll": "5px"
          }
        ]
      },
      {
        "type": "separator",
        "color": "{}".format(setbot["separator"])
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "align": "center",
            "gravity": "center",
            "wrap": True,
            "color": "{}".format(setbot["text"])
          }
        ],
        "paddingAll": "3px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "{}".format(setbot["separator"]),
    "borderWidth": "3px"
  }
}}
    sendTemplate(to, data)
def sendFooter2(to, text):
    true=True
    contact = noobcoder.getContact(noobcoderMID)
    a = contact.displayName
    b = "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus)
    data = {
    "type": "flex",
    "altText": text,
    "contents": {
        "hero": {
            "backgroundColor": "#339999",
            "borderColor": "#339999",
            "borderWidth": "2px",
            "contents": [
                {
                    "action": {
                        "type": "uri",
                        "uri": "https://line.me/ti/p/~66.6p",
                    },
                    "aspectMode": "cover",
                    "aspectRatio": "30:7",
                    "offsetBottom": "2px",
                    "size": "full",
                    "type": "image",
                    "url": "{}".format(b),
                },
                {
                    "aspectMode": "cover",
                    "aspectRatio": "15:4",
                    "position": "absolute",
                    "size": "5xl",
                    "type": "image",
                    "url": "https://a.top4top.net/p_571t4gdd1.png"
                },
                {
                    "aspectMode": "cover",
                    "aspectRatio": "15:4",
                    "offsetEnd": "0px",
                    "position": "absolute",
                    "size": "5xl",
                    "type": "image",
                    "url": "https://a.top4top.net/p_571t4gdd1.png"
                },
                {
                    "backgroundColor": "#00000Cac",
                    "contents": [
                        {
                            "uri": "https://line.me/ti/p/~66.6p",
                            "type": "text"
                        }
                    ],
                    "height": "70px",
                    "layout": "vertical",
                    "position": "absolute",
                    "type": "box",
                    "width": "1000px"
                },
                {
                    "borderColor": "#339999",
                    "borderWidth": "2px",
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "size": "full",
                            "type": "image",
                            "url": "{}".format(b),
                        }
                    ],
                    "cornerRadius": "100px",
                    "height": "42px",
                    "layout": "vertical",
                    "offsetStart": "3px",
                    "offsetTop": "10px",
                    "position": "absolute",
                    "type": "box",
                    "width": "42px"
                },
                {
                    "contents": [
                        {
                            "type": "filler"
                        },
                        {
                            "action": {
                                "label": "☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜",
                                "type": "uri",
                                "uri": "https://line.me/ti/p/~66.6p", 
                            },
                            "color": "#33FFCCac",
                            "type": "button"
                        },
                        {
                            "type": "filler"
                        }
                    ],
                    "height": "70px",
                    "layout": "vertical",
                    "position": "absolute",
                    "type": "box",
                    "width": "300px"
                },
                {
                    "borderColor": "#339999",
                    "borderWidth": "2px",
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "size": "full",
                            "type": "image",
                            "url": "{}".format(b),
                        }
                    ],
                    "cornerRadius": "100px",
                    "height": "42px",
                    "layout": "vertical",
                    "offsetEnd": "3px",
                    "offsetTop": "10px",
                    "position": "absolute",
                    "type": "box",
                    "width": "42px"
                },
                {
                    "backgroundColor": "#00000Cac",
                    "contents": [
                        {
                            "align": "center",
                            "color": "#33FFCCac",
                            "text": text,
                            "type": "text",
                            "wrap": True,
                        }
                    ],
                    "layout": "vertical",
                    "margin": "sm",
                    "type": "box"
                },
                {
                    "type": "spacer"
                }
            ],
            "cornerRadius": "18px",
            "layout": "vertical",
            "type": "box"
        },
        "size": "mega",
        "type": "bubble"
    },
    "type": "flex"
}
    sendTemplate(to, data)    
def sendFooter1(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜™",
            "iconUrl": "https://obs.line-scdn.net/{}".format(noobcoder.getContact('u29c4bb607fb8476b1ee77d0f1f7f14a2').pictureStatus),
            "linkUrl": "line://nv/profilePopup/mid=u29c4bb607fb8476b1ee77d0f1f7f14a2"
        }
    }
    sendTemplate(to, data)
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1643727178-0XPGAaRX', xyzz)
    token = noobcoder.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1643727178-0XPGAaRX', xyzz)
    token = noobcoder.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest(nbcorp.getChannel('chanview'), xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def mosing(to, isi):
    true=True
    contact = noobcoder.getContact(noobcoderMID)
    a = contact.displayName
    b = "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus)
    data = {
        "type": "flex",
        "altText": isi,
        "contents": {
          "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus), 
        "size": "full",
        "aspectMode": "cover",
        "position": "absolute",
        "aspectRatio": "10:30"
      },
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
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus), 
                    "aspectMode": "cover"
                  }
                ],
                "width": "50px",
                "height": "50px",
                "cornerRadius": "100px",
                "borderWidth": "2px",
                "borderColor": "{}".format(setbot["separator"]),
                "offsetStart": "5px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": gwcool["squad"],
                    "size": "xl",
                    "weight": "bold",
                    "color": "{}".format(setbot["text"])
                  },
                  {
                    "type": "text",
                    "text": "selfbots edition",
                    "size": "xs",
                    "color": "{}".format(setbot["text"]),
                    "weight": "bold"
                  }
                ],
                "margin": "md",
                "offsetStart": "5px"
              }
            ],
            "borderWidth": "1px",
            "borderColor": "{}".format(setbot["separator"])
          }
        ],
        "paddingAll": "6px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": isi,
                "offsetStart": "5px",
                "size": "md",
                "color": "{}".format(setbot["text"]),
                "wrap": True
              }
            ],
            "borderWidth": "1px",
            "borderColor": "{}".format(setbot["separator"])
          }
        ],
        "paddingAll": "6px"
      },
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
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "{}".format(b),
                    "aspectMode": "cover"
                  }
                ],
                "width": "20px",
                "height": "20px",
                "cornerRadius": "100px",
                "offsetStart": "5px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(a),
                    "size": "md",
                    "color": "{}".format(setbot["text"]),
                  }
                ],
                "offsetStart": "8px"
              }
            ],
            "borderWidth": "1px",
            "borderColor": "{}".format(setbot["separator"])
          }
        ],
        "paddingAll": "6px"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "{}".format(setbot["separator"]),
    "cornerRadius": "17px",
    "borderWidth": "4px"
  }
}}
    sendTemplate(to,data)
def hehehe1(to):
    data={"type":"flex","altText":gwcool["squad"],"contents":{
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
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
                            "size": "xxs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "http://linecorp.com/"
                            }
                          },
                          {
                            "type": "text",
                            "text": "login sb",
                            "align": "center",
                            "size": "xs",
                            "color": "#ffffff",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "http://linecorp.com/"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
                            "size": "xxs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "http://linecorp.com/"
                            }
                          },
                          {
                            "type": "text",
                            "text": "Logout sb",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center"
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
                            "size": "xxs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "http://linecorp.com/"
                            }
                          },
                          {
                            "type": "text",
                            "text": "Loginajstoken",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
                            "size": "xxs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "http://linecorp.com/"
                            }
                          },
                          {
                            "type": "text",
                            "text": "Logout ajs",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center"
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
                            "size": "xxs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "http://linecorp.com/"
                            }
                          },
                          {
                            "type": "text",
                            "text": "java",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center"
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
                            "size": "xxs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "http://linecorp.com/"
                            }
                          },
                          {
                            "type": "text",
                            "text": "help",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
                            "size": "xxs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "http://linecorp.com/"
                            }
                          },
                          {
                            "type": "text",
                            "text": "glist",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center"
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
                            "size": "xxs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "http://linecorp.com/"
                            }
                          },
                          {
                            "type": "text",
                            "text": "reboot",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center"
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus),
                            "size": "xxs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "http://linecorp.com/"
                            }
                          },
                          {
                            "type": "text",
                            "text": "invme",
                            "size": "xs",
                            "color": "#fffffd",
                            "align": "center"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "borderColor": "#ffffff",
            "borderWidth": "2px"
          }
        ]
      }
    ],
    "cornerRadius": "xl",
    "borderColor": "#ffffff",
    "borderWidth": "4px"
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }
  }
}}
    sendTemplate(to,data) 
def debug():
    get_profile_time_start = time.time()
    get_profile = noobcoder.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_group_time_start = time.time()
    get_group = noobcoder.getGroupIdsJoined()
    get_group_time = time.time() - get_group_time_start
    get_contact_time_start = time.time()
    get_contact = noobcoder.getContact(get_profile.mid)
    get_contact_time = time.time() - get_contact_time_start
    elapsed_time = time.time() - get_profile_time_start
    return " 「 Debug 」\n - Send Message\n   %.5f\n - Get Profile\n   %.5f\n - Get Contact\n   %.5f\n - Get Group\n   %.5f" % (elapsed_time,get_profile_time,get_contact_time,get_group_time)
#=====================================================================
def shareall(to, text):
    lol = noobcoder.getGroupIdsJoined()
    for group in lol:
        noobcoder.sendPostToTalk(group, text)
    noobcoder.sendMessage(to, "Share in {} group".format(str(len(lol))))
#=====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================================
#def Template(to):
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    noobcoder.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    noobcoder.sendMessage(to, '', annda, 13)

def B64e(to, url):
    import base64
    return noobcoder.sendMessage(to, base64.b64encode(url.encode()).decode())

def B64d(to, url):
    import base64
    return noobcoder.sendMessage(to, base64.b64decode(url.encode()).decode())
    
def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            noobcoder.sendMessage(to, text, {'MSG_SENDER_NAME': noobcoder.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + noobcoder.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            noobcoder.sendMessage(to, text, {'MSG_SENDER_NAME': noobcoder.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + noobcoder.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Dragon  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    noobcoder.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(noobcoder.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + noobcoder.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = noobcoder.genOBSParams({'oid': noobcoderMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = noobcoder.server.postContent('{}/talk/vp/upload.nhn'.format(str(noobcoder.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        noobcoder.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("noobcoderWasHere.mp4")
#=====================================================================
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)
        
def change(url):
    import base64
    return base64.b64encode(url.encode()).decode()
    
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@MentionOrang "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        noobcoder.sendMessage(to, textx, {'MSG_SENDER_NAME': client.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + noobcoder.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
def logError(text):
    noobcoder.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("noobcoder/errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
#=====================================================================
#=====================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
#=====================================================================
#=====================================================================
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''
    rmv = len(key + cmd) + 1
    return text[rmv:]
def backupData():
    try:
        backup = settings
        f = codecs.open('settings/temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('settings/wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = premium
        f = codecs.open('settings/kontol.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = java
        f = codecs.open('settings/java.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = betamaker
        f = codecs.open('settings/ajs.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest(nbcorp.getChannel('chanview'), xyzz)
    token = noobcoder.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
#=====================================================================
async def noobcoderBot(op):
    try:
        if settings["restartPoint"] != None:
            noobcoder.sendMessage(settings["restartPoint"], 'Activated♪')
            settings["restartPoint"] = None
        if op.type == 0:
            return
                        
        if op.type in [22,24]:
            client.leaveRoom(op.param1)
#=====================================================================
        if op.type == 13:
            if noobcoder.getProfile().mid in op.param3:
                G = noobcoder.getCompactGroup(op.param1)
                if settings["autoJoin"] == True:
                    if len(G.members) <= wait["Members"]:
                        noobcoder.acceptGroupInvitation(op.param1)
#                        mentions(op.param1,"Hallo @! You Are Not My Author\nI Leave , See ya",[op.param2])
                        noobcoder.leaveGroup(op.param1)
                    else:
                        noobcoder.acceptGroupInvitation(op.param1)
                if len(G.members) <= wait["Members"]:
                    noobcoder.rejectGroupInvitation(op.param1)
                else:
                    if admin in op.param2:
                        noobcoder.acceptGroupInvitation(op.param1)
            else:pass
#=====================================================================
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            khietag = "u500218bb2f290d906bc4cb3fe4c9173a"
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != noobcoderMID: to = sender
                else: to = receiver
                if msg.contentType == 6:
                    try:
                        contact = noobcoder.getContact(sender)
                        if msg.toType == 2:
                            anu = noobcoder.getGroup(to)
                            if msg.contentMetadata['GC_EVT_TYPE'] == 'S' and msg.contentMetadata['GC_MEDIA_TYPE'] == 'LIVE':
                                anu = msg.contentMetadata={'GC_EVT_TYPE': 'S', 'GC_CHAT_MID': to, 'RESULT': 'INFO', 'SKIP_BADGE_COUNT': 'false', 'GC_IGNORE_ON_FAILBACK': 'false', 'TYPE': 'G', 'DURATION': '0', 'GC_MEDIA_TYPE': 'VIDEO', 'VERSION': 'X', 'CAUSE': '16'}
                    except Exception as e:
                        noobcoder.sendMessage(to, str(e))
                if msg.contentType == 22 and inSteals(sender):
                    if msg.toType == 0:to = sender
                    true=True
                    data = {
                        "type": "flex",
                        "altText": msg.contentMetadata["ALT_TEXT"],
                        "contents": json.loads(msg.contentMetadata['FLEX_JSON'])
                    }
                    sendTemplate(to, data)
                    with open("flex.txt", "w+") as f:
                      f.write(str(json.dumps(data, indent=4, sort_keys=True)))
                if msg.contentType == 4 and inSteals(sender):
                    if msg.toType == 0:to = sender
                    noobcoder.sendMessage(to, "Not support html content/template, just flex!")
                if msg.contentType == 14:
                    if hoho["savefile"] == True:
                        try:
                             namafile = hoho["namafile"]
                             noobcoder.downloadObjectMsg(msg_id,saveAs=namafile)
                             hoho["savefile"] = False
                             noobcoder.sendMessage(to, "Successful, the file has been uploaded")
                        except Exception as e:
                            noobcoder.sendMessage(to, str(e))
                if msg.contentType == 1:
                    if settings["changePicture"] == True:
                        path = noobcoder.downloadObjectMsg(msg_id, saveAs="tmp/pict.bin")
                        settings["changePicture"] = False
                        noobcoder.updateProfilePicture(path)
                        sendFooter(to,"Profile Image Updated.")
                if msg.contentType == 1: 
                    if settings["changeCoverProfile"] == True:
                        path = noobcoder.downloadObjectMsg(msg_id)
                        settings["changeCoverProfile"] = False
                        noobcoder.updateProfileCover(path)
                        sendFooter(to, "Type:Profile\n • Detail: Change Home Photos\n • Status: Succes..")
                    if settings['changeProfileVideo']['status'] == True and sender == noobcoderMID:
                        path = noobcoder.downloadObjectMsg(msg_id, saveAs="tmp/pict.bin")
                        if settings['changeProfileVideo']['stage'] == 1:
                            settings['changeProfileVideo']['picture'] = path
                            sendFooter(to, "Silahkan kirimkan video yang ingin anda jadikan profile")
                            settings['changeProfileVideo']['stage'] = 2
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    if msg.toType == 0:
                        if settings["autoRead"] == True:
                            noobcoder.sendChatChecked(to, msg_id)
                    if msg.toType == 2:
                        if settings["autoRead1"] == True:
                            noobcoder.sendChatChecked(to, msg_id)
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        if settings["autoJoin"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = noobcoder.findGroupByTicket(ticket_id)
                                if len(group.members) >= wait["Members"]:
                                    noobcoder.acceptGroupInvitationByTicket(group.id,ticket_id)
                                else:
                                    noobcoder.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    noobcoder.leaveGroup(group.id)
                    if msg._from in myAdmin:
                        if "/remote" in cmd:
                            function = lambda s:s[:1].lower() + s[1:] if s else ''
                            number = cmd.split("/remote:")[1];number = number.split()[0];noobcoder.getGroupIdsJoined()
                            if number.isdigit():number = int(number);group = noobcoder.getGroupIdsJoined()[number-1];to = group
                            cmd = cmd.replace("/remote:%s"%number,"").lstrip().rstrip()
                            if '/remote:' in text:text = text.replace("/remote:%s"%number,"").lstrip().rstrip();function(text)
                            else:text = text.replace("/remote:%s"%number,"").lstrip().rstrip();function(text)
                            if msg.toType == 0:msg.to = sender
                            elif msg.toType == 2:msg.to = msg.to
                            sendFooter(msg.to, "Command '%s' has been send to : %s" % (cmd, noobcoder.getGroup(group).name))
#==========================================
                    if cmd == "threads":
                        noobcoder.sendMessage(to,'Threads: {}'.format(threading.active_count()))
                        log.info("Debug Threads.")                            
#==========================================
                    elif cmd.startswith("savefile"):
                        if msg._from in myAdmin:
                            text = removeCmd("savefile", text)
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ", text)
                            if " " in key:
                                noobcoder.sendMessage(to, "Failed !")
                            else:
                                hoho["namafile"] = str(key).lower()
                                hoho["savefile"] = True
                                noobcoder.sendMessage(to, "Send file to save to be「 {} 」".format(str(key).lower()))
                    elif cmd.startswith("exec"):
                        if msg._from in myAdmin:
                            try:
                                sep = text.split("\n")
                                txt = text.replace(sep[0] + "\n","")
                                exec(txt)
                            except:
                                pass
#==========================================
                    elif cmd.startswith("down "):
                        if msg._from in myAdmin:
                           number = removeCmd("down", text)
                           if len(number) > 0:
                               if number.isdigit():
                                   number = int(number)
                                   if number > 5000:                                             
                                       noobcoder.sendMessage(to,"invalid >_< ! Max: 5000.")
                                   else:
                                       for i in range(0,number):
                                           noobcoder.sendMessage(to,str(number))
                                           number -= 1
                                           time.sleep(0.008)
                               else:
                                  noobcoder.sendMessage(to,"Please specify a valid number.")
                    elif cmd == "change dp" :
                        if msg._from in myAdmin:
                            settings["changePicture"] = True
                            sendFooter(to, "Send a Image to change picture.")
                    elif cmd == "change cover":
                        if msg._from in myAdmin:
                            settings["changeCoverProfile"] = True
                            sendFooter2(to,"Send a Image to change cover.")                   
                    elif cmd.startswith("updatername "):
                        if msg._from in myAdmin:
                            key = removeCmd("updatername", text)
                            kiy = settings["keyCommand"]
                            settings["keyCommand"] = str(key).lower()
                            sendFooter(to, "╭──「 Update Rname 」\n│ ⌬ Status : Success\n│ ⌬ From : "+str(kiy.title())+"\n╰To : "+str(key.title()))
                    elif cmd == "remote":
                        if msg._from in myAdmin:               
                            helpz="remote hm :\n" 
                            helpz+="\n• glist > "
                            helpz+="\n• /remote ngr kickall > "
                            helpz+="\n• /remote ngr cancel > "
                            helpz+="\n• /remote ngr bypass:\n"
                            helpz+="\n• /remote ngr speed<txt>"
                            helpz+="\n• $ free -h <txt>"
                            helpz+="\n• Openqr ngr <txt>"
                            mosing(to, str(ret))
                    elif cmd == "java":
                        if msg._from in myAdmin:               
                            helpz="Java hm :\n" 
                            helpz+="\n• Kickall > " + str(javascript['jskick1'])
                            helpz+="\n• Bypass > " + str(javascript['jskick'])
                            helpz+="\n• Cancel > " + str(javascript['cancels'])
                            helpz+="\n\nSettings :\n"
                            helpz+="\n• Change 1 <txt>"
                            helpz+="\n• Change 2 <txt>"
                            helpz+="\n• Change 3 <txt>"
                            sendFooter(to,helpz)
                    elif cmd.startswith("change"):
                        if msg._from in myAdmin:               
           #                 textx = text.replace(text.split(" ")[0]+" ","")
                            textx = removeCmd("change", text)
                            sal = textx.lower()
                            if sal.startswith("1"):
                               texts = textx[2:]
                               javascript["jskick1"] = texts
                               sendFooter(to, "Kickall update to `%s`" % texts)
                            if sal.startswith("2"):
                               texts = textx[2:]
                               javascript["jskick"] = texts
                               noobcoder.sendMessage(to, "Bypass update to `%s`" % texts)
                            if sal.startswith("3"):
                               texts = textx[2:]
                               javascript["cancels"] = texts
                               sendFooter(to, "Cancel update to `%s`" % texts)
                    elif cmd == javascript['jskick1']:
                        if msg._from in myAdmin:               
                          xyz = noobcoder.getGroup(to)
                          mem = [c.mid for c in xyz.members]
                          targets = []
                          for x in mem:
                            if x not in ["uee3920b9c8f6b2afb7069326e2ea2982","u09c11f239846b06539d08608099f7733",noobcoder.profile.mid]:targets.append(x)
                          if targets:
                            imkhie = 'simple.js gid={} token={} app={}'.format(to, noobcoder.authToken, "CHROMEOS\t2.4.0\tChrome OS\t1")
                            for target in targets:
                              imkhie += ' uid={}'.format(target)
                            success = execute_js(imkhie)
                            if success:sendFooter(to, "Success kick %i members." % len(targets))
                            else:noobcoder.sendMessage(to, "Failed kick %i members." % len(targets))
                          else:noobcoder.sendMessage(to, "Target not found.")
                    elif cmd == javascript['jskick']:
                        if msg._from in myAdmin: 
                          xyz = noobcoder.getGroup(to)
                          if xyz.invitee == None:pends = []
                          else:pends = [c.mid for c in xyz.invitee]
                          targp = []
                          for x in pends:
                            if x not in ["uee3920b9c8f6b2afb7069326e2ea2982","u09c11f239846b06539d08608099f7733",noobcoder.profile.mid]:targp.append(x)
                          mems = [c.mid for c in xyz.members]
                          targk = []
                          for x in mems:
                            if x not in ["uee3920b9c8f6b2afb7069326e2ea2982","u09c11f239846b06539d08608099f7733",noobcoder.profile.mid]:targk.append(x)
                          imkhie = 'dual.js gid={} token={}'.format(to, noobcoder.authToken)
                          for x in targp:imkhie += ' uid={}'.format(x)
                          for x in targk:imkhie += ' uik={}'.format(x)
                          execute_js(imkhie)
                    elif cmd == javascript["cancels"]:
                        if msg._from in myAdmin: 
                            group = noobcoder.getGroup(to)
                            cm = 'clear.js gid={} token="{}"'.format(to, noobcoder.authToken)
                            for invitees in group.invitee:
                                  cm += ' uid={}'.format(invitees.mid)
                            print(cm)
                            success = execute_js(cm)
#==========================================
                    if cmd == "kiss me":
                        noobcoder.generateReplyMessage(msg.id)
                        noobcoder.sendReplyMessage(msg.id, to,"。。・゜゜・❤ "+noobcoder.getContact(sender).displayName+" ❤ \n(づ￣ ³￣)づ")
                    elif cmd == "reader":
                        ret = "Now set : " + str(tailah["siderPesan"])
                        ret += "\n\n⌬ {}read on/off".format(setKey)
                        ret += "\n⌬ {}read set <text>".format(setKey)
                        sendFooter(to, str(ret))
                    elif cmd == "leave":
                        ret = "Now set : " + str(lvin["textnya"])
                        ret += "\n\n⌬ {}leave on/off".format(setKey)
                        ret += "\n⌬ {}leave set <text>".format(setKey)
                        sendFooter(to, str(ret))
                    elif cmd == "welcome":
                        ret = "Now set : " + str(wmin["textnya"])
                        ret += "\n\n⌬ {}welcome on/off".format(setKey)
                        ret += "\n⌬ {}welcome set <text>".format(setKey)
                        sendFooter(to, str(ret))
                        
#==========================================
                    elif cmd.startswith("bye "):
                        if msg._from in myAdmin:
                            number = removeCmd("bye", text)
                            groups = noobcoder.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = noobcoder.getGroup(group)
                                try:
                                    noobcoder.leaveGroup(G.id)
                                except:
                                    noobcoder.leaveGroup(G.id)
                                noobcoder.sendMessage(to, "「Leave 」\n\nGroup : " + G.name)
                            except Exception as error:
                                noobcoder.sendMessage(to, str(error))
                    elif cmd == "help":
                        try:
                            help = "Service Commands :\n"
                            help += "\n⌬ {}Login sb".format(setKey)
                            help += "\n⌬ {}Logout sb".format(setKey)
                            help += "\n⌬ {}Restart sb".format(setKey)
                            help += "\n\nOwner Commands :\n"
                            help += "\n⌬ {}Addsb <user> <@>".format(setKey)
                            help += "\n⌬ {}Addajs <user> <@>".format(setKey)
                            help += "\n⌬ {}Delsb <num>".format(setKey)
                            help += "\n⌬ {}Delajs <num>".format(setKey)
                            help += "\n⌬ {}List sb".format(setKey)
                            help += "\n⌬ {}List ajs".format(setKey)
                            true=True
                            contact = noobcoder.getContact(msg._from)
                            a = contact.displayName
                            b = "https://obs.line-scdn.net/{}".format(noobcoder.getContact(msg._from).pictureStatus)
                            data = {
        "type": "flex",
        "altText": str(help),
        "contents": {
          "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute",
        "aspectRatio": "8:17"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": b,
                "aspectMode": "cover"
              }
            ],
            "width": "60px",
            "height": "60px",
            "cornerRadius": "100px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜",
                "size": "xl",
                "color": "#FFFFFF",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": "☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜",
                "size": "md",
                "color": "#FFFFFF",
                "weight": "bold"
              }
            ],
            "offsetStart": "10px"
          }
        ],
        "paddingAll": "6px"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": str(help),
            "size": "md",
            "color": "#FFFFFF",
            "weight": "bold",
            "wrap": True
          }
        ],
        "margin": "md",
        "offsetStart": "8px"
      },
      {
        "type": "separator",
        "margin": "md",
        "color": "#FFFFFF"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "hello, {}".format(a),
            "size": "md",
            "color": "#FFFFFF",
            "weight": "bold",
            "wrap": True
          }
        ],
        "paddingAll": "6px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                            sendTemplate(to,data)
                        except Exception as error:
                            sendFooter(to, "「 Result Error 」\n" + str(error))                                 
                    elif text.lower() == "login sb" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        loginsb(to, msg, "android_lite")

                    if cmd.startswith("loginajsar ") and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        print("LOGINAJS IN")
                        loginsb(to, msg, "android_lite", ajs=text.split(" ")[1], file="hamzhajs")

                    if cmd.startswith("loginajstoken ") and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        print("LOGINAJS IN")
                        loginsb(to, msg, "android_lite", ajs=text.split(" ")[1], file="staffajs")


                    elif text.lower() == "login ar" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        loginar(to, msg, "desktopmac")
                    elif text.lower() == "loginajs " and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        loginajs(to, msg, "chrome")
                    elif cmd.startswith("fadsfdsloginajstoken ") and msg._from not in betamaker['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in betamaker["myService"]:
                            user = betamaker["myService"][msg._from]
                            sep = text.split(" ")
                            hey = text.replace(sep[0] + " ", "")
                            print(hey)
                            try:
                                 def frzky():
                                     contact = noobcoder.getContact(sender)
                                     cover = noobcoder.getProfileCoverURL(sender)
                                     LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                                     headers = {"apiKey":"QbUPgLSmbAgQ","appName": "DESKTOPMAC\t5.24.1\tMac Os\t10.15.2","cert" : None,"server": random.choice(["pool-1","pool-2"]),"sysname": "CannibalBots"}
                                     main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
                                     #LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                                     data={"type":"flex","altText":"Login Flex","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": cover,
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Hello , {}".format(user),
                "size": "md",
                "weight": "bold",
                "color": "#ffffff",
                "wrap": True
              },
              {
                "type": "text",
                "text": "CLICK HERE FOR LOGIN",
                "size": "lg",
                "color": "#ffffff",
                "weight": "bold",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "{}".format(main["result"]["qr_link"])
                }
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "width": "50px",
            "height": "50px",
            "cornerRadius": "100px",
            "borderWidth": "2px",
            "borderColor": "#FFFFFF"
          }
        ],
        "paddingAll": "10px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                                     sendTemplate(to, data)
                                     result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
                                     if result["status"] != 200: noobcoder.sendMessage(to, "Request Timeout!!")
                                     noobcoder.sendMessage(to,"Pin code: " + result["result"])
                                     result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
                                     if result["status"] != 200:
                                        raise Exception("Timeout!!!")
                                     if msg._from not in premium['listLogin']:
                                         premium['listLogin'][msg._from] =  '%s' % user
                                         isi = "{}".format(result["result"]["token"])
                                         isian = "{}".format(hey)
                                         print(isian)
                                         os.system('cp -r ajs {}'.format(user))
                                         os.system('cd {} && echo -n "{}" > tokenajs.txt'.format(user, isian))
                                         os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                         os.system('screen -dmS {}'.format(user))
                                         os.system('screen -r {} -X stuff "cd {} && python3 majstoken.py \n"'.format(user, user))
                                         data={"type":"flex","altText":"Flex Login","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": cover,
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "File : {}".format(user),
                "size": "md",
                "weight": "bold",
                "color": "#ffffff",
                "wrap": True
              },
              {
                "type": "text",
                "text": "SUCESS TO LOGIN",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold",
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "width": "50px",
            "height": "50px",
            "cornerRadius": "100px",
            "borderWidth": "2px",
            "borderColor": "#FFFFFF"
          }
        ],
        "paddingAll": "10px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                                         sendTemplate(to, data)
                                     else:
                                         noobcoder.sendMention(msg.to, '「 Req Login 」\n• Status : Failed\n• User: @!',' ', [msg._from])
                                 thread = threading.Thread(target=frzky)
                                 thread.daemon = True
                                 thread.start()
                            except:
                                 noobcoder.sendMention(msg.to, '「 Reg Login 」\n• Status : Failed\n •User: @!',' ', [msg._from])
                    elif cmd.startswith("loginajstoken2 ") and msg._from not in betamaker['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in betamaker["myService"]:
                            user = betamaker["myService"][msg._from]
                            sep = removeCmd("loginajstoken2", text)
                            sepa = text.split(" ")
                            dan = sepa[1]
                            anu = sepa[2]
                            print(dan)
                            print(anu)
                            try:
                                 def frzky():
                                     contact = noobcoder.getContact(sender)
                                     cover = noobcoder.getProfileCoverURL(sender)
                                     result = json.loads(requests.get('https://api.boteater.us/line_qr_v2?header=desktopmac&auth=p3VX0ojnZMJt').text)
                                     LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                                     data={"type":"flex","altText":"Login Flex","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": cover,
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Hello , {}".format(user),
                "size": "md",
                "weight": "bold",
                "color": "#ffffff",
                "wrap": True
              },
              {
                "type": "text",
                "text": "CLICK HERE FOR LOGIN",
                "size": "lg",
                "color": "#ffffff",
                "weight": "bold",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "{}".format(result["result"]["qr_link"])
                }
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "width": "50px",
            "height": "50px",
            "cornerRadius": "100px",
            "borderWidth": "2px",
            "borderColor": "#FFFFFF"
          }
        ],
        "paddingAll": "10px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                                     sendTemplate(to, data)
                                     result = json.loads(requests.get(result["result"]["callback"]+'&auth=p3VX0ojnZMJt').text)
                                     if result["status"] != 200:
                                        raise Exception("Timeout!!!")
                                     noobcoder.sendMention(msg.to, '「 Pincode Login 」\n• Hello : @! \n• Your Pincode : {}'.format(result["result"]["pin_code"]),' ', [msg._from])
                                     result = json.loads(requests.get(result["result"]["callback"]+'&auth=p3VX0ojnZMJt').text)
                                     if result["status"] != 200:
                                        raise Exception("Timeout!!!")
                                     if msg._from not in betamaker['listLogin']:
                                         betamaker['listLogin'][msg._from] =  '%s' % user
                                         isi = "{}".format(result["result"]["token"])
                                         isian = "{}".format(dan)
                                         isian2 = "{}".format(anu)
                                         print(isian)
                                         os.system('cp -r ajs {}'.format(user))
                                         os.system('cd {} && echo -n "{}" > tokenajs.txt'.format(user, isian))
                                         os.system('cd {} && echo -n "{}" > tokenajs2.txt'.format(user, isian2))
                                         os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                         os.system('screen -dmS {}'.format(user))
                                         os.system('screen -r {} -X stuff "cd {} && python3 majstoken2.py \n"'.format(user, user))
                                         data={"type":"flex","altText":"Flex Login","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": cover,
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "File : {}".format(user),
                "size": "md",
                "weight": "bold",
                "color": "#ffffff",
                "wrap": True
              },
              {
                "type": "text",
                "text": "SUCESS TO LOGIN",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold",
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "width": "50px",
            "height": "50px",
            "cornerRadius": "100px",
            "borderWidth": "2px",
            "borderColor": "#FFFFFF"
          }
        ],
        "paddingAll": "10px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                                         sendTemplate(to, data)
                                     else:
                                         noobcoder.sendMention(msg.to, '「 Req Login 」\n• Status : Failed\n• User: @!',' ', [msg._from])
                                 thread = threading.Thread(target=frzky)
                                 thread.daemon = True
                                 thread.start()
                            except:
                                 noobcoder.sendMention(msg.to, '「 Reg Login 」\n• Status : Failed\n •User: @!',' ', [msg._from])
                    elif cmd.startswith("loginajstoken3 ") and msg._from not in betamaker['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in betamaker["myService"]:
                            user = betamaker["myService"][msg._from]
                            sep = removeCmd("loginajstoken2", text)
                            sepa = text.split(" ")
                            dan = sepa[1]
                            anu = sepa[2]
                            ani = sepa[3]
                            print(dan)
                            print(anu)
                            print(ani)
                            try:
                                 def frzky():
                                     contact = noobcoder.getContact(sender)
                                     cover = noobcoder.getProfileCoverURL(sender)
                                     result = json.loads(requests.get('https://api.boteater.us/line_qr_v2?header=desktopmac&auth=p3VX0ojnZMJt').text)
                                     LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                                     data={"type":"flex","altText":"Login Flex","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": cover,
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Hello , {}".format(user),
                "size": "md",
                "weight": "bold",
                "color": "#ffffff",
                "wrap": True
              },
              {
                "type": "text",
                "text": "CLICK HERE FOR LOGIN",
                "size": "lg",
                "color": "#ffffff",
                "weight": "bold",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "{}".format(result["result"]["qr_link"])
                }
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "width": "50px",
            "height": "50px",
            "cornerRadius": "100px",
            "borderWidth": "2px",
            "borderColor": "#FFFFFF"
          }
        ],
        "paddingAll": "10px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                                     sendTemplate(to, data)
                                     result = json.loads(requests.get(result["result"]["callback"]+'&auth=p3VX0ojnZMJt').text)
                                     if result["status"] != 200:
                                        raise Exception("Timeout!!!")
                                     noobcoder.sendMention(msg.to, '「 Pincode Login 」\n• Hello : @! \n• Your Pincode : {}'.format(result["result"]["pin_code"]),' ', [msg._from])
                                     result = json.loads(requests.get(result["result"]["callback"]+'&auth=p3VX0ojnZMJt').text)
                                     if result["status"] != 200:
                                        raise Exception("Timeout!!!")
                                     if msg._from not in betamaker['listLogin']:
                                         betamaker['listLogin'][msg._from] =  '%s' % user
                                         isi = "{}".format(result["result"]["token"])
                                         isian = "{}".format(dan)
                                         isian2 = "{}".format(anu)
                                         isian3 = "{}".format(ani)
                                         print(isian)
                                         print(isian2)
                                         print(isian3)
                                         os.system('cp -r ajs {}'.format(user))
                                         os.system('cd {} && echo -n "{}" > tokenajs.txt'.format(user, isian))
                                         os.system('cd {} && echo -n "{}" > tokenajs2.txt'.format(user, isian2))
                                         os.system('cd {} && echo -n "{}" > tokenajs3.txt'.format(user, isian3))
                                         os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                         os.system('screen -dmS {}'.format(user))
                                         os.system('screen -r {} -X stuff "cd {} && python3 majstoken3.py \n"'.format(user, user))
                                         data={"type":"flex","altText":"Flex Login","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": cover,
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "File : {}".format(user),
                "size": "md",
                "weight": "bold",
                "color": "#ffffff",
                "wrap": True
              },
              {
                "type": "text",
                "text": "SUCESS TO LOGIN",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold",
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "width": "50px",
            "height": "50px",
            "cornerRadius": "100px",
            "borderWidth": "2px",
            "borderColor": "#FFFFFF"
          }
        ],
        "paddingAll": "10px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                                         sendTemplate(to, data)
                                     else:
                                         noobcoder.sendMention(msg.to, '「 Req Login 」\n• Status : Failed\n• User: @!',' ', [msg._from])
                                 thread = threading.Thread(target=frzky)
                                 thread.daemon = True
                                 thread.start()
                            except:
                                 noobcoder.sendMention(msg.to, '「 Reg Login 」\n• Status : Failed\n •User: @!',' ', [msg._from])
                    elif cmd.startswith("loginajstoken4 ") and msg._from not in betamaker['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in betamaker["myService"]:
                            user = betamaker["myService"][msg._from]
                            sep = removeCmd("loginajstoken2", text)
                            sepa = text.split(" ")
                            dan = sepa[1]
                            anu = sepa[2]
                            ani = sepa[3]
                            kin = sepa[4]
                            print(dan)
                            print(anu)
                            print(ani)
                            print(kin)
                            try:
                                 def frzky():
                                     contact = noobcoder.getContact(sender)
                                     cover = noobcoder.getProfileCoverURL(sender)
                                     result = json.loads(requests.get('https://api.boteater.us/line_qr_v2?header=desktopmac&auth=p3VX0ojnZMJt').text)
                                     LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                                     data={"type":"flex","altText":"Login Flex","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": cover,
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Hello , {}".format(user),
                "size": "md",
                "weight": "bold",
                "color": "#ffffff",
                "wrap": True
              },
              {
                "type": "text",
                "text": "CLICK HERE FOR LOGIN",
                "size": "lg",
                "color": "#ffffff",
                "weight": "bold",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "{}".format(result["result"]["qr_link"])
                }
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "width": "50px",
            "height": "50px",
            "cornerRadius": "100px",
            "borderWidth": "2px",
            "borderColor": "#FFFFFF"
          }
        ],
        "paddingAll": "10px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                                     sendTemplate(to, data)
                                     result = json.loads(requests.get(result["result"]["callback"]+'&auth=p3VX0ojnZMJt').text)
                                     if result["status"] != 200:
                                        raise Exception("Timeout!!!")
                                     noobcoder.sendMention(msg.to, '「 Pincode Login 」\n• Hello : @! \n• Your Pincode : {}'.format(result["result"]["pin_code"]),' ', [msg._from])
                                     result = json.loads(requests.get(result["result"]["callback"]+'&auth=p3VX0ojnZMJt').text)
                                     if result["status"] != 200:
                                        raise Exception("Timeout!!!")
                                     if msg._from not in betamaker['listLogin']:
                                         betamaker['listLogin'][msg._from] =  '%s' % user
                                         isi = "{}".format(result["result"]["token"])
                                         isian = "{}".format(dan)
                                         isian2 = "{}".format(anu)
                                         isian3 = "{}".format(ani)
                                         isian4 = "{}".format(kin)
                                         print(isian)
                                         print(isian2)
                                         print(isian3)
                                         print(isian4)
                                         os.system('cp -r ajs {}'.format(user))
                                         os.system('cd {} && echo -n "{}" > tokenajs.txt'.format(user, isian))
                                         os.system('cd {} && echo -n "{}" > tokenajs2.txt'.format(user, isian2))
                                         os.system('cd {} && echo -n "{}" > tokenajs3.txt'.format(user, isian3))
                                         os.system('cd {} && echo -n "{}" > tokenajs4.txt'.format(user, isian4))
                                         os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                         os.system('screen -dmS {}'.format(user))
                                         os.system('screen -r {} -X stuff "cd {} && python3 majstoken3.py \n"'.format(user, user))
                                         data={"type":"flex","altText":"Flex Login","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": cover,
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "File : {}".format(user),
                "size": "md",
                "weight": "bold",
                "color": "#ffffff",
                "wrap": True
              },
              {
                "type": "text",
                "text": "SUCESS TO LOGIN",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold",
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "width": "50px",
            "height": "50px",
            "cornerRadius": "100px",
            "borderWidth": "2px",
            "borderColor": "#FFFFFF"
          }
        ],
        "paddingAll": "10px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                                         sendTemplate(to, data)
                                     else:
                                         noobcoder.sendMention(msg.to, '「 Req Login 」\n• Status : Failed\n• User: @!',' ', [msg._from])
                                 thread = threading.Thread(target=frzky)
                                 thread.daemon = True
                                 thread.start()
                            except:
                                 noobcoder.sendMention(msg.to, '「 Reg Login 」\n• Status : Failed\n •User: @!',' ', [msg._from])
                    elif text.lower() == "start ajs" and msg._from not in betamaker['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in betamaker["myService"]:
                            user = betamaker["myService"][msg._from]
                            try:
                                 def frzky():
                                     contact = noobcoder.getContact(sender)
                                     cover = noobcoder.getProfileCoverURL(sender)
                                     result = json.loads(requests.get('https://api.boteater.us/line_qr_v2?header=desktopmac&auth=p3VX0ojnZMJt').text)
                                     LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                                     data={"type":"flex","altText":"Login Flex","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": cover,
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Hello , {}".format(user),
                "size": "md",
                "weight": "bold",
                "color": "#ffffff",
                "wrap": True
              },
              {
                "type": "text",
                "text": "CLICK HERE FOR LOGIN",
                "size": "lg",
                "color": "#ffffff",
                "weight": "bold",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "{}".format(result["result"]["qr_link"])
                }
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "width": "50px",
            "height": "50px",
            "cornerRadius": "100px",
            "borderWidth": "2px",
            "borderColor": "#FFFFFF"
          }
        ],
        "paddingAll": "10px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                                     sendTemplate(to, data)
                                     result = json.loads(requests.get(result["result"]["callback"]+'&auth=p3VX0ojnZMJt').text)
                                     if result["status"] != 200:
                                        raise Exception("Timeout!!!")
                                     noobcoder.sendMention(msg.to, '「 Pincode Login 」\n• Hello : @! \n• Your Pincode : {}'.format(result["result"]["pin_code"]),' ', [msg._from])
                                     result = json.loads(requests.get(result["result"]["callback"]+'&auth=p3VX0ojnZMJt').text)
                                     if result["status"] != 200:
                                        raise Exception("Timeout!!!")
                                     if msg._from not in betamaker['listLogin']:
                                         betamaker['listLogin'][msg._from] =  '%s' % user
                                         isi = "{}".format(result["result"]["token"])
                                         os.system('cd {} && echo -n "{}" > tokenajs.txt'.format(user, isi))
                                         os.system("screen -S {} -X quit".format(user))
                                         os.system('screen -dmS {}'.format(user))
                                         os.system('screen -r {} -X stuff "cd {} && python3 majs.py \n"'.format(user, user))
                                         data={"type":"flex","altText":"Flex Login","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": cover,
        "aspectMode": "cover",
        "size": "full",
        "position": "absolute"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "File : {}".format(user),
                "size": "md",
                "weight": "bold",
                "color": "#ffffff",
                "wrap": True
              },
              {
                "type": "text",
                "text": "SUCESS TO LOGIN",
                "color": "#ffffff",
                "size": "lg",
                "weight": "bold",
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "aspectMode": "cover"
              }
            ],
            "width": "50px",
            "height": "50px",
            "cornerRadius": "100px",
            "borderWidth": "2px",
            "borderColor": "#FFFFFF"
          }
        ],
        "paddingAll": "10px"
      }
    ],
    "paddingAll": "0px",
    "cornerRadius": "17px",
    "borderColor": "#FFFFFF",
    "borderWidth": "4px"
  }
}}
                                         sendTemplate(to, data)
                                     else:
                                         noobcoder.sendMention(msg.to, '「 Req Login 」\n• Status : Failed\n• User: @!',' ', [msg._from])
                                 thread = threading.Thread(target=frzky)
                                 thread.daemon = True
                                 thread.start()
                            except:
                                 noobcoder.sendMention(msg.to, '「 Reg Login 」\n• Status : Failed\n •User: @!',' ', [msg._from])                   
#==========================================
                    elif cmd.startswith("#reader1 on"):
                        if msg._from in myAdmin:
                          tailah["siderTemp"][receiver] = []
                          #settings['siderTemp'][receiver]['status'] = True
                          sendFooter(to, "Getreader set to on.")
                    elif cmd.startswith("#reader1 off"):
                        if msg._from in myAdmin:
                            if receiver in tailah["siderTemp"]:
                                del tailah["siderTemp"][receiver]
                                #settings['siderTemp'][receiver]['status'] = False
                                sendFooter(to, "Getreader set to off.")
                    elif cmd.startswith("#reader2 on"):
                        if msg._from in myAdmin:
                          tailah["siderTemp2"][receiver] = []
                          #settings['siderTemp'][receiver]['status'] = True
                          sendFooter(to, "Getreader set to on.")
                    elif cmd.startswith("#reader2 off"):
                        if msg._from in myAdmin:
                            if receiver in tailah["siderTemp2"]:
                                del tailah["siderTemp2"][receiver]
                                #settings['siderTemp'][receiver]['status'] = False
                                sendFooter(to, "Getreader set to off.")
                    elif cmd.startswith("#reader3 on"):
                        if msg._from in myAdmin:
                          tailah["siderTemp3"][receiver] = []
                          #settings['siderTemp'][receiver]['status'] = True
                          sendFooter(to, "Getreader set to on")
                    elif cmd.startswith("#reader3 off"):
                        if msg._from in myAdmin:
                            if receiver in tailah["siderTemp3"]:
                                del tailah["siderTemp3"][receiver]
                                #settings['siderTemp'][receiver]['status'] = False
                                sendFooter(to, "Getreader set to off.")
                    elif cmd.startswith("#reader4 on"):
                        if msg._from in myAdmin:
                          tailah["siderTemp4"][receiver] = []
                          #settings['siderTemp'][receiver]['status'] = True
                          sendFooter(to, "Getreader set to on.")
                    elif cmd.startswith("#reader4 off"):
                        if msg._from in myAdmin:
                            if receiver in tailah["siderTemp4"]:
                                del tailah["siderTemp4"][receiver]
                                #settings['siderTemp'][receiver]['status'] = False
                                sendFooter(to, "Getreader set to off.")
                        elif cmd.startswith("reader msg set ") and sender == noobcoderMID:
                            text_ = removeCmd("reader msg set", text)
                            try:
                                tailah["siderPesan"] = text_
                                sendFooter(to,"Changed to : " + text_)
                            except:
                                sendFooter(to,"Failed to replace message")
                    elif text.lower().startswith("addsb ") and msg._from in myAdmin and to not in chatbot["botOff"]:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            if key1 not in premium['myService']:
                                nama = str(text.split(' ')[1])
                                premium['myService'][key1] =  '%s' % nama
                                midd = noobcoder.getContact(key1)
                                noobcoder.sendMention(to, '@! add to customer sbonly {}'.format(nama),' ',[msg._from])
                            else:
                                noobcoder.sendMessage(to, "Please try expel first, list sb and delsb [num]")
                    elif text.lower().startswith("addajs ") and msg._from in myAdmin and to not in chatbot["botOff"]:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            if key1 not in betamaker['myService']:
                                nama = str(text.split(' ')[1])
                                betamaker['myService'][key1] =  '%s' % nama
                                midd = noobcoder.getContact(key1)
                                noobcoder.sendMention(to, '@! add to customer antijs {}'.format(nama),' ',[msg._from])
                            else:
                                noobcoder.sendMessage(to, "Please try expel first, list ajs and delajs [num]")
                    elif text.lower().startswith("addmeajs ") and msg._from in myAdmin and to not in chatbot["botOff"]:
                            midd = msg._from
                            nama = str(text.split(' ')[1])
                            nick = noobcoder.getContact(midd).displayName
                            if midd in betamaker['myService']:
                               noobcoder.sendMessage(to ,"Please try expel first")
                            else:
                               betamaker['myService'][midd] =  '%s' % nama
                               backupData()
                               noobcoder.sendMention(to, "@! add to customer ajs with user {}".format(nama),"",[msg._from])
                    elif text.lower().startswith("expelmeajs ") and msg._from in myAdmin and to not in chatbot["botOff"]:
                               midd = msg._from
                               nama = str(text.split(' ')[1])
                               nick = noobcoder.getContact(midd).displayName
                               os.system("rm -rf {}".format(nama))
                               os.system("screen -S {} -X quit".format(str(nama)))
                               try:del betamaker['myService'][midd]
                               except:pass
                               backupData()
                               noobcoder.sendMention(to, "@! remove from customer ajs","",[msg._from])
                    elif text.lower() == "auto reboot" and msg._from in betamaker["customer"]  and to not in chatbot["botMute"]:
                               user = betamaker['myService'][msg._from]
                               os.system("screen -S {} -X quit".format(user))
                               os.system('screen -dmS {}'.format(user))
                               os.system('screen -r {} -X stuff "cd {} && python3 selfbot.py \n"'.format(user, user))
                               time.sleep(5)
                               noobcoder.sendMention(to, "@! restarted with user {}".format(user),"",[msg._from])
                               
#============================================================================
                    elif text.lower() == "login sb" and msg._from in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            noobcoder.sendMention(to, '「 Reg Login 」\n• Status : Failed\n• User :  @!\nType  < Logout sb >',' ', [msg._from])
                    elif text.lower().startswith("delfile"):
                        if msg._from in myAdmin:
                            sep = text.split(" ")
                            anu = text.replace(sep[0] + " ","")
                            os.system("screen -S {} -X quit".format(str(anu)))
                            os.system('rm -rf {}'.format(str(anu)))
                            time.sleep(2)
                            noobcoder.sendMessage(to, '「 Delete 」\n• Status : Succes\n• Deleted file : {}'.format(str(anu)))
                    elif text.lower().startswith("addme ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                        if msg._from not in premium['myService']:
                            nama = str(text.split(' ')[1])
                            premium['myService'][msg._from] =  '%s' % nama
                            noobcoder.sendMention(to, "「 Add Me 」 \nAdd @! to Login..","",[msg._from])
                        else:
                            noobcoder.sendMention(msg.to, "「Add Me 」\nOwner @! already in List..","",[msg._from])
                    elif text.lower().startswith("@addme ") and msg._from in myAdmin and to not in chatbot["botMute"]:
                        if msg._from not in java['Service']:
                            nama = str(text.split(' ')[1])
                            java['Service'][msg._from] =  '%s' % nama
                            backupData()
                            noobcoder.sendMention(to, "「 Add Me 」 \nAdd @! to Login..","",[msg._from])
                        else:
                            noobcoder.sendMention(to, "「Add Me 」\nOwner @! already in List..","",[msg._from])
                    elif text.lower().startswith("addsb") and msg._from in myAdmin and to not in chatbot["botOff"]:
                        anu = msg.text.split(" ")
                        anu2 = msg.text.replace(anu[0] + " ","")
                        anu3 = anu2.split("|")
                        nama = str(anu3[0])
                        mid = str(anu3[1])
                        if mid not in premium['myService']:
                            premium['myService'][mid] =  '%s' % nama
                            noobcoder.sendMention(to, '「 Service 」\nAdd @!to service ','', [mid])
                        if mid in premium['myService']:
                            noobcoder.sendMention(to, '「 Service 」\nUser @!already in service  ','', [mid])
                    elif text.lower().startswith("delsb ") and msg._from in myAdmin and to not in chatbot["botOff"]:
                        h = [a for a in premium['myService']]
                        mid = h[int(text.lower().split(' ')[1])-1]
                        user = premium["myService"][mid]
                        if mid in premium['myService'] and mid not in premium['listLogin']:
                            del premium['myService'][mid]
                            noobcoder.sendMention(to, ' Service Delete @!in service ','', [mid])
                        if mid in premium['listLogin']:
                            del premium['listLogin'][mid]
                            del premium['myService'][mid]
                            os.system("screen -S {} -X kill".format(user))
                            os.system('rm -r {}'.format(user))
                        noobcoder.sendMention(to, "User @!has been deleted.","",[mid])                        
                    elif text.lower().startswith("delajs ") and msg._from in myAdmin and to not in chatbot["botOff"]:
                        h = [a for a in betamaker['myService']]
                        mid = h[int(text.lower().split(' ')[1])-1]
                        user = betamaker["myService"][mid]
                        if mid in betamaker['myService'] and mid not in betamaker['listLogin']:
                            del betamaker['myService'][mid]
                            noobcoder.sendMention(to, ' Service Delete @!in service ','', [mid])
                        if mid in betamaker['listLogin']:
                            del betamaker['listLogin'][mid]
                            del betamaker['myService'][mid]
                            os.system("screen -S {} -X kill".format(user))
                            os.system('rm -r {}'.format(user))
                        noobcoder.sendMention(to, "User @!has been deleted.","",[mid])                        

                    elif text.lower() == "list sb" and msg._from in myAdmin and to not in chatbot["botMute"]:
                      if len(premium['myService']) > 0:
                        h = [a for a in premium['myService']]
                        k = len(h)//20
                        for aa in range(k+1):
                            msgas = '「 List sb」\n'
                            no=0
                            for a in h:
                                no+=1
                                if premium['myService'][a] == "":cd = "None."
                                else:cd = premium['myService'][a]
                                if no == len(h):msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                else:msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                            noobcoder.sendMention(to, msgas,'',h)
                      else:
                        noobcoder.sendMessage(to, "「 Empty List 」")
                    elif text.lower() == "list ajs" and msg._from in myAdmin and to not in chatbot["botMute"]:
                      if len(betamaker['myService']) > 0:
                        h = [a for a in betamaker['myService']]
                        k = len(h)//20
                        for aa in range(k+1):
                            msgas = '「 List sb」\n'
                            no=0
                            for a in h:
                                no+=1
                                if betamaker['myService'][a] == "":cd = "None."
                                else:cd = betamaker['myService'][a]
                                if no == len(h):msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                else:msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                            noobcoder.sendMention(to, msgas,'',h)
                      else:
                        noobcoder.sendMessage(to, "「 Empty List 」")
                    elif text.lower() == "logout sb" and msg._from in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            del premium['listLogin'][msg._from]
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('rm -rf {}'.format(str(user)))
                            time.sleep(2)
                            noobcoder.sendMention(to, '「  Logout 」\n> @! LogOut From Selfbot',' ', [msg._from])
                    elif text.lower() == "logout ajs" and msg._from in betamaker['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in betamaker["myService"]:
                            del betamaker['listLogin'][msg._from]
                            user = betamaker["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('rm -rf {}'.format(str(user)))
                            time.sleep(2)
                            noobcoder.sendMention(to, '「  Logout 」\n> @! LogOut From Selfbot',' ', [msg._from])
                    elif text.lower() == "logout sb" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            noobcoder.sendMention(to, '「  Logout 」\nHai @!Sorry Please You Login First By Type < Login sb >',' ', [msg._from])
                    elif text.lower() == "logout ajs" and msg._from not in betamaker['customer'] and to not in chatbot["botMute"]:
                        if msg._from in betamaker["customer"]:
                            noobcoder.sendMention(to, '「  Logout 」\nHai @!Sorry Please You Login First By Type < Start Sb >',' ', [msg._from])
                    elif text.lower() == "restart sb" and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('screen -dmS {}'.format(user))
                            os.system('screen -r {} -X stuff "cd {} && python3 selfbot.py \n"'.format(user, user))
                            time.sleep(3)
                            noobcoder.sendMention(to, '「  Restart Sb  」\n> @! Succes Restart selfbot',' ', [msg._from])
                    elif text.lower().startswith("deldir"):
                        if msg._from in myAdmin:
                            sep = text.split(" ")
                            anu = text.replace(sep[0] + " ","")
                            os.system("screen -S {} -X quit".format(str(anu)))
                            os.system('rm -rf {}'.format(str(anu)))
                            time.sleep(2)
                            noobcoder.sendMention(to, '「 Delete 」\n• Status : Succes\n • User @!\n• Deleted file : {}'.format(str(anu)),' ', [msg._from])
#==========================================
#==========================================
                    elif cmd.startswith("name "):
                        if msg._from in myAdmin:
                            string = removeCmd("name", text)
                            if len(string) <= 10000000000:
                                pname = noobcoder.getContact(sender).displayName
                                profile = noobcoder.getProfile()
                                profile.displayName = string
                                noobcoder.updateProfile(profile)
                                noobcoder.sendMessage(to, "「 Update Name 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                    elif cmd.startswith("status "):
                        if msg._from in myAdmin:
                            string = removeCmd("status", text)
                            if len(string) <= 10000000000:
                                pname = noobcoder.getContact(sender).statusMessage
                                profile = noobcoder.getProfile()
                                profile.statusMessage = string
                                noobcoder.updateProfile(profile)
                                noobcoder.sendMessage(to, "「 Update Status 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                    elif text.lower() == "req login":
                        contact = noobcoder.getContact(sender)
                        owner = "u6e882277271440a7c2e8a2a0a5c38cef"
                        noobcoder.sendContact(owner, "" + str(sender))
                        ayu = "Request Login :\nFrom @!"
                        mid = noobcoder.getContact(sender)
                        mentions(owner, ayu, [sender])
                        noobcoder.sendMessage(owner, "" + str(sender))
                        noobcoder.sendMention(to, "Hi @!\nThe request to enter the selfbots has been sent , please wait for the owner to accept your request","",[msg._from])
                    elif cmd.startswith("chatmaker "):
                        sep = text.split(" ")
                        txt = text.replace(sep[0] + " ","")
                        contact = noobcoder.getContact(sender)
                        owner = "u6e882277271440a7c2e8a2a0a5c38cef"
                        ayu = "Sender: @!"
                        ayu += "\nMessage: {}".format(txt)
                        mentions(owner, ayu, [sender])
                        noobcoder.sendMessage(owner, "" + str(sender))
                        noobcoder.sendMention(to, "Hi @!\nmessage has been send","",[msg._from])
#==========================================
                    elif cmd == "ping":
                        if msg._from in myAdmin:
                            noobcoder.sendMention(to, "PONG ! @!","",[msg._from])
                    elif cmd == "reboot":
                        if msg._from in myAdmin:
                            noobcoder.sendMention(to, "@! Brb , going to pee",' ', [msg._from])
                            restartBot()
                        else:pass
#==========================================
                    elif cmd == "join on":
                        if msg._from in myAdmin:
                            if settings["autoJoin"] == True:
                                msgs=" 「 Join 」\nJoin already Enable♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to Enable♪"
                                settings["autoJoin"] = True
                            sendFooter(to, msgs)
                    elif cmd == "join off":
                        if msg._from in myAdmin:
                            if settings["autoJoin"] == False:
                                msgs=" 「 Join 」\nJoin already DISABLED♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to DISABLED♪"
                                settings["autoJoin"] = False
                            sendFooter(to, msgs)
                    elif cmd.startswith("$"):
                        if msg._from in myAdmin:
                            kntl = removeCmd("$", text)
                            ikkeh = os.popen("{}".format(str(kntl)))
                            enaena = ikkeh.read()
                            noobcoder.sendMessage(to, "{}".format(str(enaena)))
                            ikkeh.close()
                    elif cmd == "screenlist":
                        if msg._from in myAdmin:
                            proses = os.popen("screen -list")
                            a = proses.read()
                            sendFooter(to, "{}".format(str(a)))
                            proses.close()
                    elif cmd.startswith("post"):
                        if msg._from in myAdmin:
                            shar = text.split("-")
                            gs = noobcoder.getGroup(msg.to)
                            jmlh = int(shar[1])
                            sendFooter(to, "Waiting for share.")
                            if jmlh <= 1000:
                                for baba in range(jmlh):
                                    try:
                                        noobcoder.sendPostToTalk(to, str(shar[2]))
                                    except:
                                        pass
                                sendFooter(to, "Sucess")
                            else:
                                sendFooter(to, "Amount is wrong")
                    elif cmd.startswith("postall"):
                        if msg._from in myAdmin:
                            shar = text.split("-")
                            shareall(to, shar[1])
#==========================================
#==========================================
                    elif cmd == "mentions":
                        group = noobcoder.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(noobcoder.getProfile().mid)
                        noobcoder.datamention(to,'Mentions',nama)
#==========================================
#==========================================
                    elif cmd.startswith("cvp"):
                        if msg._from in myAdmin:
                            link = removeCmd("cvp", text)
                            contact = noobcoder.getContact(sender)
                            noobcoder.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = noobcoder.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            time.sleep(2)
                            changeVideoAndPictureProfile(pict, vids)
                            noobcoder.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            os.remove("TeamAnuBot.mp4")                            
#==========================================
                    elif text.lower() == "login" and msg._from not in premium['listLogin'] and to not in chatbot["botMute"]:
                        if msg._from in premium["myService"]:
                            user = premium["myService"][msg._from]
                            try:
                                header = "ios_ipad"
                                auth = "Q541hNgFX1AM"
                                result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header+"&auth="+auth).text)
                                noobcoder.sendMessage(to, "Login IP: {} \nQR Link: {}".format(result["result"]["login_ip"],result["result"]["qr_link"]))
                                result = json.loads(requests.get(result["result"]["callback"]+"&auth="+auth).text)
                                if result["status"] != 200:
                                    raise Exception("Timeout!!!")
                                noobcoder.sendMessage(to, "Pincode: "+result["result"]["pin_code"])
                                result = json.loads(requests.get(result["result"]["callback"]+"&auth="+auth).text)
                                if result["status"] != 200:
                                    raise Exception("Timeout!!!")
                                zzz = result["result"]["token"]
                                if msg._from not in premium['listLogin']:
                                    premium['listLogin'][msg._from] =  '%s' % user
                                    isi = "{}".format(result["result"]["token"])
                                    os.system('cp -r percobaan {}'.format(user))
                                    os.system('cd {} && echo -n "{}" > token1.txt'.format(user, isi))
                                    os.system('screen -dmS {}'.format(user))
                                    os.system('screen -r {} -X stuff "cd {} && python3 staff.py \n"'.format(user, user))
                                    noobcoder.sendMention(to, '「 Login Succes 」\nHello @!\nTemplate link allow kro\nline://app/1643727178-0XPGAaRX?type=text&text=cannibal\nWaiting for 10 sec for activated',' ', [msg._from])
                                    time.sleep(10)
                                    noobcoder.sendMessage(to, 'Type < Help > to see your command')
                                else:
                                    noobcoder.sendMention(to, '「 Request Login 」\n@!\nLink QR Expired -_-',' ', [msg._from])
                            except:
                                noobcoder.sendMention(to, '「  ERROR 」\n@!\nPlease Nonactive Filter Chat Or Letter Sealing -_-',' ', [msg._from])
#==========================================
                        elif cmd.startswith("ulti "):
                          if msg._from in myAdmin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        noobcoder.kickoutFromGroup(to, [ls])
                                        noobcoder.findAndAddContactsByMid(ls)
                                        noobcoder.inviteIntoGroup(to, [ls])
                                        noobcoder.cancelGroupInvitation(to, [ls])
                                    except:
                                       sendFooter(to, "Limited !")
                    elif cmd == "debug":
                       if msg._from in myAdmin:
                            noobcoder.sendMessage(to, debug())
                    elif cmd == "speed":
                        start = time.time()
                        noobcoder.sendMessage("u2cf74acf6ed04d122def4db8ffdd2e39", '</>')
                        elapsed_time = time.time() - start
                        noobcoder.sendMessage(to,"Time:\n%s"%str(round(elapsed_time,5)))
#==========================================
                    elif cmd == "glist":
                       if msg._from in myAdmin:
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = noobcoder.getGroupIdsJoined()
                            sd = noobcoder.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal {} Groups\n\n「 Command 」\n\n> Remote Mention\nUsage: #Glist [num] tag [1|<|>|-]\n\n> Remote Kick\nUsage: #glist [num] kick [1|<|>|-]\n\n> Leave Groups\nUsage: #Leave [num]\n\n> Get QR\nUsage: #Openqr  [num]\n\n> Cek Member\nUsage: #Glist [num]\nUsage: #Glist [num] mem [num]".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} | {}".format(no, G.name[0:20], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
                                noobcoder.generateReplyMessage(msg.id)
                                noobcoder.sendReplyMessage(msg.id, to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))

                    elif cmd.startswith('glist'):
                        if msg._from in myAdmin:
                            to = msg.to
                            gid = noobcoder.getGroupIdsJoined()
                            group = noobcoder.getGroup(gid[int(cmd.split(' ')[1])-1])
                            nama = [a.mid for a in group.members]
                            if len(cmd.split(" ")) == 2:
                                total = "Local ID: {}".format(int(cmd.split(' ')[1]))
                                noobcoder.datamention(to,'List Member',nama,'\n├Group: '+group.name[:20]+'\n├'+total)
                            if len(cmd.split(" ")) == 4:
                                if cmd.startswith('glist '+cmd.split(' ')[1]+' mem '):noobcoder.getinformation(to,nama[int(cmd.split(' ')[3])-1],wait)
                                if cmd.startswith('glist '+cmd.split(' ')[1]+' tag'):noobcoder.adityaarchi(wait,'Mention','tag',gid[int(cmd.split(' ')[1])-1],cmd.split(' ')[3],msg,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(cmd.split(' ')[1])),nama=nama)
                                if cmd.startswith('glist '+cmd.split(' ')[1]+' kick'):noobcoder.adityaarchi(wait,'Kick Member','kick',gid[int(cmd.split(' ')[1])-1],cmd.split(' ')[3],msg,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(cmd.split(' ')[1])),nama=nama)
                    if cmd.startswith("leave groups "):
                        if msg.toType in [0,1,2]:
                            gid = noobcoder.getGroupIdsJoined()
                            if len(cmd.split(" ")) == 3:
                                selection = MySplit(cmd.split(' ')[2],range(1,len(gid)+1))
                                k = len(gid)//100
                                for a in range(k+1):
                                    if a == 0:eto='╭「 Leave Group 」─'
                                    else:eto='├「 Leave Group 」─'
                                    text = ''
                                    no = 0
                                    for i in selection.parse()[a*100 : (a+1)*100]:
                                        noobcoder.leaveGroup(gid[i - 1])
                                        no+=1
                                        if no == len(selection.parse()):text+= "\n╰{}. {}".format(i,noobcoder.getGroup(gid[i - 1]).name)
                                        else:text+= "\n│{}. {}".format(i,noobcoder.getGroup(gid[i - 1]).name)
                                    noobcoder.sendMessage(to,eto+text)
                    elif cmd.startswith("gcast "):
                      if msg._from in myAdmin:
                            txt = removeCmd("gcast", text)
                            groups = noobcoder.getGroupIdsJoined()
                            for group in groups:
                                sendFooter1(group, "「 Group Broadcast 」\n{}".format(str(txt)))
                                time.sleep(1)
                            sendFooter(to, "Succes broadcast to {} group".format(str(len(groups))))
                    elif cmd.startswith('joinme '):
                         if msg._from in myAdmin:
                             text = msg.text.split()
                             number = text[1]
                             if number.isdigit():
                              groups = noobcoder.getGroupIdsJoined()
                              if int(number) < len(groups) and int(number) >= 0:
                                  groupid = groups[int(number)]
                                  group = noobcoder.getGroup(groupid)
                                  target = sender
                                  try:
                                      noobcoder.getGroup(groupid)
                                      noobcoder.findAndAddContactsByMid(target)
                                      noobcoder.inviteIntoGroup(groupid, [target])
                                      noobcoder.sendMessage(msg.to,"Succes invite to " + str(group.name))
                                  except:
                                      noobcoder.sendMessage(msg.to,"I no there baby")

                    elif cmd.startswith('invme '):
                         if msg._from in myAdmin:
                             cond = cmd.split(" ")
                             num = int(cond[1])
                             gid = noobcoder.getGroupIdsJoined()
                             group = noobcoder.getCompactGroup(gid[num-1])
                             noobcoder.findAndAddContactsByMid(sender)
                             noobcoder.inviteIntoGroup(gid[num-1],[sender])

                    elif cmd.startswith("openqr "):
                      if msg._from in myAdmin:
                            number = removeCmd("openqr", text)
                            groups = noobcoder.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = noobcoder.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = False
                                    noobcoder.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(noobcoder.reissueGroupTicket(G.id)))
                                except:
                                    G.preventedJoinByTicket = False
                                    noobcoder.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(noobcoder.reissueGroupTicket(G.id)))
                                sendFooter1(to, "「 Open Qr 」\n\nGroup : " + G.name + "\nLink: " + gurl)
                            except Exception as error:
                                noobcoder.sendMessage(to, str(error))
                    elif cmd == "/byeall":
                        if msg._from in myAdmin:
                            anu = noobcoder.getGroupIdsJoined()
                            for i in anu:
                                try:
                                    noobcoder.leaveGroup(i)
                                except Exception as e:
                                    noobcoder.sendMessage(msg.to, e)
                        else:noobcoder.sendMention(msg.to, "Lo siapa sih @!NGENTOT!!!","SIKONTOL",' ', [msg._from])
                    elif cmd.startswith("mid "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = "Pencolongan mid"
                                for ls in lists:
                                    ret_ += "\n\n{}".format(str(ls))
                                noobcoder.generateReplyMessage(msg.id)
                                noobcoder.sendReplyMessage(msg.id, to, str(ret_))
                    elif cmd == "reader":
                            ret = " 🦂 reader1 on\n"
                            ret += " 🦂 Reader1 off\n"
                            ret += " 🦂 reader2 on\n"
                            ret += " 🦂 reader2 off\n"
                            ret += " 🦂 reader3 on\n"
                            ret += " 🦂 reader3 off\n"
                            ret += " 🦂 reader4 on\n"
                            ret += " 🦂 reader4 off\n"
                            ret += " 🦂 reader msg set \n"
                            #ret += " 🦂 Change help1\n"
                            #ret += " 🦂 Change help2\n"
                            #ret += " 🦂 Change help3\n"
                            #ret += " 🦂 Change me\n"
                            #ret += " 🦂 Change about"
                            mosing(to, str(ret))
                    elif cmd == 'helper':hehehe1(to)
                    elif cmd == "helpercek":
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2018 
                                bln = 8    #isi bulannya yg sewa
                                hr = 9   #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                h = noobcoder.getContact(noobcoderMID)
                                groups = noobcoder.getGroupIdsJoined()
                                contactlist = noobcoder.getAllContactIds()
                                kontak = noobcoder.getContacts(contactlist)
                                favorite = noobcoder.getFavoriteMids()
                                blockedlist = noobcoder.getBlockedContactIds()
                                kontak2 = noobcoder.getContacts(blockedlist)
                                fil = noobcoder.getSettings().privacyReceiveMessagesFromNotFriend
                                seal = noobcoder.getSettings().e2eeEnable
                                src = noobcoder.getSettings().privacySearchByUserid
                                status = {"kick": "", "invite": ""}
                                try:noobcoder.kickoutFromGroup(to, [noobcoderMID]);status["kick"] = "Normal"
                                except:status["kick"] = "Limit"
                                try:noobcoder.inviteIntoGroup(to, [noobcoderMID]);status["invite"] = "Normal"
                                except:status["invite"] = "Limit"
                                if src == True:alid = "Add From LineID : True"
                                else:alid = "Add From LineID : False"                            
                                if seal == True:letsel = "Letter Sealing : True"
                                if seal == False:letsel = "Letter Sealing : False"
                                if fil == True:fpes = "Filter Message : False"
                                if fil == False:fpes = "Filter Message : True"
                                ret_ = "About noobcoder :\n"
                                ret_ += "\nnoobcoder : {}".format(h.displayName)
                                ret_ += "\nGroup : {}".format(str(len(groups)))
                                ret_ += "\nFriend : {}".format(str(len(kontak)))
                                ret_ += "\nFavorite: {}".format(str(len(favorite)))
                                ret_ += "\nBlocked : {}".format(str(len(kontak2)))
                                ret_ += "\nChat Send: {}".format(str(peler["sendcount"]))
                                ret_ += "\nChat Received : {}".format(str(peler["receivercount"]))
                                ret_ += "\n{}".format(alid)
                                ret_ += "\n{}".format(letsel)
                                ret_ += "\n{}".format(fpes)
                                ret_ += "\nKick : %s" % status["kick"]
                                ret_ += "\nInvite : %s" % status["invite"]
                                ret_ += "\n\n< About Bots >\n"
                                ret_ += "\nType : Selfbot"
                                ret_ += "\nVersion : V.09\n"
                                ret_ += "\nMaker :  ☞︎ 🇶🇦⃤𝘽𝙊𝙏𝙎 ● 𝗞𝗚𝗧 🇸🇦⃤☜"
                                sendFooter(to, str(ret_))
                            except Exception as e:
                                noobcoder.sendMessage(to, str(e))
                    elif cmd.startswith("clearflex"):
                        if msg._from in myAdmin:
                            clearSteals()
                            noobcoder.sendMessage(to, "Data flex message is cleared now & set to off.")
                    elif cmd.startswith("seeflex "):
                        if msg._from in myAdmin:
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = [] 
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            if lists != []:
                              for x in lists:
                                appendSteals(x)
                              sendFooter(to, "Waiting target send flex message!")   
                    elif cmd == "vps":
                            ac = subprocess.getoutput('lsb_release -a')
                            am = subprocess.getoutput('cat /proc/meminfo')
                            ax = subprocess.getoutput('lscpu')
                            core = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')
                            python_imp = platform.python_implementation()
                            python_ver = platform.python_version()
                            for line in ac.splitlines():
                                if 'Description:' in line:
                                    osi = line.split('Description:')[1].replace('  ','')
                            for line in ax.splitlines():
                                if 'Architecture:' in line:
                                    architecture =  line.split('Architecture:')[1].replace(' ','')
                            for line in am.splitlines():
                                if 'MemTotal:' in line:
                                    mem = line.split('MemTotal:')[1].replace(' ','')
                                if 'MemFree:' in line:
                                    fr = line.split('MemFree:')[1].replace(' ','')
                            md = "⚒️ System\n\n"
                            md +="OS: {}\n".format(osi)
                            md +="Lang: {}\n".format(python_imp)
                            md +="Ver: {}\n".format(python_ver)
                            md +="Architecture: {}\n".format(architecture)
                            md +="CPU Core: {}\n".format(core)
                            md +="Memory: {}\n".format(mem)
                            md +="Free: {}".format(fr)
                            sendFooter(to,md)
                        
                            
                    elif cmd.startswith("ipc "):
                            search = removeCmd("ipc", text)
                            r = _session.get("https://ipapi.co/" + search + "/json")
                            data = r.text
                            data = json.loads(data)
                            if "error" not in data:
                                ret_ = "IP Checker :\n"
                                ret_ += "\nIp : {}".format(data["ip"])
                                ret_ += "\nCity : {}".format(data["city"])
                                ret_ += "\nRegion : {}".format(data["region"])
                                ret_ += "\nRegion Code : {}".format(data["region_code"])
                                ret_ += "\nCountry : {}".format(data["country"])
                                ret_ += "\nCountry Name : {}".format(data["country_name"])
                                ret_ += "\nPostal : {}".format(data["postal"])
                                ret_ += "\nLatitude : {}".format(data["latitude"])
                                ret_ += "\nLongitude : {}".format(data["longitude"])
                                ret_ += "\nTimezone : {}".format(data["timezone"])
                                ret_ += "\nASN Code : {}".format(data["asn"])
                                ret_ += "\nOrganization : {}".format(data["org"])
                                sendFooter(msg.to,str(ret_))
                            else:
                                noobcoder.sendMessage(to, "IP not found !")   
                    elif cmd == "hmm":
                        if msg._from in myAdmin:
                            helppss(to)
                    if text.lower() == "rname":
                        if msg._from in myAdmin:
                            key = settings["keyCommand"]
                            if settings["setKey"] == True:
                                statuskey = "Enabled"
                            else:
                                statuskey = "Disabled"
                            sendFooter(to, "⌬ Rname : "+str(key.title())+"\n⌬ Status : "+str(statuskey))
                    if "u" in text.lower():
                        mid = re.compile(r'u\w{32}')
                        mymid = mid.findall(text)
                        print(mymid)
                        n_links = []                            
                        for l in mymid:
                            if l not in n_links:
                                n_links.append(l)
                        if n_links == []:
                            pass
                        else:
                            no = 0
                            ret = "List Mids :\n"
                            for midd in n_links:
                                noobcoder.sendContact(to, midd)
                                kontak = noobcoder.getContact(midd)
                                nama = kontak.displayName
                                no += 1
                                ret += "\n" + str(no) + ". " + str(midd[:4]) + " - " + str(nama)
                            ret += "\n\nTotal {} Mids".format(str(len(n_links)))
                            k = len(ret)//10000
                            for aa in range(k+1):
                                noobcoder.sendMessage(to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                    if cmd == "me":
                        
                                contact = noobcoder.getContact(sender)
                                groups = noobcoder.getGroupIdsJoined()
                                contactz = noobcoder.getAllContactIds()
                                blockeds = noobcoder.getBlockedContactIds()
                                coverUrl = noobcoder.getProfileCoverURL(sender)
                                bio = contact.statusMessage
                                print(bio)
                                LINKFOTO = "https://os.line.naver.jp/os/p/{}".format(sender)
                                data={"type":"flex","altText":gwcool["squad"],"contents":{
  "type": "bubble",
  "size": "kilo",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "paddingAll": "0px",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "borderWidth": "3px",
        "borderColor": "#C123D9FF",
        "cornerRadius": "10px",
        "contents": [
          {
            "type": "image",
            "url": "https://b.top4top.io/p_1844zwtck1.jpg",
            "size": "full",
            "aspectRatio": "13:16",
            "aspectMode": "cover"
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "35px",
            "offsetEnd": "4px",
            "width": "244px",
            "height": "225px",
            "cornerRadius": "4px",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus), 
                "size": "full",
                "aspectMode": "cover"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "9px",
            "offsetEnd": "15px",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "10px",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus), 
                "size": "full",
                "aspectMode": "cover"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "12px",
            "offsetEnd": "40px",
            "width": "100px",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(contact.displayName),
                "size": "xxs",
                "color": "#000000FF",
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "170px",
            "width": "100px",
            "contents": [
              {
                "type": "image",
                "url": "https://f.top4top.io/p_1844cy2t11.png",
                "size": "full",
                "aspectMode": "cover"
              }
            ]
          }
        ]
      }
    ]
  }
}
} 
                                sendTemplate(to,data)
                    if cmd == "me3":
                        if msg._from in myAdmin:
                                contact = noobcoder.getContact(sender)
                                groups = noobcoder.getGroupIdsJoined()
                                contactz = noobcoder.getAllContactIds()
                                blockeds = noobcoder.getBlockedContactIds()
                                coverUrl = noobcoder.getProfileCoverURL(sender)
                                bio = contact.statusMessage
                                print(bio)
                                LINKFOTO = "https://os.line.naver.jp/os/p/{}".format(sender)
                                data={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
  "type": "bubble",
  "size": "kilo",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "paddingAll": "0px",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://f.top4top.io/p_18430pnd01.jpg",
            "size": "full",
            "aspectRatio": "9:16",
            "aspectMode": "cover"
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "93px",
            "offsetEnd": "5px",
            "width": "247px",
            "height": "310px",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus), 
                "size": "full",
                "aspectMode": "cover"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "58px",
            "offsetStart": "5px",
            "width": "30px",
            "height": "30px",
            "cornerRadius": "25px",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectMode": "cover"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "61px",
            "offsetStart": "40px",
            "width": "200px",
            "height": "22px",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(contact.displayName),
                "align": "start",
                "contents": []
              }
            ]
          }
        ]
      }
    ]
  }
}
  }
                                sendTemplate(to,data)
                    if cmd == "me5":
                        if msg._from in myAdmin:
                                contact = noobcoder.getContact(sender)
                                groups = noobcoder.getGroupIdsJoined()
                                contactz = noobcoder.getAllContactIds()
                                blockeds = noobcoder.getBlockedContactIds()
                                coverUrl = noobcoder.getProfileCoverURL(sender)
                                bio = contact.statusMessage
                                print(bio)
                                LINKFOTO = "https://os.line.naver.jp/os/p/{}".format(sender)
                                data={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
      "header": {
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            
            "contents": [
              {
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "9:16",
                "url": "https://b.top4top.io/p_1843g6qzm1.jpg",
                "type": "image"
              },
              {
                "width": "160px",
                "offsetStart": "50px",
                "type": "box",
                "layout": "vertical",
                "position": "absolute",
                "offsetTop": "110px",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                    "size": "full",
                    "aspectMode": "cover"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    
                    "contents": [
                      {
                        "text": "{}".format(contact.displayName),
                        "contents": [],
                        "color": "#FFFFFFFF",
                        "type": "text",
                        "size": "xxs",
                        "align": "center"
                      },
                      {
                        "contents": [],
                        "size": "xxs",
                        "color": "#FFFFFFFF",
                        "text": bio,
                        "type": "text",
                        "align": "center"
                      }
                    ],
                    "paddingAll": "1px"
                  }
                ],
                "backgroundColor": "#000000FF",
                "height": "200px"
              }
            ],
            "layout": "vertical"
          }
        ],
        "paddingAll": "0px",
        "type": "box"
      },
      "type": "bubble",
      "direction": "ltr",
      "size": "kilo"
    }
  }
                                sendTemplate(to,data)
                    if cmd == "me2":
                        if msg._from in myAdmin:
                                contact = noobcoder.getContact(sender)
                                groups = noobcoder.getGroupIdsJoined()
                                contactz = noobcoder.getAllContactIds()
                                blockeds = noobcoder.getBlockedContactIds()
                                coverUrl = noobcoder.getProfileCoverURL(sender)
                                bio = contact.statusMessage
                                print(bio)
                                LINKFOTO = "https://os.line.naver.jp/os/p/{}".format(sender)
                                data={"type":"flex","altText":gwcool["squad"],"contents":{
  "type": "bubble",
  "size": "kilo",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "paddingAll": "0px",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://h.top4top.io/p_18434afuv1.jpg",
            "size": "full",
            "aspectRatio": "9:16",
            "aspectMode": "cover"
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "77px",
            "offsetEnd": "24px",
            "width": "215px",
            "height": "270px",
            "borderWidth": "2px",
            "borderColor": "#040101CC",
            "cornerRadius": "6px",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "9:16",
                "aspectMode": "cover"
              },
              {
                "type": "box",
                "layout": "vertical",
                "position": "absolute",
                "offsetTop": "210px",
                "paddingAll": "2px",
                "width": "211px",
                "height": "56px",
                "backgroundColor": "#0E0113A0",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(contact.displayName),
                    "size": "xs",
                    "color": "#FFFFFFFF",
                    "contents": []
                  },
                  {
                    "type": "text",
                    "text": bio,
                    "size": "xxs",
                    "color": "#FFFFFFFF",
                    "wrap": True,
                    "contents": []
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
} 
                                sendTemplate(to,data)
                    if text.lower() == "rname on":
                        if msg._from in myAdmin:
                            settings["setKey"] = True
                            sendFooter(to, "Rname has been enabled")
                    if text.lower() == "rname off":
                        if msg._from in myAdmin:
                            settings["setKey"] = False
                            sendFooter(to, "Rname has been disabled")
#==========================================
##paste
                        elif cmd.startswith("flexgbc2 "):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            groups = noobcoder.getGroupIdsJoined()
                            for gr in groups:
                                data = {
    "type": "flex",
    "altText": "متمردهIQ🍸™",
    "contents": {
        "type": "bubble",
        "size": "giga",
        "direction": "rtl",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [{
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [{
                            "type": "box",
                            "layout": "vertical",
                            "contents": [{
                                "type": "image",
                                "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(sender).pictureStatus),
                                "aspectMode": "cover",
                                "size": "full"
                            }],
                            "cornerRadius": "100px",
                            "width": "72px",
                            "height": "72px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [{
                                    "type": "text",
                                    "contents": [{
                                        "type": "span",
                                        "text": "{}".format(text),
                                        "size": "lg",
                                        "color": "#000000",
                                        "weight": "regular",
                                        "style": "normal",
                                        "decoration": "none"
                                    }],
                                    "size": "sm",
                                    "wrap": True
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [{
                                        "type": "text",
                                        "text": "{}".format(noobcoder.getContact(sender).displayName),
                                        "size": "xxl",
                                        "color": "#000000",
                                        "weight": "bold",
                                        "style": "normal",
                                        "decoration": "none",
                                        "position": "relative"
                                    }],
                                    "spacing": "sm",
                                    "margin": "lg",
                                    "position": "relative"
                                }
                            ],
                            "position": "relative",
                            "margin": "md"
                        }
                    ],
                    "spacing": "xl",
                    "paddingAll": "20px",
                    "margin": "md"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [{
                        "type": "box",
                        "layout": "vertical",
                        "contents": [{
                            "type": "image",
                            "url": "{}".format(noobcoder.getProfileCoverURL(sender)),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "150:98",
                            "gravity": "center"
                        }],
                        "flex": 1
                    }]
                }
            ],
            "paddingAll": "0px"
        },
        "styles": {
            "body": {
                "separator": True
            }
        }
    }
}
                                bcTemplate(gr, data)
                                time.sleep(2)
                            noobcoder.sendMessage(to, "Succes broadcast to {} group".format(str(len(groups))))
                                ##paste
                        elif cmd.startswith("tweet "):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            data={"type":"flex","altText":gwcool["squad"],"contents":{
        "body": {
            "contents": [
                {
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "aspectRatio": "5:1",
                            "size": "full",
                            "type": "image",
                            "url": "https://imagizer.imageshack.com/img923/1734/iz9aRh.png"
                        }
                    ],
                    "layout": "vertical",
                    "type": "box"
                },
                {
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "aspectRatio": "1:1",
                            "size": "xs",
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(noobcoder.getContact(noobcoderMID).pictureStatus)
                        }
                    ],
                    "cornerRadius": "100px",
                    "layout": "vertical",
                    "offsetStart": "15px",
                    "offsetTop": "13px",
                    "position": "absolute",
                    "type": "box"
                },
                {
                    "contents": [
                        {
                            "color": "#ffffff",
                            "size": "xs",
                            "text": "{}".format(noobcoder.getContact(noobcoderMID).displayName),
                            "type": "text",
                            "weight": "bold"
                        },
                        {
                            "color": "#84929b",
                            "size": "xs",
                            "text": "@{}".format(gwcool["squad"]),
                            "type": "text"
                        }
                    ],
                    "layout": "vertical",
                    "offsetStart": "87px",
                    "offsetTop": "23px",
                    "position": "absolute",
                    "type": "box"
                },
                {
                    "contents": [
                        {
                            "color": "#ffffff",
                            "size": "xl",
                            "text": "{}".format(text),
                            "type": "text",
                            "wrap": True
                        }
                    ],
                    "layout": "vertical",
                    "paddingBottom": "10px",
                    "paddingEnd": "15px",
                    "paddingStart": "15px",
                    "paddingTop": "22px",
                    "type": "box"
                },
                {
                    "contents": [
                        {
                            "aspectMode": "cover",
                            "aspectRatio": "5:1",
                            "size": "full",
                            "type": "image",
                            "url": "https://imagizer.imageshack.com/img924/1714/K1ABpF.png"
                        }
                    ],
                    "layout": "vertical",
                    "offsetStart": "5px",
                    "type": "box"
                }
            ],
            "layout": "vertical",
            "paddingAll": "0px",
            "type": "box"
        },
        "styles": {
            "body": {
                "backgroundColor": "#0f2028"
            }
        },
        "type": "bubble"
    },
    "type": "flex"
}
                            sendTemplate(to, data)
                                
                        elif cmd.startswith("flexgbc "):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            groups = noobcoder.getGroupIdsJoined()
                            for gr in groups:
                                data = {
        "type": "flex",
        "altText": "king",
        "contents": {
            "type": "carousel",
            "contents": [
              {
                "type": "bubble",
                "body": {
                "type": "box",
                "layout": "vertical",
                "cornerRadius": "xl",
                "borderWidth": "4px",
                "borderColor": "#FFFFFF",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "1:1",
                    "gravity": "top"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                          {
                            "type": "text",
                            "text": "{}".format(text),
                            "wrap": True,
                            "color": "#ffffff",
                            "size": "sm",
                            "flex": 0
                          }
                        ],
                        "spacing": "lg"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "filler"
                          },
                          {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                              {
                                "type": "filler"
                              },
                              {
                                "type": "text",
                                "text": "king",
                                "weight": "bold",
                                "action": {
                                  "type": "uri",
                                  "uri": "https://line.me/ti/p/~" + noobcoder.profile.userid
                                },
                                "color": "#ffffff",
                                "flex": 0,
                                "offsetTop": "-2px"
                              },
                              {
                                "type": "filler"
                              }
                            ],
                            "spacing": "sm"
                          },
                          {
                            "type": "filler"
                          }
                        ],
                        "borderWidth": "1px",
                        "cornerRadius": "4px",
                        "spacing": "sm",
                        "borderColor": "#ffffff",
                        "margin": "xxl",
                        "height": "40px"
                      }
                    ],
                    "position": "absolute",
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "backgroundColor": "#000000cc",
                    "paddingAll": "20px",
                    "paddingTop": "18px"
                  }
                ],
                "paddingAll": "0px"
            }
          } 
        ]
      } 
    }
                                bcTemplate(gr, data)
                                time.sleep(1)
                            noobcoder.sendMessage(to, "Succes broadcast to {} group".format(str(len(groups))))
#==========================================
        if op.type == 55:
            if op.param1 in tailah["siderTemp4"] and op.param2 not in tailah["siderTemp4"][op.param1]:
                tailah["siderTemp4"][op.param1].append(op.param2)
                if "@!" in settings["readerPesan"]:
                    contact = noobcoder.getContact(op.param2)
                    cover = noobcoder.getProfileCoverURL(op.param2)
                    pesan = tailah["siderPesan"]
                    data={
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
  "type": "bubble",
  "size": "micro",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "paddingAll": "0px",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://b.top4top.io/p_1843eajrb1.jpg",
            "size": "full",
            "aspectRatio": "9:16",
            "aspectMode": "cover"
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "30px",
            "offsetEnd": "17px",
            "width": "125px",
            "height": "125px",
            "cornerRadius": "12px",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectMode": "cover"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "width": "160px",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(contact.displayName),
                "size": "xxs",
                "color": "#FFFFFF9E",
                "align": "center",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "183px",
            "width": "160px",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(pesan),
                "size": "xxs",
                "color": "#FFFFFF9E",
                "align": "center",
                "contents": []
              }
            ]
          }
        ]
      }
    ]
  }
}
  }
                    sendTemplate(op.param1,data)
            if op.param1 in tailah["siderTemp"] and op.param2 not in tailah["siderTemp"][op.param1]:
                tailah["siderTemp"][op.param1].append(op.param2)
                if "@!" in settings["readerPesan"]:
                    group = noobcoder.getGroup(op.param1)
                    contact = noobcoder.getContact(op.param2)
                    pesan = tailah["siderPesan"]
                    data={"type":"flex","altText":gwcool["squad"],"contents":{
  "type": "bubble",
  "size": "micro",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "paddingAll": "0px",
    "borderWidth": "3px",
    "backgroundColor": "#FFFFFFFF",
    "borderColor": "#F300D5A0",
    "cornerRadius": "8px",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://g.top4top.io/p_1844uk6f81.jpg",
            "size": "full",
            "aspectRatio": "9:16",
            "aspectMode": "cover"
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "28px",
            "offsetEnd": "24px",
            "width": "110px",
            "height": "190px",
            "borderWidth": "5px",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectMode": "cover"
              },
              {
                "type": "box",
                "layout": "vertical",
                "position": "absolute",
                "offsetTop": "85px",
                "width": "100px",
                "backgroundColor": "#F300D5A0",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(contact.displayName),
                    "size": "xxs",
                    "color": "#FFFFFFFF",
                    "align": "center",
                    "contents": []
                  }
                ]
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "257px",
            "width": "154px",
            "height": "30px",
            "backgroundColor": "#F300D5A0",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(pesan),
                "size": "xs",
                "color": "#FFFFFFFF",
                "align": "center",
                "contents": []
              }
            ]
          }
        ]
      }
    ]
  }
}
} 
                    sendTemplate(op.param1,data)    
        if op.type == 55:
            if op.param1 in tailah["siderTemp3"] and op.param2 not in tailah["siderTemp3"][op.param1]:
                tailah["siderTemp3"][op.param1].append(op.param2)
                if "@!" in settings["readerPesan"]:
                    contact = noobcoder.getContact(op.param2)
                    pesan = tailah["siderPesan"]
                    data={"type":"flex","altText":gwcool["squad"],"contents":{
  "type": "bubble",
  "size": "kilo",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "paddingAll": "0px",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i2.wp.com/iphoneislam.com/wp-content/uploads/2018/05/the_x_love_and_tears2-crunch.png?resize=240%2C520&ssl=1",
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "30px",
            "offsetStart": "30px",
            "width": "200px",
            "height": "200px",
            "contents": [
              {
                "type": "image",
                "url": "https://k.top4top.io/p_1844ev1cr2.png",
                "size": "full",
                "aspectMode": "cover"
              },
              {
                "type": "box",
                "layout": "vertical",
                "position": "absolute",
                "offsetTop": "55px",
                "offsetEnd": "49px",
                "width": "94px",
                "height": "94px",
                "cornerRadius": "75px",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                    "size": "full",
                    "aspectMode": "cover"
                  }
                ]
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "200px",
            "offsetStart": "10px",
            "width": "100px",
            "backgroundColor": "#FCB2BBCE",
            "cornerRadius": "25px",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(contact.displayName),
                "size": "xs",
                "color": "#62000CFF",
                "align": "center",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "220px",
            "offsetEnd": "10px",
            "width": "150px",
            "backgroundColor": "#FCB2BBCE",
            "cornerRadius": "25px",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(pesan),
                "size": "xs",
                "color": "#62000CFF",
                "align": "center",
                "contents": []
              }
            ]
          }
        ]
      }
    ]
  }
}
  }
                    sendTemplate(op.param1, data)
            if op.param1 in tailah["siderTemp2"] and op.param2 not in tailah["siderTemp2"][op.param1]:
                tailah["siderTemp2"][op.param1].append(op.param2)
                if "@!" in settings["readerPesan"]:
                    contact = noobcoder.getContact(op.param2)
                    cover = noobcoder.getProfileCoverURL(op.param2)
                   # gifna = ("","https://i.ibb.co/wCsmyFL/a85c8cd8276f678176a69788cd259efe.png","https://i.ibb.co/CsGFJFg/a85c8cd8276f678176a69788cd259efe.png","https://i.ibb.co/Rvhtj7X/a85c8cd8276f678176a69788cd259efe.png","https://i.ibb.co/4F12NSx/a85c8cd8276f678176a69788cd259efe.png","https://i.ibb.co/KKbkPCD/a85c8cd8276f678176a69788cd259efe.png","https://i.ibb.co/vxNLd3k/a85c8cd8276f678176a69788cd259efe.png","https://i.ibb.co/4YFqvkR/a85c8cd8276f678176a69788cd259efe.png")
                    # gifnay = random.choice(gifna)
                    pesan = tailah["siderPesan"]
                    data = {
                        "type": "flex",
                        "altText":"Reader",
                        "contents": {
                          "type": "bubble",
  "size": "micro",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "vertical",
    "paddingAll": "0px",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": cover,
            "size": "full",
            "aspectRatio": "9:16",
            "aspectMode": "cover"
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "60px",
            "offsetStart": "10px",
            "width": "140px",
            "contents": [
              {
                "type": "image",
                "url": "https://up4net.com/uploads3/up4net-1611170228343.png",
                "size": "full",
                "aspectMode": "cover"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "92px",
            "offsetStart": "22px",
            "width": "115px",
            "height": "64px",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectMode": "cover"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "position": "absolute",
            "offsetTop": "215px",
            "width": "160px",
            "height": "80px",
            "backgroundColor": "#290E1996",
            "contents": [
              {
                "type": "text",
                "text": "Hello , {}".format(contact.displayName),
                "size": "xs",
                "color": "#FFFFFFFF",
                "align": "center",
                "contents": []
              },
              {
                "type": "text",
                "text": "-------------------------------",
                "size": "xxs",
                "color": "#FFFFFFFF",
                "align": "center",
                "wrap": True ,
                "contents": []
              },
              {
                "type": "text",
                "text": "{}".format(pesan),
                "size": "xxs",
                "color": "#FFFFFFFF",
                "align": "center",
                "contents": []
              }
            ]
          }
        ]
      }
    ]
  }
}
} 
                    sendTemplate(op.param1, data)
        if op.type == 55:                
            if op.param1 in read["readPoint"]:
                _name = noobcoder.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
#==========================================

        if op.type == 55:
            print("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in wait['readPoint']:
                    if op.param2 in wait['ROM1'][op.param1]:
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                    else:
                        wait['ROM1'][op.param1][op.param2] = op.param2
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                        try:
                            if wait['lurkauto'] == True:
                                if len(wait['setTime'][op.param1]) % 5 == 0:
                                    anulurk(op.param1,wait)
                        except:pass
                elif op.param2 in wait['readPoints']:
                    wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                    wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
                else:pass
            except:
                pass
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
    
def run():
    while True:
        try:
            ops = noobcoderPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(noobcoderBot(op))
                   noobcoderPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()
