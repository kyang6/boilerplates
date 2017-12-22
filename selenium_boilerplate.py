import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import json

import csv


company_name = "zuora"
job_title = "Senior"
# ------------------------------------------



driver = webdriver.Chrome('/Users/KevinYang/Documents/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://app.hubspot.com/')

username = driver.find_element_by_id('username')
username.send_keys('kyang6@stanford.edu')

password = driver.find_element_by_id('password')
password.send_keys('')

login = driver.find_element_by_id('loginBtn')
login.click()



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nav-main-item-sales-contacts"))
    )
finally: 
	print("Logged in and loaded")

contacts_nav = driver.find_element_by_id('nav-main-item-sales-contacts')
contacts_nav.click()

def add_filter(str_property):
	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, "div.filter-controls"))
	    )
	finally: 
		print("Contacts page loaded")

	driver.execute_script("document.getElementsByClassName('filter-controls')[0].click()")

	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, "h5.group-title"))
	    )
	finally: 
		print("filter page loaded")

	search_property = driver.find_elements_by_class_name("form-control")[1]
	search_property.send_keys(str_property)

	counter = 0
	while True:
		try:
		    if(driver.find_element_by_css_selector("label.property-label").text == str_property):
		    	print(str_property + " filter loaded")
		    	break
		    if(counter >= 1000):
		    	raise Exception(str_property + ' was never loaded')
		    	break
		    counter += 1
		except:
			continue

	filter_prop_result = driver.find_element_by_css_selector("li.property-type")
	filter_prop_result.click()

def add_company():
	add_filter("Associated company")
	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.uiButton.btn-default.uiDropdown__button"))
	    )
	finally: 
		print("Search for a company Loaded")

	while True:
		try:
			open_search_bar = driver.find_elements_by_css_selector("button.btn.uiButton.btn-default.uiDropdown__button")[1]
			open_search_bar.click()
			break
		except:
			continue

	search_for_company = driver.find_elements_by_css_selector("input.select2-input")[0]
	search_for_company.send_keys(company_name)


	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, "span.select2-match"))
	    )
	finally: 
		print("Company found")

	try:
		company_result = driver.find_element_by_css_selector("span.select2-match")
		print("Clicking on the company " + company_result.text)
		company_result.click()
	except:
		print("Company not found or click failed")

	add_new_filter = driver.find_elements_by_css_selector("button.btn.uiButton.btn-primary")[2]
	add_new_filter.click()

def add_job_title():
	add_filter("Job Title")
	try:
	    element = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control"))
	    )
	finally: 
		print("Search bar for job title loaded")
	job_search_bar = driver.find_elements_by_css_selector("input.form-control")[2]
	job_search_bar.send_keys(job_title)

	print("Job searching for " + job_title)

	prev_contact = driver.find_elements_by_css_selector("td.name-cell")[-1]
	while True:
		if(prev_contact != driver.find_elements_by_css_selector("td.name-cell")[-1]):
			break

	add_new_filter = driver.find_elements_by_css_selector("button.btn.uiButton.btn-primary")[2]
	add_new_filter.click()


add_company()
add_job_title()




#file = open('testdata.csv')
#data = csv.reader(file)

# directory = 'manufacturing equipment'
# companies = ['Flowserve', 'Parker-Hannifin Corp', 'Pentair Plc', 'Ingersoll-Rand PLC', 'Illinois Tool Works', 'Lincoln Electric Holdings', 'Stanley Black & Decker Inc.', 'Xylem', 'IDEX Corp.', 'Snap-On Inc.', 'Pall Corp.', 'Schneider Electric', 'Honeywell', 'Johnson Controls']
# print("Worksp")
# # for name in companies:
# # 	company_dict = {}

# 	try:
# 	    element = WebDriverWait(driver, 10).until(
# 	        EC.presence_of_element_located((By.ID, "x-auto-66-input"))
# 	    )
# 	finally: 
# 		print("search bar for " + name + " loaded")

# 	search = driver.find_element_by_id('x-auto-66-input')
# 	search.clear()
# 	search.send_keys(name)
# 	time.sleep(10)
# 	#search.send_keys(Keys.RETURN)
# 	search_button = driver.find_element_by_class_name('x-btn-text')
# 	search_button.click()

# 	try:
# 	    element = WebDriverWait(driver, 20).until(
# 	        EC.presence_of_element_located((By.CSS_SELECTOR, "#departments input"))
# 	    )
# 	except:
# 		print("oh well")
# 	finally: 
# 		print("checkboxes loaded")

# 	department_list = driver.find_elements(By.CSS_SELECTOR, "#departments input")
# 	print("Length of departments " + str(len(department_list)))
# 	for department in department_list:
# 		department.click()
# 		try:
# 		    element = WebDriverWait(driver, 10).until(
# 		        EC.presence_of_element_located((By.CSS_SELECTOR, "div.x-grid3-row"))
# 		    )
# 		except:
# 			print("oh well")
# 		finally: 
# 			print("next department")

# 		for i in range(10):
# 			html = driver.page_source
# 			company_dict = grab_contacts(html, company_dict)

# 			try:
# 				next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-describedby='x-auto-3'][aria-disabled='false']")
# 			except:
# 				break
# 			next_button.click()
# 			try:
# 			    element = WebDriverWait(driver, 10).until(
# 			        EC.presence_of_element_located((By.CSS_SELECTOR, "div.x-grid3-row"))
# 			    )
# 			finally: 
# 				print("next page")
			
# 		department.click()
	
# 	json_str = json.dumps(company_dict)

# 	if not os.path.exists(directory):
# 		os.makedirs(directory)

# 	f = open(directory + '/' + str(name) + '.txt', 'w')
# 	f.write(json_str)

