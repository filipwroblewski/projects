import pyautogui, time

password = ''
with open('password_to_league_of_legends.txt') as file:
    for row in file:
        password = row.split()

pyautogui.click(x=129, y=1059, duration=0.5)
pyautogui.typewrite('League of legends', interval=0.05)
pyautogui.press('enter')
time.sleep(5)

time.sleep(3)
account_login = 'login_name'
pyautogui.click(452, 438) # login
pyautogui.typewrite(account_login, interval=0.05)
pyautogui.click(452, 498) # password
pyautogui.typewrite(f'{password[0]}', interval=0.05)
pyautogui.click(505, 653) # sign in
