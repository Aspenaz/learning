images = []

base_url = 'http://localhost:8000/simple_server'
src = "img/owl-alcohol.png" 

img_url = ('{base_url}/{src}'.format(base_url=base_url, src=src))
name = img_url.split('/')[-1]
images.append(dict(name=name, url=img_url))

print()
print('img_url:', img_url)
print('name:', name)
print('images:', images)
print()

print('name:', images[0]['name'])
print('url:', images[0]['url'])
print()

# img_url: http://localhost:8000/simple_server/img/owl-alcohol.png
# name: owl-alcohol.png

# images: [      # list of dictionaries.
#     {
#         'name': 'owl-alcohol.png', 
#         'url': 'http://localhost:8000/simple_server/img/owl-alcohol.png'
#       }
#     ]

# name: owl-alcohol.png
# url: http://localhost:8000/simple_server/img/owl-alcohol.png


ext_map = {     # dictionary of list.
    'png': ['.png'],
    'jpg': ['.jpg', '.jpeg'],
}

type_ = 'jpg'
print('type_:', type_, ':', ext_map[type_])       # ['.jpg', '.jpeg']
type_ = 'png'
print('type_:', type_, ':', ext_map[type_])       # ['.png']
print('ext_map dict:', ext_map)
print()

import os 

filename = images[0]['name']
print('filename:', filename)
name, extension = os.path.splitext(filename.lower())
print('name:', name, '      extension:', extension)
print()

filename = 'owl-alcohol.123'
print('filename:', filename)
name, extension = os.path.splitext(filename.lower())
print('name:', name, '      extension:', extension)
print()

import requests

# img_data = requests.get(img['url']).content 
img_data = requests.get(images[0]['url']).content 
print('img_data:', img_data)