from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pyperclip

class ScoopIt:
	global PATH
	PATH = "./driver/chromedriver.exe"
	def __init__(self, nick, password):
		self.nick = nick
		self.password = password
		self.driver = webdriver.Chrome(PATH)

	def closeBrowser(self):
		self.driver.quit()

	def login(self):
		global driver
		driver = self.driver
		driver.get('https://www.scoop.it/login')
		print(driver.title)
		time.sleep(2)

		login_loginForm = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div/input')
		login_loginForm.clear()
		login_loginForm.send_keys(self.nick)

		pswd_loginForm = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/input')
		pswd_loginForm.clear()
		pswd_loginForm.send_keys(self.password)
		pswd_loginForm.send_keys(Keys.RETURN)
		time.sleep(2)

	def addPost(self):
		link_input = driver.find_element_by_xpath('//*[@id="urlChooserField"]')
		link_input.clear()
		link_input.send_keys(link_post)
		link_input.send_keys(Keys.RETURN)

		while (True):
			try:
				new_scoop = driver.find_element_by_class_name('h-scoopitwindow-post-content')
				break
			except NoSuchElementException:
				time.sleep(1)

		input_description = driver.find_element_by_class_name('h-scoopitwindow-post-content')
		input_description.clear()
		input_description.send_keys(text_post)
		

data = []
with open("scoop it dane.txt", encoding='utf8') as f:
	for row in f:
		data.append(row.strip())

user_login = data[0]
user_paswd = pyperclip.paste()
link_post = data[1]
text_post = ''

for i in range(2, len(data)):
	text_post += (data[i] + '\n')

pyperclip.copy('')

ScoopItUser = ScoopIt(user_login, user_paswd)
ScoopItUser.login()
ScoopItUser.addPost()
