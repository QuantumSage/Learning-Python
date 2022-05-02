# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 23:04:40 2022

@author: Quantum Sage
"""

from selenium import webdriver
browser=webdriver.Chrome("C:/Users/Quantum Sage/Desktop/chromedriver_win32/chromedriver")
browser.get("https://www.google.com") #opens chrome window!!!
elem=browser.find_element_by_link_text('Images')
elem.click()
search=browser.find_element_by_name("q") #we get this by inspecting specific webpage elements 
search.send_keys("Updoot")
search=browser.find_element_by_class_name("Tg7LZd") 
search.click()