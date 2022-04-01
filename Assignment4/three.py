from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Open Firefox 
browser = webdriver.Firefox()

# Navigate to Facebook
browser.get("http://www.facebook.com")
print(driver.title)