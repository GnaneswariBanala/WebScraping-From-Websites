import requests
import pandas 
from bs4 import BeautifulSoup
import csv
response=requests.get("https://www.bikewale.com/royalenfield-bikes/")
# print(response)
Soup=BeautifulSoup(response.content,'html.parser')
# print(Soup.prettify)
#images
image=Soup.find_all('div',class_="imageWrapper relative")
img1=[]
for i in image:
     j=i.img['src']
     img1.append(j)
# print(img1)    
links=[]
link=Soup.find_all('div',class_='bikeDescWrapper')
for i in link:
     j=i.a['href']
     links.append(j)
# print(links)    
#text
links=[]
link=Soup.find_all('div',class_='bikeDescWrapper')
for i in link:
     j=i.a.text
     links.append(j)
# print(links)  
# names
names=Soup.find_all('h3',class_='bikeTitle margin-bottom10')
name=[]
for i in names:
     j=i.get_text()
     name.append(j)
# print(name)
#prices
prices=Soup.find_all('span',class_="font18")
price=[]
for i in prices:
     j=i.get_text()
     price.append(j)
# print(price)


#using csv we will store the data
with open ('il.csv','w')as csv_file:
     write=csv.writer(csv_file)
     write.writerow(image)
     for i in image:
          j=i.img['src']
          img1.append(j)
     write.writerow(image)     
