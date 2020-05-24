# -*- coding: utf-8 -*-
"""
Created on Sat May  2 02:15:39 2020

@author: 91779
"""

"""import requests
from bs4 import BeautifulSoup
import re

url = "https://www.amazon.in/b/ref=s9_acss_bw_cg_LP_4c1_w?node=20367083031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-20&pf_rd_r=JV922G6WMNYCS3475F54&pf_rd_t=101&pf_rd_p=b1f9b196-9779-4d16-8855-c33e35065600&pf_rd_i=1389401031"

page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content,"html.parser")
#print(soup.prettify())

main_block= soup.find(id = "search-results")
sub_block = main_block.find_all(class_="s-item-container")
mobi_name = main_block.find(class_="a-size-base s-inline s-access-title a-text-normal")
print(mobi_name.get_text())

#This is to get the simple one block like for 1 phone to get all the phones now
mob_name = soup.find(class_="a-size-base s-inline s-access-title a-text-normal")
no_of_ratings = soup.find(class_="a-size-small a-link-normal a-text-normal")
mob_rating = soup.find("span",class_="a-icon-alt")

print(mob_name.text)
print(no_of_ratings.text)
print(mob_rating.text)

mob_name = [item.find("h2",class_='a-size-base s-inline s-access-title a-text-normal') for item in sub_block]
for i in mob_name:
    print(i.text)"""
    
def countList(lst1, lst2): 
    return [sub[item] for item in range(len(lst2)) 
                      for sub in [lst1, lst2]] 
      
# Driver code 
lst1 = [1, 2, 3] 
lst2 = ['a', 'b', 'c'] 
print(countList(lst1, lst2)) 

        