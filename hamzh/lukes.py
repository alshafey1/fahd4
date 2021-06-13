from bs4 import BeautifulSoup as Soup
import requests as Req
import json

class Lukes_twitter:
	def getInfo():
		"""
		FOR PYTHON 3.6+
		Created by Rensmt
		Lineid: ecaamt
		"""
		user = input("Id: ")
		url = f"https://mobile.twitter.com/{user}"
		r = Req.get(url)
		if r.status_code != 200:
			return "user_not_found"
		s = Soup(r.text, 'html.parser')
		uwujson = str(s).split("Profile: ")[1].split(",\n")[0]
		json_obj = json.loads(uwujson)
		return json_obj
	def creatorInfo():
		creator = """
			Lukes
			Line id: line://ti/p/~orangtampan.no1
			On Development
			Complete results With 100% Worked
		"""
		return creator