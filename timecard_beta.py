from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Get the user info
user = 'bz15'
work_list = dict(tuesday=["09:30AM", "02:00PM"], thursday=["10:00AM", "02:30PM"])
pwd = input("Please enter your password: ")

date_list = dict(sunday=[0, 28], monday=[4, 32], tuesday=[8, 36], wednesday=[12, 40], thursday=[16, 44],
				 friday=[20, 48], saturday=[24, 52])
submit_list = dict(finish="F", save ="L")


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


def locate_timecard():
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


def select_one_day(Weekday, hour_start, hour_end):
	el3 = driver.find_elements_by_xpath("//select")
	date_list = dict(sunday=[0, 28], monday=[4, 32], tuesday=[8, 36], wednesday=[12, 40], thursday=[16, 44],
					 friday=[20, 48], saturday=[24, 52])
	indice = date_list[Weekday]

	for index in indice:
		Select(el3[index]).select_by_visible_text(hour_start)
		Select(el3[index + 1]).select_by_visible_text(hour_end)

def finish_and_submit(submit = 'L', pause=False):
	if not pause:
		submit_button = driver.find_element_by_name('SUBMIT2')
		submit_button.click()

		save = Select(driver.find_element_by_name("VAR5"))

		# L: save. F: finish and send to adviser
		save.select_by_value(submit)
		submit_button = driver.find_element_by_name('SUBMIT2')
		submit_button.click()
		driver.close()

# deselet all time slots in case you have messed up before
def unselect_all():
	el3 = driver.find_elements_by_xpath("//select")
	for el in el3:
		Select(el).select_by_index(0)

login_to_timecard(user, pwd, driver)
locate_timecard()
for key in work_list:
	start = work_list[key][0]
	end = work_list[key][1]
	select_one_day(key, start, end)

finish_and_submit()
