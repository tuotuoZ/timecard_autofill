from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

Weekday = input("Please enter a working day")
hour_start = input("Please enter the start time you will work")
hour_end = input("Please enter the end time of your work")

driver = webdriver.Chrome()

##Get to the main page
user = "xxxx"
pwd = "xxxx"

driver.get("http://thehub.hampshire.edu")
assert "TheHub Main Menu" in driver.title
elem = driver.find_element_by_id("acctLogin")
elem.click()

##Fill the username and password to login
elem = driver.find_element_by_id("USER_NAME")
elem.send_keys(user)
elem = driver.find_element_by_id("CURR_PWD")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

# Navigate to the timecard page
student_link = driver.find_element_by_link_text('Students')
student_link.click()
timecard_link = driver.find_element_by_link_text('Enter a Timecard')
timecard_link.click()

# Select a job
first_job = driver.find_element_by_name('LIST.VAR1_RADIO')
first_job.click()
submit_button = driver.find_element_by_name('SUBMIT2')
submit_button.click()

# Select the first timeslot
# Need to have a better way to deal with the dates, now it's hard coding
# Tuesday LIST_VAR_4_5, 4_19, Thursday 4_9, 4_23
# select = Select(driver.find_element_by_xpath("//select[@name='LIST.VAR4_5']"))
# select.select_by_visible_text('10:00AM')
el3 = driver.find_elements_by_xpath("//select")


print(len(el3))
date_list = {"Sunday": [0, 28], "Monday": [4, 32], "Tuesday": [8, 36], "Wednesday": [12, 40]}
indice = date_list[Weekday]

for index in indice:
	Select(el3[index]).select_by_visible_text(hour_start)
	Select(el3[index+1]).select_by_visible_text(hour_end)
