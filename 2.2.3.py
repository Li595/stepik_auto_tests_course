from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_css_selector('#num1').text
    num2 = browser.find_element_by_css_selector('#num2').text
    x = str(str(int(num1) + int(num2)))
    
    select = Select(browser.find_element_by_css_selector('#dropdown'))
    select.select_by_value(x)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    
finally:
    time.sleep(5)
    browser.quit()