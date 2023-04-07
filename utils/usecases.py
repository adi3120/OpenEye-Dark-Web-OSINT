import joblib
import json
from .scrape import *
from .mlfunctions import *
from timeout_decorator import timeout
import re
import sys
import os

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def clear_line():
    sys.stdout.write('\033[F')  # Move cursor to previous line
    sys.stdout.write('\033[K')  # Clear line
    

def fetch_data_url(url):
	html=get_html(url)

	titles=""
	descriptions=""
	keywords=""

	datalist=[]

	data={
		"OnionLink":"",
		"Active":True,
		"VendorIDs":[],
		"Vulnerabilities":"",
		"Open Ports":"",
		"IllegalWords":[],
	}

	if html:

		data["VendorIDs"]=get_emails(html)

		data["OnionLink"]=url
		
		# print("Getting Title...")
		title=get_title(html)

		# print("Getting Description...")
		description=get_description(html)

		# print("Getting Keywords...")
		keyword=get_keywords(html)

		if title:
			titles+=title+"\n" 
		if description:
			descriptions+=description+"\n"
		if keyword:
			keywords=keyword+"\n"
		

		data["Title"]=title
		data["Description"]=description
		data["Keywords"]=keyword

		data["IllegalWords"]=illegal_words(html)
		


	else:
		return None
	
	return data


def keyword_search_analysis(keyword=None):
	if keyword==None:
		os.remove("Oniondata.json")
		keyword=input("Enter keyword: ")
	text=""
	print("Getting urls...")

	urls=get_urls_from_keywords(keyword)

	datalist=[]
	n=50
	with open("Oniondata.json", "a", encoding='utf-8') as f:
		f.write('[')
		urls=urls[:n]
		for i, url in enumerate(urls):
			complete=100*(i)/(len(urls))

			data = fetch_data_url(url)
			json.dump(data, f,cls=SetEncoder)  # Write individual data to the file
			if i!=len(urls)-1:
				f.write(',')  # Add a newline character after each data entry
			# print(f"Data {i+1} written to the file")
			# print("=============================================")
			print("Completed "+str(complete)+" %")
			clear_line()

		f.write(']')
		

	print("Done...")

def onion_url_search_analysis():
	url=input("Enter Onion Link : ")
	print("Getting HTML...")
	html=get_html(url)

	data=fetch_data_url(url)

	with open("Oniondata.json","w",encoding='utf-8') as f:
		print("writing to the file....")
		json.dump(data, f,cls=SetEncoder)

	print("Done...")

def get_emails(html):
	soup = BeautifulSoup(html, 'html.parser')

	email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
	email_addresses = []
	if email_regex.search(soup.text):
		email_addresses.extend(email_regex.findall(soup.text))

	return email_addresses
    
def run_onionscan(onion):

    print(f"[*] Onionscanning {onion}")
    os.system("onionscan "+onion)

def illegal_words(html):
	soup = BeautifulSoup(html, 'html.parser')
	text = soup.get_text().lower()
	words_found = set()

	with open("files/drugs.txt","r") as f:
		for word in f:
			if word in text:
				words_found.add(word)

	with open("files/weapons.txt","r") as f:
		for word in f:
			if word in text:
				words_found.add(word)

	return words_found


