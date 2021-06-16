from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='/home/uranium/Documents/DS_project/chromedriver')

browser.get('http:/www.google.com')
browser.find_element_by_name("gLFyf gsfi").send_keys("hello")
