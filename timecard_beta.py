from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

##Get to the main page
user = "bz15"
pwd = "cexf28322832"

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
select = Select(driver.find_element_by_xpath("//select[@name='LIST.VAR4_5']"))
select.select_by_visible_text('10:00AM')

select = Select(driver.find_element_by_xpath('//select[@name="LIST.VAR5_5"]'))
select.select_by_visible_text('02:00PM')

select = Select(driver.find_element_by_xpath("//select[@name='LIST.VAR4_9']"))
select.select_by_visible_text('10:00AM')

select = Select(driver.find_element_by_xpath('//select[@name="LIST.VAR5_9"]'))
select.select_by_visible_text('02:00PM')

select = Select(driver.find_element_by_xpath("//select[@name='LIST.VAR4_19']"))
select.select_by_visible_text('10:00AM')

select = Select(driver.find_element_by_xpath('//select[@name="LIST.VAR5_19"]'))
select.select_by_visible_text('02:00PM')

select = Select(driver.find_element_by_xpath("//select[@name='LIST.VAR4_23']"))
select.select_by_visible_text('10:00AM')

select = Select(driver.find_element_by_xpath('//select[@name="LIST.VAR5_23"]'))
select.select_by_visible_text('02:00PM')

submit_button = driver.find_element_by_name('SUBMIT2')
submit_button.click()

select = Select(driver.find_element_by_name('VAR5'))
select.select_by_value('L')



submit_button = driver.find_element_by_name('SUBMIT2')
submit_button.click()
