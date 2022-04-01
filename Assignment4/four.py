from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time

# Open Firefox 
browser = webdriver.Firefox()

# Web page url
browser.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
  
# Find id of option
x = browser.find_element_by_id('RESULT_RadioButton-9')
drop = Select(x)
  
# Select by index
drop.select_by_index(2)
time.sleep(4)
browser.close()



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time

# Open Firefox 
driver = webdriver.Firefox()

driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
#identify element with an attribute using xpath
l = driver.find_element_by_xpath("//img[@alt='tutorialspoint']")
#get src attribute
s = l.get_attribute('src')
print('Src attribute value is: ')
print(s)
#browser quit
driver.quit()





from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time

# Open Firefox 
driver = webdriver.Firefox()

driver.implicitly_wait(0.8)
driver.get("https://www.tutorialspoint.com/index.htm")
# to identify element
l = driver.find_element_by_xpath("//*[text()='Library']")
#click with execute_script
driver.execute_script("arguments[0].click();",l)
print("Page title after click: " + driver.title)