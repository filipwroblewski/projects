import pyautogui, time, random
from emoji import emojize

def next_post():
	next_post = pyautogui.locateOnScreen('images/next.PNG', confidence=0.8)
	point_next_post = pyautogui.center(next_post)
	x, y = point_next_post
	pyautogui.click(x, y, duration = random.uniform(2.5, 3.5))
	time.sleep(random.uniform(1.5, 2.0))

accountType = 'logo'

COMMENTS = []
with open(f'comments - {accountType}.txt') as f:
	for l in f:
		COMMENTS.append(l.strip())

HASHTAGS = []
with open(f'hashtags - {accountType}.txt') as f:
	for l in f:
		HASHTAGS.append(l.strip())

EMOTICONS = []
with open(f'emoticons - {accountType}.txt') as f:
	for l in f:
		EMOTICONS.append(l.strip())

accounts_to_follow = random.randint(38, 40)
search = pyautogui.locateOnScreen('images/search.PNG', confidence = 0.9)
point_search = pyautogui.center(search)
x, y = point_search
pyautogui.click(x, y)

hashtag_num = random.randint(1, len(HASHTAGS)-1)
pyautogui.write(f'#{HASHTAGS[hashtag_num]}')
time.sleep(random.uniform(2.5, 3.0))
pyautogui.click('images/# new.PNG')
time.sleep(random.uniform(3.5, 4.5))

most_recent = pyautogui.locateOnScreen('images/most recent.PNG')
while most_recent == None:
	pyautogui.scroll(-1000)
	most_recent = pyautogui.locateOnScreen('images/most recent.PNG')

time.sleep(random.uniform(0.1, 0.3))
most_recent = pyautogui.locateCenterOnScreen('images/most recent.PNG')
pyautogui.click(most_recent.x, most_recent.y + 50)
time.sleep(random.uniform(0.5, 0.7))

counter = 0
num_of_posts = 0
while counter < accounts_to_follow:
	to_follow = pyautogui.locateOnScreen('images/follow.PNG', confidence = 0.8)
	to_like = pyautogui.locateOnScreen('images/empty heart.PNG', confidence = 0.8)
	limited_comments = pyautogui.locateOnScreen('images/comments limited.PNG', confidence = 0.9)
	

	if to_follow != None and to_like != None and limited_comments == None:
		durations = []
		for i in range(6):
			durations.append(random.uniform(0.4, 1.0))

		print(f'account ({counter + 1}/{accounts_to_follow}) ready to follow')
		# follow account
		point_follow = pyautogui.center(to_follow)
		x, y = point_follow
		pyautogui.click(x, y, duration = durations[0])

		# like post
		point_like = pyautogui.center(to_like)
		x, y = point_like
		pyautogui.click(x, y, duration = durations[1])

		# add comment (if == None -> Next post)
		comment = pyautogui.locateOnScreen('images/comment.PNG', confidence=0.8)
		if comment == None:
			next_post()
		else:
			point_comment = pyautogui.center(comment)
			x, y = point_comment
			pyautogui.click(x, y, duration = durations[2]/3)
			comment_num = random.randint(1, len(COMMENTS)-1)
			pyautogui.write(COMMENTS[comment_num], interval = random.uniform(0.05, 0.15))
			print(COMMENTS[comment_num])

		# get access to emoticons
		emoticon = pyautogui.locateOnScreen('images/emoticons.PNG', confidence=0.8)
		point_emoticon = pyautogui.center(emoticon)
		x, y = point_emoticon
		pyautogui.click(x, y, duration = durations[3])

		# add emoji
		time.sleep(random.uniform(2.5, 3.5))
		emoji_num = random.randint(1, len(EMOTICONS)-1)
		emoji = pyautogui.locateOnScreen(EMOTICONS[emoji_num], confidence=0.9)
		print(EMOTICONS[emoji_num])
		point_emoji = pyautogui.center(emoji)
		x, y = point_emoji
		pyautogui.click(x, y, duration = durations[4])

		# post comment
		comment = pyautogui.locateOnScreen('images/Post comment.PNG', confidence=0.8)
		point_comment = pyautogui.center(comment)
		x, y = point_comment
		pyautogui.click(x, y, duration = durations[5])

		counter += 1

	next_post()
	
	num_of_posts += 1

print(f'Obejrzane posty: {num_of_posts}, liczba skomentowanych postow: {counter}')

hour, minute = map(int, time.strftime("%H %M").split())
print(f'Next start: {hour+1}:{minute+1}')
