from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get('http://the-internet.herokuapp.com/login')

sleep(5)

username_input = driver.find_element(By.ID, 'username')
username_input.send_keys('tomsmith')

sleep(5)

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys('SuperSecretPassword!')

sleep(5)

login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
login_button.click()

sleep(5)

success_message = driver.find_element(By.CSS_SELECTOR, 'div.flash.success')
print(success_message.text.strip())

driver.quit()
