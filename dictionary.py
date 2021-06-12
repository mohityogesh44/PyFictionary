import requests
from bs4 import BeautifulSoup

def get_meaning(word):
	url = 'https://dictionary.cambridge.org/dictionary/english/'
	
	header = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
	
	response = requests.get(url+word, headers = header)
	# response.status_code
	
	soup = BeautifulSoup(response.text, 'html.parser')
	
	#Finding the class.
	div = soup.find(class_= 'entry-body')

	#Part of speech
	pos = div.find(class_='pos dpos').text
	#meaning
	meaning = div.find(class_='def ddef_d db').text

	return pos, meaning

if __name__ == '__main__':
	word = input("Enter a word: ")
	pos, meaning = get_meaning(word)

	print(f"{word} ({pos}) \n {meaning}")