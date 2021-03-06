import urlparse
import urllib
import parser
from bs4 import BeautifulSoup

"""
Scrapes data from the calDining page. Creates a list of Food objects that contain fat, protein, carbs, and calories as floats.
Returns a tuple (foodlist, dictionary)
Dictionary is in the form fooddict[NAME] = [fat, carbs, protein, calories]

"""
#calorie_text = []
#nutrition = {}

def run():
	dictFood={}
	foodlist = []
	url = "http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp"
	urls = [url]
	visited = [url]
	i = 0

	while len(urls) > 0:
		try:
			htmltext = urllib.urlopen(urls[0]).read()
					#Opens the url
		except:
			print("Error")
			print(urls[0])
		soup = BeautifulSoup(htmltext)
		urls.pop(0)



		for link in soup.find_all('a',href=True):
			link['href'] = urlparse.urljoin(url,link['href'])

			if "label.asp?" in link['href'] and link['href'] not in visited:
						#opens the link for different foods
						#urls.append(link['href'])
						#visited.append(link['href'])
				#information = parser.nutrition_parse(link['href'])
				foodlist.append(parser.create_food(link['href']))
				#dictFood[foodlist[i].get_name()] = [foodlist[i].get_fat(), foodlist[i].get_carbs(), foodlist[i].get_protein(), foodlist[i].get_calorie()]
				foodlist[i].id = i + 1
				i+= 1 
				#calorie_text.append(information[0])
				#nutrition[information[0]] = (information[1],information[2])

						#parser.nutrition_parse currently parses the calories


	return foodlist



