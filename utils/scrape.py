from bs4 import BeautifulSoup
import requests
session = requests.session()
session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                   'https': 'socks5h://127.0.0.1:9050'}
xquery="hidden wiki"

def remove_duplicates_last_part(urls):
	print("Removing duplicates")

	unique_urls = []
	seen_parts = set()

	for url in urls:
		url_parts = url.split(".onion/")
		if len(url_parts) == 2:
			url_suffix = url_parts[1]
			if url_suffix not in seen_parts:
				seen_parts.add(url_suffix)
				unique_urls.append(url)
	return unique_urls

# def remove_duplicates_title(urls):
# 	print("Removing duplicates")
# 	unique_urls = []
# 	seen_parts = set()

# 	for url in urls:
# 		html=get_html("http://"+url)
# 		if html:
# 			title=get_title(html)
# 			if title:
# 				if title not in seen_parts:
# 					seen_parts.add(title)
# 					unique_urls.append(url)
# 	return unique_urls

def get_title(text):

	soup = BeautifulSoup(text, 'html.parser')
	if soup.title:	
		title=soup.title.string
		return title
	else: return None

def get_description(text):
	soup = BeautifulSoup(text, 'html.parser')
	
	description = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else None

	return description

def get_keywords(text):
	soup = BeautifulSoup(text, 'html.parser')
	keywords = soup.find('meta', attrs={'name': 'keywords'})['content'] if soup.find('meta', attrs={'name': 'keywords'}) else None
	return keywords

# @timeout(5,use_signals=False)
def get_html(url):
	try:
		page = session.get(url,timeout=5)
		return page.text
	except requests.exceptions.RequestException as e:
		# print("Failed to fetch HTML:", e)
		return None

def get_urls_from_keywords(keyword):
	urls=[]
	try:
		page=session.get("https://ahmia.fi/search/?q="+keyword)
		soup = BeautifulSoup(page.text, 'html.parser')
		n=5
		for url in soup.find_all('a'):
			# if n:
				if "http://" in url.get('href'):
					url = url.get('href').split("http://")[1]
					# url = url.split(".onion")[0] + ".onion"
					urls.append("http://"+url)
					# n-=1
		# urls=remove_duplicates_title(urls)
		print("Found "+str(len(urls))+" urls!")
		urls=remove_duplicates_last_part(urls)
		return urls
	except requests.exceptions.RequestException as e:
		print("Failed to fetch HTML:", e)
		return None