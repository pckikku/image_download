
from imutils import paths
import argparse
import cv2
import requests, os

path_text = "url.txt"

o = open(path_text,"r")
url0 = o.read()
o.close()

## list, containing downloaded files 
urls = url0.split()
print("The number of urls: {}".format(len(urls)))
print("____________________________")
for url in urls[:10]:
    print(url)


loc_data = "./data/"
try:
    os.makedirs(loc_data)
except:
    pass
iimage = 0
for url in urls:
    try:
        f = open(loc_data + 'image{:05.0f}.jpg'.format(iimage),'wb')
        f.write(requests.get(url).content)
        f.close()
        iimage += 1
    except Exception as e:
        print("\n{} {}".format(e,url))
        pass