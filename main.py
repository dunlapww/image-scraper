
from selenium import webdriver 
from scraper import search_and_download

#credit to Fabian Bosler who created this webscraper:
#https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d

#first you need to download the chrome driver that matches your version of chrome
#e.g. I have chrome 91.0.4472.77, so I have version 91.
#go to 'https://chromedriver.chromium.org/downloads' and download the chrome driver that matches your version
# below is where I saved my chrome driver (replace DRIVER_PATH with your path) 

DRIVER_PATH = '/Users/will.dunlap/Documents/image_recog/chrome_driver/chromedriver'

search_term = 'fluffy dog'
target_path='./images'
number_images = 3

search_and_download(search_term=search_term, driver_path=DRIVER_PATH, target_path=target_path, number_images=number_images)

#wd.quit()