import time, datetime, win32gui, json, os.path



def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  return "{0}h {1}m {2}s".format(int(hours),int(mins),sec)


def if_file_exist():
	if os.path.exists(get_file_name()):
		with open(get_file_name(), "r") as read_file:
			all_windows = json.load(read_file)

		print(f"data loaded from file: {get_file_name()}")
		return all_windows


def get_file_name():
	today = datetime.datetime.now()
	f_name = f'{today.year}_{today.month}_{today.day}.json'
	return f_name

def to_json_file(dictionary):
	# Serializing json
	json_object = json.dumps(dictionary, indent = 4)
	with open(get_file_name(), "w") as outfile:
		outfile.write(json_object)


all_windows = {}
active_window_name = ''
stopperStatus = ''

all_windows = if_file_exist()
while True:
	new_window_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
	
	if active_window_name != new_window_name:
		if stopperStatus != '':
			stopperStatus = 'end'
			end_time = time.time()
			time_lapsed = end_time - start_time
			# print(active_window_name, round(time_lapsed))

			if active_window_name in all_windows:
				all_windows[active_window_name] += round(time_lapsed)
			else:
				all_windows[active_window_name] = round(time_lapsed)

			print(active_window_name, all_windows[active_window_name])
			to_json_file(all_windows)

			
		stopperStatus = 'start'
		start_time = time.time()

		active_window_name = new_window_name

	time.sleep(1)


# todo
# exe
