import requests
import json
import os


with open('train.json', 'r') as reader:
	jf = json.loads(reader.read())

#print(jf['images'][0]['url'][0]) url 取法
#print(jf['images'][0]['image_id'])

path = os.getcwd()
if not os.path.isdir(path + '/train_image'):
	os.mkdir("train_image")
os.chdir(path + '/train_image')

for i in range(0,10):
	print(jf['images'][i]['image_id'])
	r = requests.get(jf['images'][i]['url'][0])
	with open(str(jf['images'][i]['image_id']) + '.jpg','wb') as f:
		f.write(r.content)