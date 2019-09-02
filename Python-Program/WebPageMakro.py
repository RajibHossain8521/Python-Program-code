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
import time
import webbrowser as wb

# Program start time
print(time.strftime('%I:%M:%S %p %d %B, %Y'))

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
#'branNameRegexp' pattern find the brand name of product : Done
brandNameRegexp = re.compile(r'<span itemprop="brand" >(.*?)</span>')
#'brandModelRegexp' pattern find the brand model of product : Done
brandModelRegexp = re.compile(r'<span itemprop="model">(.*?)</span>')
#'brandPriceRegexp' pattern find the brand price of product : Done
brandPriceRegexp = re.compile(r'<p class="price\s*">\m*\s*R\s*(.*?)<span class="mak-product__cents">')
#'brandSaveRegexp' pattern find the brand savings of product : Done
brandSaveRegexp = re.compile(r'<div class="priceData-savings">\m*\s*Save&nbsp;\s*R\s*(.*?)<span class="mak-product__cents">')
#'brandSizeRegexp' pattern find the brand size of product : Done
brandSizeRegexp = re.compile(r'<div class="col-xs-4 no-space">Size</div>\m*\s*?<div class="col-xs-8 no-space">(.*?)</div>')
#'brandTechRegexp' pattern find the brand technology of productsiz : Done
brandTechRegexp = re.compile(r'<td class="attrib col-xs-4">Screen Type</td>\m*\s*?<td class="col-xs-8">\m*\s*(.*?)</td>')
#'brandDescripRegexp' pattern find the description of product
brandDescripRegexp = re.compile(r'<a href="">Details</a>\s*?\m*\s*(.*?)<div class="mak-content__block mixin-h3">Features</div>')
#'descripSetSpace' pattern set the space of brand description
descripSetSpace = re.compile(r'<[/]td>')
#'removeDescripExtraTag' pattern remove the extra tag from descriptio
removeDescripExtraTag = re.compile(r'<(.*?)>')


# First Loop : Traverse all urls of products | Makro.co.za Site
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
    
    # Check total page for all links of promotion product : For all next page
    total_nextPage = re.findall(next_pageCount, page_content)
    total_nextPage = list(map(int, total_nextPage))
    highest_page = max(total_nextPage)
    print(highest_page)

    # Second Loop : This loop traverse all the next page and store promo link 
    for nextpage in range(highest_page-1):

        pageNumber = nextpage+1
        pageNumber = str(pageNumber)

        # parse the next page link to the server for the page source
        response = requests.get(url_list[productLink]+'&page='+pageNumber)

        if response.ok is False:
            sys.exit('Could not get response from server.')

        next_pageContent = response.text
        all_nextPageLinks = re.findall(regexp, next_pageContent)
        
        # Store all pages links into promo_link_storeList list
        promo_link_storeList = promo_link_storeList + all_nextPageLinks

    print(len(all_nextPageLinks))
    print(len(promo_link_storeList))
    #print(promo_link_storeList)
    # End Second Loop : This loop was for traversing all next page for promo links

    
    # Third Loop : This loop traverse all promotion link of product and finds the data
    for promolinks in range(len(promo_link_storeList)):
        
        promoProductUrl = 'https://www.makro.co.za'+promo_link_storeList[promolinks]
        print(promoProductUrl)
        response_promoPage = requests.get(promoProductUrl)
        
        print(response_promoPage.status_code)
        print(response_promoPage.ok)
        if response.ok is False:
            sys.exit('Could not get response from server.')
            
        promo_page_source = response_promoPage.text
        '''
        with open("Makro.text", "w") as f:
	        f.write(promo_page_source)

        # find the file path and store into file_path
        file_path  = os.path.realpath("Makro.text")
        print(file_path)

        # open file text or content in the browsers
        wb.open("file://" + file_path)
        break
        '''

        # find all required data of product using regular expression
        brandName = re.findall(brandNameRegexp, promo_page_source)
        brandModel = re.findall(brandModelRegexp, promo_page_source)
        brandSize = re.findall(brandSizeRegexp, promo_page_source)
        brandTechnology = re.findall(brandTechRegexp, promo_page_source)
        brandPrice = re.findall(brandPriceRegexp, promo_page_source)
        brandSaving = re.findall(brandSaveRegexp, promo_page_source)
        brandDescription = re.findall(brandDescripRegexp, promo_page_source)

        brandNameList = []
        brandNameList = brandNameList + brandName

        # Replace the unnecessary tag from description
        #brandDescription = re.sub(r'<(.*?)>', ' ', brandDescription)
        #brandDescription = re.sub()         
        print("brand:",brandName)
        print("Model:",brandModel)
        print("Size:",brandSize)
        print("Technology:",brandTechnology)  
        print("Price:",brandPrice) 
        print("Save:",brandSaving)
        print("Description:",brandDescription)
        
    # End : Third Loop | This loop was for traversing all promo links for products data
    
# Program End Time
print(time.strftime('%I:%M:%S %p %d %B, %Y'))



















