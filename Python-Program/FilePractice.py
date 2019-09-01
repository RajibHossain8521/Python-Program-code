import requests
import sys
import os
import webbrowser as wb
import io
import re

with open('file.text', "r") as f:
    text = f.read()
    
find = re.findall(r'^.*?$',text, re.IGNORECASE|re.MULTILINE)
print(find)

'''
url = sys.argv[1]
file_name = sys.argv[2]
r = requests.get(url)
with open(file_name, "w") as f:
	f.write(r.text)
'''
'''
file_name = "file.text"
mode = "r"

try:
	with open(file_name, mode) as fp:
		content = fp.read()
		print(content)
except FileNotFoundError:
	print(file_name, "not found, please check if the files name is correct.")
except io.UnsupportedOperation:
	print("Are you sure", file_name, "is readble.")
except Exception as e:
	print(e)
'''

'''
# this block was the part of WebPageMakro.py file
# open file and store the webpage content
with open("Makro.text", "w") as f:
	f.write(page_content)

# find the file path and store into file_path
file_path  = os.path.realpath("Makro.text")
print(file_path)

# open file text or content in the browsers
wb.open("file://" + file_path)

"""
for i in range(len(next_page_linkStore)):
    page_count = re.findall(next_pageCount, i[next_page_linkStore])
    previous_page = page_count
    if page_count == previous_page-1:
        break
"""
"""
# connet with server for next page url
if len(next_page_linkStore) != 0: 
    response = requests.get(next_page_linkStore[0])

if response.ok is False:
    sys.exit("Could not get response from server.")

page_content = response.text

next_pageLinks = re.findall(regexp, page_content)
promo_link_store = promo_link_store + next_pageLinks
"""

'''
	
