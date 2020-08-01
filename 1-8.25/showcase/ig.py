from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C://Users//Richard//Documents//VSCODE//executables//chromedriver.exe")
driver.get("https://www.instagram.com/")
time.sleep(1)
driver.find_element_by_name("username").send_keys("maodou.canspeak")
driver.find_element_by_name("password").send_keys("maodou999" + Keys.ENTER)
time.sleep(2)
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[5]/a/div/div[2]/div[1]").click()

for i in range(200):
    driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("今天是我主人第" + str(i+1) + "次想你" + Keys.ENTER)
