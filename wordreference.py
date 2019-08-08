from sys import argv
from bs4 import BeautifulSoup
from requests import get

try:
	if len(argv) < 4:
		print("\nusage: python wordrefernce.py <from_lang> <to_lang> <words>\n")
	else:
		lang1 = argv[1]
		lang2 = argv[2]
		words = ' '.join(argv[3:])

		source = get(f'https://www.wordreference.com/{lang1}{lang2}/{words}').text
		soup = BeautifulSoup(source, 'lxml')

		table = soup.find('div', class_='content').table
		row = table.find('tr', class_='even')
		word = row.find('td', class_='ToWrd')
		em = word.em.text

		word = word.text.replace(em, '')

		print(word)
except AttributeError:
	print("Word not found!")
except Exception:
	print("Please connect to the internet!")