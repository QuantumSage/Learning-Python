# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:38:39 2022

@author: Quantum Sage
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("C:/Users/Quantum Sage/Desktop/chromedriver_win32/chromedriver")
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600) #delay is to wait for slow internet connection to load actual page
target='"Ankit"' #target receipients
st="Python script dump(1) By.XPATH value" #message to be sent
x_args='//span[contains(@title,'+target+')]'
target=wait.until(EC.presence_of_element_located((By.XPATH,x_args))) #???
target.click()
input_box=driver.find_element_by_class_name('p3_M1') #gotta use the whole ass class and not delve down into the input box (whole here means "Type message" element and textbox element)
input_box.send_keys(st,Keys.ENTER) #Keys.ENTER replicates the enter we press to send messages

