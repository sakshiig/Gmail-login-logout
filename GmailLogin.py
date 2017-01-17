from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
browser.find_element_by_id("Email").send_keys("email id")
browser.find_element_by_id("next").click()
time.sleep(2)
browser.find_element_by_id("Passwd").send_keys("password")
browser.find_element_by_id("signIn").click()
time.sleep(3)
browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/a/span").click()
browser.find_element_by_id("gb_71").click()

