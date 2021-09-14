from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ytChannelFinder:
	global PATH
	PATH = "C:\Program Files (x86)\chromedriver.exe"

	def __init__(self):
		self.driver = webdriver.Chrome(PATH)

	def closeBrowser(self):
		self.driver.quit()

	def start(self):
		global driver
		driver = self.driver
		driver.get('https://www.youtube.com/')
		print(driver.title)

	def closePoppingElems(self):
		popping_elem = driver.find_element_by_id('text')
		print(popping_elem.value)

	def findChannel(self, channel_name):
		# type channel
		input_elem = driver.find_element_by_id('search')
		input_elem.clear()
		input_elem.send_keys(self.channel_name)
		input_elem.send_keys(Keys.RETURN)
		time.sleep(2)



wr = ytChannelFinder()
wr.start()
wr.closePoppingElems()
# wr.findChannel('wrobl_ew/ski')
# wr.closeBrowser()