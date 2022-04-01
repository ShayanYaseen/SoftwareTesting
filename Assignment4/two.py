from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Open Firefox 
browser = webdriver.Firefox()

# Navigate to Facebook
browser.get("http://www.facebook.com")

username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
username.send_keys("you@email.com")
password.send_keys("yourpassword")

# Login Button
login_button = browser.find_element_by_name('login')
login_button.click() # Send mouse click
