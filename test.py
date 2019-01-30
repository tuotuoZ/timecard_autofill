from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Get the user info
user = input("Please enter your user name: ")
pwd = input("Please enter your password: ")
Weekday = input("Please enter a working day: ").lower()
hour_start = input("Please enter the start time you will work: ")
hour_end = input("Please enter the end time of your work: ")

driver = webdriver.Chrome()

def login_to_timecard(username, password, driver):
	# Get to the main page
	driver.get("http://thehub.hampshire.edu")
	assert "TheHub Main Menu" in driver.title
	elem = driver.find_element_by_id("acctLogin")
	elem.click()
	# Fill the username and password to login
	elem = driver.find_element_by_id("USER_NAME")
	elem.send_keys(username)
	elem = driver.find_element_by_id("CURR_PWD")
	elem.send_keys(password)
	elem.send_keys(Keys.RETURN)
	# Navigate to the timecard page
	student_link = driver.find_element_by_link_text('Students')
	student_link.click()
	timecard_link = driver.find_element_by_link_text('Enter a Timecard')
	timecard_link.click()


def select_job_and_fill():
	# Select a job the id is LIST_VAR1_
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
	date_list = dict(sunday=[0, 28], monday=[4, 32], tuesday=[8, 36], wednesday=[12, 40], thursday=[16, 44],
					 friday=[20, 48], saturday=[24, 52])
	indice = date_list[Weekday]

	for index in indice:
		Select(el3[index]).select_by_visible_text(hour_start)
		Select(el3[index + 1]).select_by_visible_text(hour_end)

	submit_button = driver.find_element_by_name('SUBMIT2')
	submit_button.click()

	save = Select(driver.find_element_by_name("VAR5"))

	# L: save. F: finish and send to adviser
	save.select_by_value("L")
	submit_button = driver.find_element_by_name('SUBMIT2')
	submit_button.click()
	driver.close()


login_to_timecard(user, pwd, driver)
select_job_and_fill()


