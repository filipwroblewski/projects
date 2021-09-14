import pyautogui
import time

def check_coin_rain():
	try:
		coin_drop_img = pyautogui.locateOnScreen('img\\free coins.PNG', region=(0, 700, 400, 320))
		coin_drop_img_X, coin_drop_img_Y = pyautogui.center(coin_drop_img)
		pyautogui.click(x = coin_drop_img_X, y = coin_drop_img_Y, duration=0.5)
		print('--- Coin rain ---')
		pyautogui.moveTo(x = 1650, y = 500, duration=0.5)
	except:
		pass

print('start')
while True:
	time.sleep(10)
	check_coin_rain()
