# start: Tuzmer
import pyautogui
import time

def on_the_map_go_to(Name, type, input_left = 0, input_top = 250, input_width = 654, input_height = 1153):
	if type == 'npc':
		img_type = 'npc_on_map.png'
	elif type == 'doors':
		img_type = 'doors_on_map.png'

	podreczna_mapa_img = pyautogui.locateOnScreen('img\\Podreczna_mapa.png', region=(0, 250, 654, 524-250), confidence=0.80)
	left, top = podreczna_mapa_img[0], podreczna_mapa_img[1]
	pyautogui.click(left, top + 660)
	pyautogui.move(0, 100)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.press('delete')
	pyautogui.write(Name)

	object_on_map_img = pyautogui.locateOnScreen(f'img\\{img_type}', region=(input_left, input_top, input_width, input_height), confidence=0.98)
	if object_on_map_img == None:
		time.sleep(0.5)
		object_on_map_img = pyautogui.locateOnScreen(f'img\\{img_type}', region=(input_left, input_top, input_width, input_height), confidence=0.98)
	pyautogui.click(object_on_map_img)
	pyautogui.click(21, 1241)

	time.sleep(0.5)
	while True:
		coordinates_1st_img = pyautogui.screenshot(region=(2006, 310, 2102-2006, 350-310))
		time.sleep(0.5)
		coordinates_2nd_img = pyautogui.screenshot(region=(2006, 310, 2102-2006, 350-310))
		time.sleep(0.5)
		coordinates_3rd_img = pyautogui.screenshot(region=(2006, 310, 2102-2006, 350-310))

		if coordinates_1st_img == coordinates_2nd_img == coordinates_3rd_img:
			time.sleep(0.5)
			break

def type_of_interaction(key):
	pyautogui.press(key)
	time.sleep(0.5)

def dialog_go_through(num, reps):
	for i in range(1, reps + 1):
		pyautogui.press(num)
		time.sleep(0.5)

def buy_from_shop(item_img_name, count):
	object_to_buy = pyautogui.locateOnScreen(f'img\\{item_img_name}', region=(1269, 502, 2548 - 1269, 1832 - 502), confidence=0.9)
	for i in range(1, count + 1):
		pyautogui.click(object_to_buy)
		time.sleep(0.1)
	accept_img = pyautogui.locateOnScreen(f'img\\shop_accept.png', region=(1269, 502, 2548 - 1269, 1832 - 502), confidence=0.9)
	pyautogui.click(accept_img)

def move_hero_one_tile_using_wsad(key):
	pyautogui.keyDown(key)
	time.sleep(0.1)
	pyautogui.keyUp(key)

on_the_map_go_to('Port Tuzmer', 'doors', 254, 930, 334 - 254, 954 - 930)
on_the_map_go_to('Latarniane Wybrze', 'doors', 0, 569, 37 - 0, 640 - 569)
on_the_map_go_to('Henk Hornigold', 'npc')
type_of_interaction('r')
dialog_go_through('4', 1)
dialog_go_through('1', 5)

on_the_map_go_to('Tawerna pod Szemrz', 'doors', 513, 564)
on_the_map_go_to('Klaban Grantis', 'npc')
type_of_interaction('r')
dialog_go_through('3', 1)
dialog_go_through('1', 4)

on_the_map_go_to('Latarniane Wybrze', 'doors', 113, 895)
on_the_map_go_to('Port Tuzmer', 'doors')
on_the_map_go_to('Kendala', 'doors')
on_the_map_go_to('Kendal', 'npc')
move_hero_one_tile_using_wsad('s')
type_of_interaction('r')
dialog_go_through('4', 1)
dialog_go_through('1', 1)


time.sleep(4*60)
type_of_interaction('r')
dialog_go_through('4', 1)
dialog_go_through('1', 1)

on_the_map_go_to('Port Tuzmer', 'doors')
on_the_map_go_to('Latarniane Wybrze', 'doors', 0, 569, 37 - 0, 640 - 569)
on_the_map_go_to('Tawerna pod Szemrz', 'doors', 513, 564)
on_the_map_go_to('Klaban Grantis', 'npc')
type_of_interaction('r')
dialog_go_through('3', 1)
dialog_go_through('1', 1)

