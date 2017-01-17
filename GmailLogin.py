import requests
import requests.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from requests.exceptions import ConnectionError
import getpass
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

browser.get(
    "https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")

send="/html/body/div[13]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]"
body="/html/body/div[13]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div"

def login(email,password):
 browser.find_element_by_id("Email").send_keys(email)
 browser.find_element_by_id("next").click()
 time.sleep(2)
 browser.find_element_by_id("Passwd").send_keys(password)
 browser.find_element_by_id("signIn").click() #this click logs in to gmail
 time.sleep(5)
 try:
    if browser.find_element_by_id("errormsg_0_Passwd").is_displayed():
         print "FAIL"
    elif browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/div/div").is_displayed():
         print "PASS"
 except Exception as e:
         print "FAIL"


def compose():
 browser.find_element_by_xpath("//*[@gh='cm']").click()
 browser.find_element_by_name("to").send_keys("acc.test91@gmail.com",Keys.ENTER)
 browser.find_element_by_name("subjectbox").send_keys("Test mail",Keys.ENTER)
 browser.find_element_by_xpath(body).send_keys("random text in the body of the mail")
 browser.find_element_by_xpath(send).click()
 time.sleep(5)

"""
#Create filter
browser.get("https://mail.google.com/mail/u/0/#settings/filters")
time.sleep(2)
browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div[5]/div/table/tbody/tr[6]/td/span[1]").click()
browser.find_element_by_xpath("/html/body/div[31]/div/div[2]/div[2]/span[2]/input").send_keys("acc.test91@gmail.com")
browser.find_element_by_xpath("/html/body/div[31]/div/div[2]/div[3]/span[2]/input").send_keys("testspm91@gmail.com")
browser.find_element_by_xpath("/html/body/div[31]/div/div[2]/div[9]/div[2]").click()
time.sleep(5)

# #logout
browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/a/span").click()
browser.find_element_by_id("gb_71").click()

"""
login("testspm91","abc123!@#")
compose()




