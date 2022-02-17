# start: Eder
import pyautogui
import time

def on_the_map_go_to(name, type, input_left = 0, input_top = 250, input_width = 654, input_height = 1153):
	if type == 'npc':
		img_type = 'npc_on_map.png'
	elif type == 'doors':
		img_type = 'doors_on_map.png'
	elif type == 'mob':
		img_type = 'mob_on_map.png'

	podreczna_mapa_img = pyautogui.locateOnScreen('img\\Podreczna_mapa.png', region=(0, 250, 654, 524-250), confidence=0.8)
	left, top = podreczna_mapa_img[0], podreczna_mapa_img[1]
	pyautogui.click(left, top + 660)
	pyautogui.move(0, 100)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.press('delete')
	pyautogui.write(name)

	oject_on_map_img = pyautogui.locateOnScreen(f'img\\{img_type}', region=(input_left, input_top, input_width, input_height), confidence=0.93)
	pyautogui.click(oject_on_map_img)
	pyautogui.click(236, 1277)

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

def move_hero_one_tile_using_wsad(key):
	pyautogui.keyDown(key)
	time.sleep(0.1)
	pyautogui.keyUp(key)

def find_and_use_item_form_eq(item_img):
	# find_and_use_item_form_eq('Smoczy_Szafir.png')
	eq_bag = pyautogui.locateOnScreen('img\\bag_active.png', region=(3453, 792, 3828 - 3453, 921 - 792), confidence=0.99)
	if eq_bag == None:
		eq_bag = pyautogui.locateOnScreen('img\\bag_no_active.png', region=(3453, 792, 3828 - 3453, 921 - 792), confidence=0.99)
	
	x, y = eq_bag[0]+20, eq_bag[1]+20
	for i in range(0, 181, 90):
		pyautogui.click(x + i, y)
		pyautogui.moveTo(3504, 425)
		chosen_item = pyautogui.locateOnScreen(f'img\\{item_img}', region=(3230, 902, 3831 - 3230, 1412 - 902), confidence=0.95)
		if chosen_item != None:
			pyautogui.click(chosen_item, clicks=2)

			return 'found and used'
			break
	return 'not found and not used'

on_the_map_go_to('Perth', 'npc')
type_of_interaction('r')
dialog_go_through('2', 1)
dialog_go_through('1', 2)

on_the_map_go_to('Lageira', 'npc')
type_of_interaction('r')
dialog_go_through('1', 1)
dialog_go_through('2', 1)
dialog_go_through('1', 2)
dialog_go_through('2', 1)
dialog_go_through('1', 2)
dialog_go_through('3', 1)
dialog_go_through('2', 1)
dialog_go_through('1', 3)
time.sleep(0.5)

type_of_interaction('r')
dialog_go_through('1', 5)

on_the_map_go_to('Ratusz Nithal', 'doors', 238, 738)
on_the_map_go_to('Wiceburmistrz Rea Animi', 'npc')
type_of_interaction('r')
dialog_go_through('3', 1)
dialog_go_through('4', 1)
dialog_go_through('1', 1)
dialog_go_through('2', 2)
dialog_go_through('1', 2)
dialog_go_through('2', 1)
dialog_go_through('1', 1)
dialog_go_through('2', 1)
dialog_go_through('1', 2)

on_the_map_go_to('Ratusz Nithal - muzeum p.1', 'doors')
on_the_map_go_to('Ratusz Nithal - muzeum p.2', 'doors')
on_the_map_go_to('Leiff', 'npc')
type_of_interaction('r')
dialog_go_through('1', 1)
dialog_go_through('2', 1)
dialog_go_through('1', 4)
dialog_go_through('2', 1)
dialog_go_through('1', 1)

on_the_map_go_to('Ratusz Nithal - muzeum p.1', 'doors')
on_the_map_go_to('Ratusz Nithal', 'doors')
on_the_map_go_to('Nithal', 'doors', 253, 914, 335 - 253, 960 - 914)
on_the_map_go_to('Portal', 'npc')
type_of_interaction('r')
dialog_go_through('1', 1)
dialog_go_through('5', 1)
time.sleep(1)	# czekamy po tp zeby mapa sie zaladowala

on_the_map_go_to('Przemytnik Nespurik', 'npc')
type_of_interaction('r')
dialog_go_through('2', 1)
dialog_go_through('1', 2)

on_the_map_go_to('Garek', 'npc')
type_of_interaction('r')
dialog_go_through('1', 4)
dialog_go_through('2', 1)
dialog_go_through('1', 1)
dialog_go_through('2', 1)
dialog_go_through('1', 1)
dialog_go_through('1', 1)
dialog_go_through('2', 1)
dialog_go_through('1', 1)
dialog_go_through('2', 1)
dialog_go_through('1', 2)

on_the_map_go_to('Buk', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)

on_the_map_go_to('ciniec Bard', 'doors', 329, 1023)
on_the_map_go_to('Nizina Wie', 'doors')
on_the_map_go_to('liwy Vermir', 'npc')
type_of_interaction('r')
dialog_go_through('1', 9)

on_the_map_go_to('wierszcz', 'mob', 157, 627)
type_of_interaction('q')
time.sleep(0.3)
type_of_interaction('f')
on_the_map_go_to('liwy Vermir', 'npc')
type_of_interaction('r')
dialog_go_through('1', 5)

