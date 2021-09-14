import subprocess,os

def openFolder(path):
	subprocess.Popen(f'explorer {os.path.realpath(path)}')

folder1 = 'D:\\a'
folder2 = 'D:\\b'
folder3 = 'D:\\c'
folder4 = 'D:\\d'

paths = [folder1, folder2, folder3, folder4]
for path in paths:
	openFolder(path)