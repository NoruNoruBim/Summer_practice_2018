#список команд принимавших участие во всех этапах 5ти последних мировых чемпионатах по футболу
#с каким счетом и кто с кем играл

import requests
from bs4 import BeautifulSoup

url_array = [ "https://en.wikipedia.org/wiki/2014_FIFA_World_Cup", "https://en.wikipedia.org/wiki/2010_FIFA_World_Cup", "https://en.wikipedia.org/wiki/2006_FIFA_World_Cup", "https://en.wikipedia.org/wiki/2002_FIFA_World_Cup", "https://en.wikipedia.org/wiki/1998_FIFA_World_Cup", "https://en.wikipedia.org/wiki/1994_FIFA_World_Cup", "https://en.wikipedia.org/wiki/1990_FIFA_World_Cup" ]

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['(', ')', ',', '.']
#url_array = [ "https://en.wikipedia.org/wiki/2014_FIFA_World_Cup" ]
list_of_teams = []
score = []
tmp = []
marker = 0

for i in range(len(url_array)):

	list_of_teams = []

	request = requests.get(url_array[i])

	soup = BeautifulSoup((request.text), "lxml")
	
	main_information = soup.find('div', {'id' : 'bodyContent'})

	with open("library.txt", "a", encoding = "utf8") as library:
		library.write("          " + url_array[i] + "          \n")
		library.write(main_information.text)

	tmp = main_information.text.split()
	
	for spec in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
		for i in range(len(tmp)):
			if marker == 0 and tmp[i].lower() == "group" and tmp[i + 1].lower()[0] == spec:# try to find "GROUP A"
				for j in range(i, i + 100):
					#print(str(tmp[j]))
					if tmp[j].lower() == "pos":
						#print(tmp[i - 10 : i + 30])
						#marker = 1
						for i in range(j + 10, len(tmp)):
							if marker != 4 and tmp[i] == str(marker + 1) and tmp[i + 1] not in digits and len(tmp[i + 1]) >= 3 and '(' not in tmp[i + 1]:
								if tmp[i + 2] not in digits and len(tmp[i + 1]) >= 3 and '(' not in tmp[i + 2]:
									list_of_teams += [tmp[i + 1] + ' ' + tmp[i + 2]]
								else:
									list_of_teams += [tmp[i + 1]]
								#print(str(list_of_teams) + '\n')
								marker += 1
							if marker == 4:
								break
			if marker == 4:
				marker = 0
				for j in range(i, i + 400):
					if len(tmp[j]) == 3 and tmp[j][0] in digits and marker != 6:
						if tmp[j - 1] in list_of_teams:
							score += [tmp[j - 1]] + [tmp[j]] + [tmp[j + 1]]
						elif tmp[j - 2] + ' ' + tmp[j - 1] in list_of_teams:
							score += [tmp[j - 2]] + [tmp[j]] + [tmp[j + 1]]
						elif tmp[j - 3] + ' ' + tmp[j - 2] + ' ' + tmp[j - 1] in list_of_teams:
							score += [tmp[j - 3]] + [tmp[j]] + [tmp[j + 1]]
						#print(list_of_teams)
						#print(score)
						marker += 1
					if marker == 6:
						marker = 0
						break
				break
	
	
	#print(str(score))
	#print(main_information.text.split()[0 : 10])
	#print(str(list_of_teams))
	with open("list_of_teams.txt", "w", encoding = "utf8") as file:
		for team in list_of_teams:
			file.write(team.strip() + '\n')
			
			
	#print(score)
	q = 1
	with open("score.txt", "w", encoding = "utf8") as file:
		for element in score:
			if q <= 3:
				file.write(element + " ")
			else:
				file.write("\n" + element + " ")
				q = 1
			q += 1

		
		
		
		
		
		
		