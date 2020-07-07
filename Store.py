from bs4 import BeautifulSoup
import requests
import random
import docx


def save():
	with open('Horror Story.doc', 'w') as file:
		file.write(f'\t\t\t\tНазвание истории - {story["title"].upper()}\n{story["text"]}')


def parserPage():
	link_list = ['hameleon.html', 'arina.html', 'dzhinsyubiycy.html', 'klub_vorov.html', 'uchitelynica_veshey.html', 'supersila.html', 'feysid.html', 'koronavirus.html', 'rodimoe_pyatno.html', 'chernaya_sestra.html', 'puteschestvie_duschi.html', 
				 'golubi.html', 'karmannye_denygi.html']
	URL = 'http://prizraka.net/' + random.choice(link_list)
	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')

	items = soup.findAll('body')

	stories = []

	for item in items:
		stories.append({
			'title': item.find('h1').get_text(strip = True),
			'text': item.find('div', class_ = 'oolktext').get_text(strip = True)
			})

		global story
		for story in stories:
			print(f'\t\t\t\t\t\tНазвание истории - {story["title"].upper()}\n{story["text"]}')
			save()

parserPage()