on_the_map_go_to('Podgrodzie Nithal', 'doors')
on_the_map_go_to('Nithal', 'doors', 139, 935)
on_the_map_go_to('Portal', 'npc')
type_of_interaction('r')
dialog_go_through('1', 1)
dialog_go_through('8', 1)
time.sleep(0.5)
on_the_map_go_to('Thuzal', 'doors', 254, 897)
on_the_map_go_to('Gawronich Pi', 'doors')
on_the_map_go_to('Lazurowe Wzg', 'doors', 187, 932)
on_the_map_go_to('Chata Bandyt', 'doors')
on_the_map_go_to('p.1', 'doors')
on_the_map_go_to('Chiron', 'npc')
type_of_interaction('r')
dialog_go_through('1', 9)

on_the_map_go_to('Chata Bandyt', 'doors', 292, 616)
on_the_map_go_to('Lazurowe Wzg', 'doors', 242, 965, 368 - 242, 1008 - 965)
on_the_map_go_to('Gawronich Pi', 'doors')
on_the_map_go_to('Thuzal', 'doors')
on_the_map_go_to('Gildia Mag', 'doors')
on_the_map_go_to('Fontanna Plan', 'npc')
type_of_interaction('r')
dialog_go_through('7', 1)
time.sleep(0.5)
type_of_interaction('r')
dialog_go_through('7', 1)
time.sleep(0.5)
on_the_map_go_to('Port Tuzmer', 'doors', 254, 930, 334 - 254, 954 - 930)
on_the_map_go_to('Tyberiasz', 'npc')
type_of_interaction('r')
dialog_go_through('1', 1)
dialog_go_through('2', 1)
dialog_go_through('1', 8)
on_the_map_go_to('Tuzmer', 'doors')
on_the_map_go_to('Tawerna Pod Beczk', 'doors', 187, 727, 219 - 187, 785 - 727)
on_the_map_go_to('p.1', 'doors')
on_the_map_go_to('czyzna', 'npc')
type_of_interaction('r')
dialog_go_through('1', 6)
dialog_go_through('2', 1)
dialog_go_through('1', 2)
dialog_go_through('2', 1)
dialog_go_through('1', 8)
dialog_go_through('3', 1)
dialog_go_through('1', 1)

on_the_map_go_to('mieszkanie', 'doors')
on_the_map_go_to('Szuflada', 'npc')
type_of_interaction('r')
dialog_go_through('2', 1)
dialog_go_through('1', 1)

on_the_map_go_to('p.1', 'doors', 267, 685)
on_the_map_go_to('Tawerna Pod Beczk', 'doors', 156, 632, 265 - 156, 678 - 632)
on_the_map_go_to('Tuzmer', 'doors', 260, 913, 343 - 260, 946 - 913)
on_the_map_go_to('Zakon Planu Astralnego', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)
time.sleep(0.5)
type_of_interaction('r')
dialog_go_through('5', 1)

on_the_map_go_to('Przemytnik Nespurik', 'npc')
type_of_interaction('r')
dialog_go_through('1', 1)

on_the_map_go_to('Garek', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)
dialog_go_through('2', 3)
dialog_go_through('1', 3)
dialog_go_through('2', 1)
dialog_go_through('1', 1)

on_the_map_go_to('Buk', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)

on_the_map_go_to('Zakon Planu Astralnego', 'npc')
type_of_interaction('r')
dialog_go_through('1', 1)
dialog_go_through('6', 1)
on_the_map_go_to('Podgrodzie Nithal', 'doors', 249, 596, 311 - 249, 628 - 596)
on_the_map_go_to('Grimar', 'npc')
type_of_interaction('r')
dialog_go_through('2', 1)
dialog_go_through('1', 2)

on_the_map_go_to('Stajnie', 'doors')
on_the_map_go_to('Wiadro', 'npc', 222, 796, 297 - 222, 844 - 796)
type_of_interaction('r')
dialog_go_through('2', 1)
dialog_go_through('1', 1)
on_the_map_go_to('Worek z ziemniakami', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)
on_the_map_go_to('Worek z trocinami', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)
on_the_map_go_to('Worek z cukrem', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)
on_the_map_go_to('Lasso', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)
on_the_map_go_to('Beczka z piwem', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)

on_the_map_go_to('Didier', 'npc')
type_of_interaction('r')
dialog_go_through('1', 2)

on_the_map_go_to('Wiadro', 'npc', 239, 700, 40, 40)
type_of_interaction('r')
dialog_go_through('7', 1)
dialog_go_through('1', 1)
on_the_map_go_to('Wiadro', 'npc', 319, 774, 40, 40)
move_hero_one_tile_using_wsad('w')
type_of_interaction('r')
dialog_go_through('8', 1)
dialog_go_through('1', 1)
on_the_map_go_to('Wiadro', 'npc', 216, 912, 40, 40)
type_of_interaction('r')
dialog_go_through('5', 1)
dialog_go_through('1', 1)
on_the_map_go_to('Wiadro', 'npc', 353, 909, 40, 40)
type_of_interaction('r')
dialog_go_through('4', 1)
dialog_go_through('1', 1)
on_the_map_go_to('Wiadro', 'npc', 352, 647, 40, 40)
type_of_interaction('r')
dialog_go_through('9', 1)
dialog_go_through('1', 1)
on_the_map_go_to('Didier', 'npc')
type_of_interaction('r')
dialog_go_through('1', 3)
on_the_map_go_to('Wiadro', 'npc', 236, 804, 40, 40)
type_of_interaction('r')
dialog_go_through('1', 2)
time.sleep(0.5)
type_of_interaction('r')
dialog_go_through('1', 2)

on_the_map_go_to('Perth', 'npc')
type_of_interaction('r')
dialog_go_through('2', 1)