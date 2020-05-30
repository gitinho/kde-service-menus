import requests
import json
import os
import time
import base64

time.sleep(2)

urlbb = "https://api.imgbb.com/1/upload"
url = "http://localhost:5000/search"

databb = {
    "key": 'dbe8b8a736204586994c8400af07166d'
}

data = {
    "resized_images": False,  # Or True
    "cloud_api": False
}
for fi in range(len(os.sys.argv)-1):
    image_path = os.sys.argv[fi+1]
    image = open(image_path, 'rb')
    databb["image"] = base64.b64encode(image.read())
    print('uploading ' + os.path.basename(image_path) + '...')
    rbb = requests.post(urlbb, databb)
    print('uploaded!')
    response = rbb.json()
    image_url = response['data']['url']

    data["image_url"] = image_url
    headers = {'Content-type': 'application/json'}
    print('analysing...')
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print('analysed!')

    # r.json to get the response as json
    best_guess = r.json()['best_guess']
    os.system("notify-send -a 'Image tagger' '" + os.path.basename(image_path) + "' '" + best_guess + "'")

    newname = best_guess + ' - ' + os.path.basename(image_path)
    print(newname)
    os.rename(image_path, newname)

os.system('pkill python')
