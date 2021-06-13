from bs4 import BeautifulSoup as Soup
import requests as Req
import json

class Rensmt_smule:
	def getInfo(user):
		"""
		FOR PYTHON 3.6+
		Created by Rensmt
		Lineid: ecaamt
		"""
		url = f"https://www.smule.com/{user}"
		r = Req.get(url)
		if r.status_code != 200:
			return "user_not_found"
		s = Soup(r.text, 'html.parser')
		uwujson = str(s).split("Profile: ")[1].split(",\n")[0]
		json_obj = json.loads(uwujson)
		return json_obj
	def creatorInfo():
		creator = """
			Rensmt Corporation
			Line id: line://ti/p/~ecaamt
			Smule V1
			Complete results With 100% Worked
		"""
		return creator