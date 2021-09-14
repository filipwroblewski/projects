import pyautogui
import pyperclip

def check_coin_rain():
	try:
		coin_drop_img = pyautogui.locateOnScreen('img\\free coins.PNG', region=(0, 700, 400, 320))
		coin_drop_img_X, coin_drop_img_Y = pyautogui.center(coin_drop_img)
		pyautogui.click(x = coin_drop_img_X, y = coin_drop_img_Y, duration=0.5)
		print('--- Coin rain ---')
		pyautogui.moveTo(x = 1650, y = 500, duration=0.5) # odsuniecie kursora na bok
	except:
		print('Nie zlokalizowano Coin rain')

counter = 0
check = 'start'
print(check)
i = 0
money = []
win = 'no'

while win != 'yes':
	print('iteracja nr ', i)
	place_bet_img = ''
	try:
		while place_bet_img == '' or place_bet_img == None:
			place_bet_img = pyautogui.locateOnScreen('img\\place bet.PNG', region=(900, 600, 300, 150))
			check = 'ready to place bet'
	except:
		print('place bet btn error')

	if check == 'ready to place bet':
		pyautogui.doubleClick(x = 1748, y = 165, duration=0.5) # duration=0.5
		pyautogui.hotkey('ctrl', 'c')
		wallet_value = pyperclip.paste()
		current_money_in_wallet = float(wallet_value.replace(',', '.'))
		money.append(current_money_in_wallet)

		if money[0] < money[-1]:
			print('--- Jestes do przodu! ---')
			break

		if counter == 13:
			x2_img = pyautogui.locateOnScreen('img\\x2.PNG', region=(1370, 550, 100, 100))
			x2_img_X, x2_img_Y = pyautogui.center(x2_img)
			pyautogui.click(x = x2_img_X, y = x2_img_Y, duration=0.5)
			print('x2')
			counter = 0
		else:
			counter += 1

		place_bet_img = pyautogui.locateOnScreen('img\\place bet.PNG', region=(900, 600, 300, 150))
		place_bet_img_X, place_bet_img_Y = pyautogui.center(place_bet_img)
		pyautogui.click(x = place_bet_img_X, y = place_bet_img_Y, duration=0.5)
		print('placing bet successfully')
		pyautogui.moveTo(x = 1650, y = 500, duration=0.5) # odsuniecie kursora na bok
		check = 'w8'
		i += 1

		check_coin_rain()

		print('oczekiwanie na wynik losowania...')
		pipe_img = ''
		try:
			while pipe_img == '' or pipe_img == None:
				pipe_img = pyautogui.locateOnScreen('img\\pipe.PNG', region=(1070, 360, 100, 200))
		except:
			print('rolling img error')

	check = 'w8'
	print('counter =', counter)

print('-' * 10)
print('All wykonan: ', i)
print('Jak to bylo z kasa: ', money)