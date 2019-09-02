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
# Web Crawling for Makro.co.za site

# re is a regular expression package module
# requests module connent address to the web server
# os package for find real path of any files
# webbrowser module used for open any file in the browsers
# sys module for passing url, vlaue, fileName etc throug command line

import re
import requests
import os
import sys
import webbrowser as wb


# url_list for store the all site links of products
url_list = ['https://www.makro.co.za/electronics-computers/televisions/led/c/BAA?text=&q=%3Arelevance%3AsashOverlayTitle%3AOn%2BPromotion']


"""
're.compile()' method give us access to use this pattern more than one in the program
            without compiling the same pattern at a time more than once
"""
#'regexp' pattern find the all promotion product links of page : Done
regexp = re.compile(r'<a class="product-tile-inner__img" href="(.*?)"')
#'next_page_number' pattern check the next page links of page : Done
next_page_number = re.compile(r'<li class="pagination-next">\s*<a href="(.*?)"')
#'next_pageCount' pattern find the exact or total number of page : Done
next_pageCount = re.compile(r'page=\d+["]>(.*?)</a>')
#'branNameRegexp' pattern find the brand name of product
brandNameRegexp = re.compile(r'<span itemprop="brand" >(.*?)</span>')
#'brandModelRegexp' pattern find the brand model of product
brandModelRegexp = re.compile(r'<span itemprop="model">(.*?)</span>')
#'brandPriceRegexp' pattern find the brand price of product
brandPriceRegexp = re.compile(r'<p class="price ">(.*?)<span class="mak-product__cents">')
#'brandSaveRegexp' pattern find the brand savings of product
brandSaveRegexp = re.compile(r'<div class="priceData-savings">\m*\s*Save&nbsp;\s*R\s*(.*?)<span class="mak-product__cents">')
#'brandSizeRegexp' pattern find the brand size of product
brandSizeRegexp = re.compile(r'<div class="col-xs-4 no-space">Size</div>\m*<div class="col-xs-8 no-space">(.*?)</div>')
#'brandTechRegexp' pattern find the brand technology of productsiz
brandTechRegexp = re.compile(r'<td class="attrib col-xs-4">Screen Type</td>\m*<td class="col-xs-8">(.*?)</td>')
#'brandDescripRegexp' pattern find the description of product
brandDescripRegexp = re.compile(r'<a href="">Details</a>(.*?)<div class="mak-content__block mixin-h3">Features</div>')


for productLink in range(len(url_list)):
    # connect to the server for url webpage
    response = requests.get(url_list[productLink])

    # if address of webpage failed to connecte with server
    if response.ok is False:
        sys.exit("Could not get response from server.")

    # Store the WebPage content into page_content
    page_content = response.text

    # Grap all promotion link into link_Store : For Main Page
    promo_link_storeList = re.findall(regexp, page_content)
    #print(promo_link_store)
    #print(len(promo_link_storeList))

    #--------------------------------------------------------------------------
    # Check total page for all links of promotion product : For all next page
    total_nextPage = re.findall(next_pageCount, page_content)
    total_nextPage = list(map(int, total_nextPage))

    highest_page = max(total_nextPage)
    print(highest_page)

    # this loop traverse all the next page
    for nextpage in range(highest_page-1):

        pageNumber = nextpage+1
        pageNumber = str(pageNumber)

        response = requests.get(url_list[productLink]+'&page='+pageNumber)

        if response.ok is False:
            sys.exit('Could not get response from server.')

        next_pageContent = response.text
        all_nextPageLinks = re.findall(regexp, next_pageContent)

        promo_link_storeList = promo_link_storeList + all_nextPageLinks

    print(len(all_nextPageLinks))
    print(len(promo_link_storeList))
    #--------------------------------------------------------------------------

    # This loop traverse all promotion link of product and finds the data
    for promolinks in range(len(promo_link_storeList)):

        response_promoPage = requests.get('https://www.makro.co.za' + promo_link_storeList[promolinks])

        if response.ok is False:
            sys.exit('Could not get response from server.')

        promo_page_source = response.text

'''

	
