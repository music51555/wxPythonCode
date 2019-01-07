import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS('/Users/mac/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get('https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=')

time.sleep(3)

driver.save_screenshot('1.png')

driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

time.sleep(3)

driver.save_screenshot('2.png')

page_text = driver.page_source

soup = BeautifulSoup(page_text,'lxml')

movie_list = soup.select('.movie-content')

for movie in movie_list:
    movie_name = movie.select('.movie-name-text a')[0].text
    movie_score = movie.select('.rating_num')[0].text
    print(movie_name+'\n'+movie_score)