import requests
import json
import os
import time

with open('train.json', 'r') as reader:
	jf = json.loads(reader.read())

#print(jf['images'][0]['url'][0]) url 取法
#print(jf['images'][0]['image_id'])

path = os.getcwd()
if not os.path.isdir(path + '/train_image'):
	os.mkdir("train_image")
os.chdir(path + '/train_image')
start = input("start: ")
end = input("end: ")

for i in range(int(start), int(end)):#len(jf['images']) - 1):
	try:
		r = requests.get(jf['images'][i]['url'][0])
		with open(str(jf['images'][i]['image_id']) + '.jpg','wb') as f:
			f.write(r.content)
	except:
		print(jf['images'][i]['image_id'],"error")
	time.sleep(1)

