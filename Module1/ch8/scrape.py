
import argparse
import base64
import json
import os
from bs4 import BeautifulSoup
import requests

def scrape(url, format_, type_):
    print('\n==========start scrape==========\n')
    print()
    print('url:', url)
    print('format_:', format_)
    print('type_:', type_)
    print()
    try:
        page = requests.get(url)
        print('page:', page)
        print()
    except requests.RequestException as rex:    # The RequestException is the base exception class for all the exceptions in the requests library.
        print(str(rex))
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        print('soup:', soup)
        images = _fetch_images(soup, url)
        print('images in scrape after _fetch_images():\n', images)
        images = _filter_images(images, type_)
        print('images in scrape after _filter_images():\n', images)
        print('\n==========end scrape==========\n')
        print()
        _save(images, format_)
                
def _fetch_images(soup, base_url):
    print('\n***** start in _fetch_images() *****\n')
    print('soup:\n', soup)
    print('\nbase_url:', base_url)
    images = []
    for img in soup.findAll('img'):
        print('\n================================')
        print('\nimg =', img)
        src = img.get('src')
        print('\nsrc =', src)
        img_url = ('{base_url}/{src}'.format(base_url=base_url, src=src))
        print('\nimg_url = {''base_url''}/{''src''} =', img_url)
        name = img_url.split('/')[-1]
        print('\nname =', name)
        images.append(dict(name=name, url=img_url))
        print('\nimages =', images) 
        print('================================\n')
    print('\n***** end in _fetch_images() *****\n')
    return images 

def _filter_images(images, type_):
    print('\n***** start in _filter_images() *****\n')
    if type_ == 'all':
        return images 
    ext_map = {
        'png': ['.png'],
        'jpg': ['.jpg', '.jpeg'],
    }
    print('ext_map:', ext_map)
    print('img in images:', (img for img in images if _matches_extension(img['name'], ext_map[type_])))
    print('\n***** end in _filter_images() *****\n')
    return [
        img for img in images if _matches_extension(img['name'], ext_map[type_])
    ]
    
def _matches_extension(filename, extension_list):
    name, extension = os.path.splitext(filename.lower())
    print('\n***** start in _matches_extension() *****\n')
    print('name:', name)
    print('extension:', extension)
    print('\n***** end in _matches_extension() *****\n')
    return extension in extension_list 

def _save(images, format_):
    if images:
        if format_ == 'img':
            _save_images(images)
        else:
            _save_json(images)
        print('Done')
    else:
        print('No images to save.')
        
def _save_images(images):
    for img in images:
        img_data = requests.get(img['url']).content 
        with open(img['name'], 'wb') as f:
            f.write(img_data)
            
def _save_json(images):
    data = {}
    for img in images:
        img_data = requests.get(img['url']).content 
        b64_img_data = base64.b64encode(img_data)
        str_img_data = b64_img_data.decode('utf-8')
        data[img['name']] = str_img_data 

    with open('images.json', 'w') as ijson:
        ijson.write(json.dumps(data))
        


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description='Scrape a webpage.')
    
    parser.add_argument(
        '-t',
        '--type',
        choices=['all', 'png', 'jpg'], 
        default='all',
        help='The image type we want to scrape.')
    
    parser.add_argument(
        '-f',
        '--format',
        choices=['img', 'json'], 
        default='img',
        help='The format images are saved to.')
    
    parser.add_argument(
        'url',
        help='The URL we want to scrape for images.')
    
    args = parser.parse_args()
    print('\n*****args =', args)
    print('*****args.url =', args.url)
    print('*****args.format =', args.format)
    print('*****args.type =', args.type)
    print('\n')
    
    scrape(args.url, args.format, args.type)