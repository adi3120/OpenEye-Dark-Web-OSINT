import os
import json

def show_data():
	os.system("streamlit run E:/crawler/handmade/utils/st.py")

def display():
	import streamlit as st
	st.title("Dark Web Crawled Dataset")

	with open('Oniondata.json', 'r') as file:
		json_data = json.load(file)
		st.write(json_data)

display()