from bs4 import BeautifulSoup as bs
from selenium import webdriver

#Creates a local instance of Chrome
driver = webdriver.Chrome('/usr/bin/chromedriver')

#Enter Url whose data to be parsed
url=input("Enter URL-") 
driver.get(url)
htmlcontent=driver.page_source #page_source stores the entire HTML content

#Passing the obtained html content to beautifulsoup
soup=bs(htmlcontent)
