import time
import win32gui
import json


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  return "{0}h {1}m {2}s".format(int(hours),int(mins),sec)

def to_json_file(dictionary, f_name):
	# Serializing json 
	json_object = json.dumps(dictionary, indent = 4)
	with open(f"{f_name}.json", "w") as outfile:
		outfile.write(json_object)


all_windows = {}
active_window_name = ''
stopperStatus = ''
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
			to_json_file(all_windows, "all_windows")

			
		stopperStatus = 'start'
		start_time = time.time()

		active_window_name = new_window_name

	time.sleep(1)


