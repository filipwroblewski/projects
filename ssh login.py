import pyautogui, os, paramiko

uname = 'user_name'
pswd = 'password'
ip_address_1 = pyautogui.prompt(text='Input ip address (1)', title='ip address 1' , default='')
ip_address_2 = pyautogui.prompt(text='Input ip address (2)', title='ip address 2' , default='')

stdin = ''
stdout = ''
stderr = ''
try:
	pyautogui.alert(text='Rozpoczynam logowanie do ssh', title='logowanie do ssh' , buttton='OK')
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    stdin, stdout, stderr = ssh.exec_command(f'ls')# efekt do pliku
except:
	pyautogui.alert(text='Blad logowania do ssh', title='logowanie do ssh' , buttton='OK')
	print('connection error')

response = f'''stdin:
{stdin}
---
stdout:
{stdout}
---
stderr:
{stderr}'''

with open('f.txt', 'w') as f:
	f.write(response)

print('done')