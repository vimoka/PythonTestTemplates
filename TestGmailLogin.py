import time
from selenium import webdriver

#Entering the username and password
username = "vimoka@gmail.com"
password = "vi123"

#Setting up the driver path and instantiating chrome driver 
DriverPath = "C:\\Users\\Vimoka\\Desktop\\selenium_testing\\chromedriver.exe"
driver = webdriver.Chrome(DriverPath)

#Opening the Gmail website to check the login functionality
driver.get("http://www.gmail.com")

#Entering the email id
emailid = driver.find_element_by_id("IdentifierId")
emailid.send_keys(username)

#Hitting the next button
driver.find_element_by_xpath("//*[@id="identifierNext"]/content").click()
time.sleep(5)

#Entering the password
passwd = driver.find_element_by_xpath("//*[@id="password"]/div[1]/div/div[1]/input")
passwd.send_keys(password)
time.sleep(3)

#Submitting the login
driver.find_element_by_xpath("//*[@id="passwordNext"]/content/span").click()
time.sleep(10)

#Closing the driver
driver.close()