from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MargonemBot:
	global PATH
	PATH = "C:\Program Files (x86)\chromedriver.exe"
	def __init__(self, nick, password):
		self.nick = nick
		self.password = password
		self.driver = webdriver.Chrome(PATH)

	def closeBrowser(self):
		self.driver.quit()

	def login(self):
		global driver
		driver = self.driver
		driver.get('https://www.margonem.pl/')
		print(driver.title)
		time.sleep(2)

		login_btn = driver.find_element_by_class_name('menu-login')
		login_btn.click()

		login_loginForm = driver.find_element_by_id('popup-login-input')
		login_loginForm.clear()
		login_loginForm.send_keys(self.nick)

		pswd_loginForm = driver.find_element_by_id('popup-login-password')
		pswd_loginForm.clear()
		pswd_loginForm.send_keys(self.password)
		pswd_loginForm.send_keys(Keys.RETURN)
		time.sleep(2)

		enter_game_btn = driver.find_element_by_class_name('enter-game')
		enter_game_btn.click()
		time.sleep(5)

		new_interface = driver.find_element_by_class_name('ni-button')
		new_interface.click()
		time.sleep(5)

	def hero_info(self):
		global hero_info
		hero_info = {}
		driver = self.driver

		gold_amount = driver.find_element_by_class_name('herogold')
		hero_info.update({'gold':int(gold_amount.text)})
		# print('zloto:', hero_info['gold'])

		hero_lvl = driver.find_element_by_class_name('herolvl')
		hero_info.update({'lvl':hero_lvl.text.replace(' lvl', '')})
		print('lvl:', hero_info['lvl'])

		max_hero_hp = 0
		with open('stats.txt') as f:
			for row in f:
				max_hero_hp = int(row.strip())

		hero_info.update({'max_hp':max_hero_hp})
		print('hp:', hero_info['max_hp'])

		exp = driver.find_element_by_class_name('pointer-exp')
		hero_info.update({'exp':float(exp.text.replace(',', '.')[:-1])})
		print('exp:', hero_info['exp'])

	def install_perks(self):
		driver = self.driver

	def hero_collecting_experience(self):
		driver = self.driver
		lvl_up = 'no'
		if lvl_up == 'yes':
			hero_lvl = driver.find_element_by_class_name('herolvl')
			hero_info.update({'lvl':hero_lvl.text.replace(' lvl', '')})
			print('Zdobyles', hero_info['lvl'], 'lvl')

			hero_hp = driver.find_element_by_xpath('//div[@class="stats-wrapper"]/ul[@class="stats-list"]/li[@class="hp"]/span[@class="value"]')
			hero_info.update({'hp':hero_hp.text})
			# print('hp:', hero_info['hp'])
			with open('stats.txt', 'w') as f:
				f.write({'hp':hero_hp.text}) # max hp value

account_login = 'login_name'
account_password = 'password'
Your_margonem_account = MargonemBot(account_login, account_password)
Your_margonem_account.login()
Your_margonem_account.hero_info()
# Your_margonem_account.closeBrowser()
print('done')




