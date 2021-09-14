import pyautogui, time, random, pyperclip, re

def search_btn(img):
	search = pyautogui.locateOnScreen(img, confidence = 0.9)
	point_search = pyautogui.center(search)
	x, y = point_search
	pyautogui.click(x, y)

def open_hashtag():
	hashtag_num = random.randint(1, len(HASHTAGS)-1)
	pyautogui.write(f'#{HASHTAGS[hashtag_num]}')
	time.sleep(random.uniform(1.0, 1.3))
	hashtag = pyautogui.locateOnScreen('images/#.PNG', confidence = 0.8)
	point_hashtag = pyautogui.center(hashtag)
	x, y = point_hashtag
	pyautogui.click(x, y)

	time.sleep(random.uniform(0.5, 1.0))

def scroll_down_to(img):
	most_recent = pyautogui.locateOnScreen(img)
	while most_recent == None:
		pyautogui.scroll(-1000)
		most_recent = pyautogui.locateOnScreen(img)

	time.sleep(random.uniform(0.1, 0.3))
	most_recent = pyautogui.locateCenterOnScreen(img)
	pyautogui.click(most_recent.x, most_recent.y + 50)
	time.sleep(random.uniform(0.5, 0.7))

def open_account_info():
	to_follow = pyautogui.locateOnScreen('images/follow.PNG', confidence = 0.8)
	point_follow = pyautogui.center(to_follow)
	x, y = point_follow
	pyautogui.moveTo(x-35, y)
	time.sleep(random.uniform(1.5, 1.8))
	
def click_next_to_ig_logo():
	ig_logo = pyautogui.locateOnScreen('images/Instagram logo.PNG', confidence = 0.9)
	point_ig_logo = pyautogui.center(ig_logo)
	x, y = point_ig_logo
	pyautogui.click(x-100, y)

def find_website_url():
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'c')

	web_url = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)

	text = str(pyperclip.paste())#.encode('utf-8')

	current_website_urls = []
	for groups in web_url.findall(text):
		current_website_urls.append(groups[0])

	pyautogui.move(0, -100)
	time.sleep(random.uniform(1.0, 1.3))

	return current_website_urls

def next_post():
	next_post = pyautogui.locateOnScreen('images/next.PNG', confidence=0.8)
	point_next_post = pyautogui.center(next_post)
	x, y = point_next_post
	pyautogui.click(x, y)
	time.sleep(random.uniform(1.5, 2.0))

def save_urls(urls):
	with open("myfile.txt", "a") as f:
	    f.write("Hello \n")
	    f.writelines(urls)

# all hashtags to be searched
HASHTAGS = [
	'instagram',
	'instagood',
	'mood',
]

accounts_to_access = 3
search_btn('images/search.PNG')
open_hashtag()
scroll_down_to('images/most recent.PNG')
web_urls = []
counter = 1
for account in range(accounts_to_access):
	print(f'{counter}/{accounts_to_access}')
	open_account_info()
	web_urls.append(find_website_url())
	next_post()
	counter += 1

for links in web_urls:
	for link in links:
		print(link)
