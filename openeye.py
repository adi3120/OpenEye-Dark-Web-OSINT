from utils import usecases
import sys

import requests
session = requests.session()
session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                   'https': 'socks5h://127.0.0.1:9050'}
xquery="hidden wiki"

text="""
===================================================
 .╭-━-━-━-╮                .╭-━-━-━-╮ 
╱╱┃ ╭-━-╮ ┃               ╱╱┃ ╭-━-━-╯ 
╱╱┃ ┃ ╱ ┃ ┣-━-━-┳-━-━-┳-━━-╮┃ ╰-━-━-┳-╮  .╭-┳-━-━-╮
╱╱┃ ┃ ╱ ┃ ┃ ╭-╮ ┃ ┃ ━-┫ ╭-╮ ┫ ╭-━-━-┫ ┃  ╱┃ ┃ ┃ ━-┫
╱╱┃ ╰-━-╯ ┃ ╰-╯ ┃ ┃ ━-┫ ┃ ┃ ┃ ╰-━-━-┫ ╰-━-╯ ┃ ┃ ━-┫
╱╱╰-━-━-━-┫ ╭-━-┻-━-━-┻-╯ ╰-┻-━-━-━-┻-━-╮ ╭-┻-━-━-╯
╱//╱╱╱╱╱//┃ ┃╱//╱╱╱╱╱╱╱╱//╱╱╱//╱╱╱╱╱╱/╭━╯ ┃╱╱╱╱╱╱/
          ╰-╯                         ╰━━-╯
===================================================	      
"""

print(text)

if len(sys.argv)>1:
	if sys.argv[1]=='-k':
		if sys.argv[2]=='-r':
			if sys.argv[3]:
				with open(sys.argv[3],"r") as f:
					for i in f:
						usecases.keyword_search_analysis(i)
		else:
			if sys.argv[2]:
				usecases.keyword_search_analysis()
		
	elif sys.argv[1]=='-u':
		usecases.onion_url_search_analysis()
	elif sys.argv[1]=='-s':
		if sys.argv[2]=='-r':
			if sys.argv[3]:
				with open(sys.argv[3],"r") as f:
					for i in f:
						usecases.run_onionscan(i.split('.onion')[0]+'.onion')
		else:
			if sys.argv[2]:
				usecases.run_onionscan(sys.argv[2])
	elif sys.argv[1]=='-n':
		if sys.argv[2]=='-r':
			if sys.argv[3]:
				with open(sys.argv[3],"r") as f:
					for i in f:
						usecases.run_onionscan(i.split('.onion')[0]+'.onion')
		else:
			if sys.argv[2]:
				usecases.run_onionscan(sys.argv[2])
	elif sys.argv[1]=='-d':
		from utils import st
		st.show_data()
		
	elif sys.argv[1]=='-h':
		print("flags : ")
		print("-k           : To fetch data from sites by entering keywords")
		print("-k -r <file> : To fetch data from keywords from file")
		print("-u           : To fetch data from the url entered")
		print("-u -r <file> : To fetch data from urls from file")
		print("-s -r <file> : Run OnionScan on a file containing urls")
		print("-s <url>     : Run OnionScan on a url")
		print("-d 			: Show data")
		print("-h 			: Show help")
else:
	print("flags : ")
	print("-k           : To fetch data from sites by entering keywords")
	print("-k -r <file> : To fetch data from keywords from file")
	print("-u           : To fetch data from the url entered")
	print("-u -r <file> : To fetch data from urls from file")
	print("-s -r <file> : Run OnionScan on a file containing urls")
	print("-s <url>     : Run OnionScan on a url")
	print("-d 			: Show data")
	print("-h 			: Show help")

