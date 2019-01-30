from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

##Get to the main page
user = "xil16"
pwd = "lxylmylzh6224"

driver.get("http://www.meizitu.com/a/5443.html")

elem = driver.find_elements_by_xpath("//img")





for i in elem:
	print(i['src'])

# for index in indice:
# 	Select(el3[index]).select_by_visible_text(hour_start)
# 	Select(el3[index+1]).select_by_visible_text(hour_end)
