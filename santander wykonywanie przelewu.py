from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SantanderBot:
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
		driver.get('https://www.centrum24.pl')
		print(driver.title)
		time.sleep(2)

		nik_elem = driver.find_element_by_name('nik')
		nik_elem.clear()
		nik_elem.send_keys(self.nick)
		nik_elem.send_keys(Keys.RETURN)
		time.sleep(2)

		pswd_elem = driver.find_element_by_id('ordinarypin')
		pswd_elem.clear()
		pswd_elem.send_keys(self.password)
		pswd_elem.send_keys(Keys.RETURN)
		time.sleep(2)

		next_btn = driver.find_element_by_id('back-button')
		next_btn.click()

		# oczekiwanie na wpisane kodu sms
		time.sleep(60)

		dalej_btn = driver.find_element_by_id('okBtn2')
		dalej_btn.click()
		time.sleep(2)

		# odswiezanie santandera zeby nie wylogowalo
		# for i in range(10):
		# 	session_clock = driver.find_element_by_id('session_clock')
		# 	session_clock.click()
		# 	time.sleep(240)

	def new_remittance(self):
		driver = self.driver
		recipients = [['Bob Bobson', '123123123', 1.01, 'Jakis tytul']]

		remittance_btn = driver.find_element_by_class_name('button-secondary')
		remittance_btn.click()
		time.sleep(2)

		recipient = driver.find_element_by_name('recipientInputPanel:nameBorder:nameBorder_body:name')
		recipient.clear()
		recipient.send_keys(recipients[0][0])

		account = driver.find_element_by_name('recipientInputPanel:accountNumberC:accountNumberBorder:accountNumberBorder_body:accountNumber')
		account.clear()
		account.send_keys(recipients[0][1])

		amount = driver.find_element_by_name('transferInputPanel:transferAmountBorder:transferAmountBorder_body:creditedAmount')
		amount.clear()
		amount.send_keys(recipients[0][2])

		remittance_title = driver.find_element_by_name('transferInputPanel:titleBorder:titleBorder_body:title')
		remittance_title.clear()
		remittance_title.send_keys(recipients[0][3])

		next_btn = driver.find_element_by_id('id75')
		next_btn.click()
		time.sleep(2)



tmp = []
with open('tmp.txt', 'r') as f:
	for row in f:
		tmp.append(row.strip())

# reset informacji z pliku txt (todo: dodac do funkcji np. clear_personal_data())
# with open('tmp.txt', 'w') as f:
# 	f.write('')


SantanderAccount = SantanderBot(tmp[0], tmp[1])
SantanderAccount.login()
SantanderAccount.new_remittance(recipients)
# SantanderAccount.closeBrowser()
print('done')