on_the_map_go_to('Aslan Szpon', 'npc')
move_hero_one_tile_using_wsad('w')
type_of_interaction('r')
dialog_go_through('4', 1)
dialog_go_through('1', 5)

on_the_map_go_to('Latarniane Wybrze', 'doors', 113, 895)
on_the_map_go_to('Port Tuzmer', 'doors')
on_the_map_go_to('Tuzmer', 'doors')
on_the_map_go_to('Zakon Planu Astralnego', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)
time.sleep(0.5)
type_of_interaction('r')
dialog_go_through('6', 1)
time.sleep(0.5)
on_the_map_go_to('Winnica Meflakasti', 'doors')
on_the_map_go_to('Wazir hen Mefla', 'npc')
type_of_interaction('r')
dialog_go_through('3', 1)
dialog_go_through('1', 3)

on_the_map_go_to('Nithal', 'doors')
on_the_map_go_to('Portal', 'npc')
type_of_interaction('r')
dialog_go_through('1', 1)
dialog_go_through('7', 1)
time.sleep(0.5)
type_of_interaction('r')
dialog_go_through('7', 1)
time.sleep(0.5)

on_the_map_go_to('Port Tuzmer', 'doors')
on_the_map_go_to('Latarniane Wybrze', 'doors', 0, 569, 37 - 0, 640 - 569)
on_the_map_go_to('Tawerna pod Szemrz', 'doors', 513, 564)
on_the_map_go_to('Aslan Szpon', 'npc')
move_hero_one_tile_using_wsad('w')
type_of_interaction('r')
dialog_go_through('4', 1)
dialog_go_through('1', 1)

on_the_map_go_to('Miralas', 'npc')
type_of_interaction('r')
dialog_go_through('4', 1)
dialog_go_through('1', 3)

on_the_map_go_to('Latarniane Wybrze', 'doors', 113, 895)
on_the_map_go_to('Henk Hornigold', 'npc')
time.sleep(0.5)
type_of_interaction('r')
dialog_go_through('1', 2)
time.sleep(0.5)
on_the_map_go_to('Port Tuzmer', 'doors')
on_the_map_go_to('Marynarz Typolis', 'npc')
time.sleep(0.5)
move_hero_one_tile_using_wsad('w')
move_hero_one_tile_using_wsad('s')
time.sleep(1)
type_of_interaction('r')
dialog_go_through('3', 1)
dialog_go_through('1', 3)

on_the_map_go_to('Latarniane Wybrze', 'doors', 0, 569, 37 - 0, 640 - 569)
on_the_map_go_to('Tawerna pod Szemrz', 'doors', 513, 564)
on_the_map_go_to('Miralas', 'npc')
type_of_interaction('r')
dialog_go_through('4', 1)
dialog_go_through('1', 2)

on_the_map_go_to('Hak Odeward', 'npc')
type_of_interaction('r')
dialog_go_through('4', 1)
dialog_go_through('1', 3)

on_the_map_go_to('Latarniane Wybrze', 'doors', 113, 895)
on_the_map_go_to('Henk Hornigold', 'npc')
type_of_interaction('r')
dialog_go_through('1', 3)

on_the_map_go_to('Port Tuzmer', 'doors')
on_the_map_go_to('Tuzmer', 'doors')
on_the_map_go_to('Przemytnik Polifiks', 'npc')
type_of_interaction('r')
dialog_go_through('4', 1)
dialog_go_through('1', 4)

on_the_map_go_to('Port Tuzmer', 'doors', 254, 930, 334 - 254, 954 - 930)
on_the_map_go_to('Latarniane Wybrze', 'doors', 0, 569, 37 - 0, 640 - 569)
on_the_map_go_to('Henk Hornigold', 'npc')
type_of_interaction('r')
dialog_go_through('1', 3)

on_the_map_go_to('Tawerna pod Szemrz', 'doors', 513, 564)
on_the_map_go_to('Barman Wichran', 'npc')
type_of_interaction('r')
dialog_go_through('1', 5)

on_the_map_go_to('Latarniane Wybrze', 'doors', 113, 895)
on_the_map_go_to('Henk Hornigold', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)

on_the_map_go_to('Port Tuzmer', 'doors')
on_the_map_go_to('Tuzmer', 'doors')
on_the_map_go_to('Zakon Planu Astralnego', 'npc')