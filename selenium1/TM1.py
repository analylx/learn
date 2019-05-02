#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from time import sleep

# Create a new instance of the chrome driver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')

# go to the google home page
driver.get("http://wakeupnow.tk")
driver.find_element_by_id('username').send_keys("admin")
driver.find_element_by_id('password').send_keys("310018")
driver.find_element_by_id('submit').click()
#driver.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr/td[2]/a").click()
#sleep(60)
#driver.find_element_by_xpath("//frame[@id='p_left']/html/body/form/select/option[1]").click()

#for link in driver.find_elements_by_xpath("//*[@href]"):#获取当前页面的href
#    print(link.get_attribute('href'))

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_id("kw")

# type in the search
inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    #print driver.title

finally:
    driver.quit()

