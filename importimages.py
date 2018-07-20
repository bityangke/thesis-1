import os
import sys
import pprint
import urllib
import unicodedata
import shutil
from googleapiclient.discovery import build

def main():
    if len(sys.argv) != 3:
        print("Usage: python importimages.py <query in ""> <image title in "">")
        exit(1)

    query = sys.argv[1]
    name = sys.argv[2]
    path = "/Users/sanieaakhtar/VirtualEnvs/imagedata/images/"

    service = build("customsearch", "v1", developerKey="AIzaSyBQl5CyhGrEY6yUR7tsjo5fYQu7LZWyeaw")

    imagelinks = []
    count = 0
    while (count < 3):
        res = service.cse().list(
            q = query,
            cx = '008811527317547926365:d-prjjj3z0g',
            searchType = 'image',
            safe = 'off',
            imgType = 'photo',
            start = (count * 10) + 1,
            imgSize = 'large'
            ).execute()
        test = 0

        if not 'items' in res:
            print 'No results obtained. \n res is: {}'.format(res)

        else:
        	for item in res['items']:
        		# print(res['items'].index(item))
        		link = item['link']
        		imagelinks.append(link.encode("ascii")) #same append operation works here as desired
        		test = test + 1
        		# print('Test:', test)
        		# print('Link: {}\n'.format(link.encode("ascii")))
                # imagelinks.append(link.encode("ascii")) this append here does not work
        
        print('Count: {}\n'.format(count))
        count += 1

#         name = res['queries']['request'][0]['searchTerms']

    print("Number of images: ", len(imagelinks))

    imagespath = path + name + '/'

    if os.path.isdir(imagespath):
    	shutil.rmtree(imagespath)
    os.mkdir(path + name)

    for ind, item in enumerate(imagelinks):
        #print('{}'.format(item))
        #print('{}'.format(res['items'].index(item)))
        urllib.urlretrieve(item, imagespath + '{}_{}.jpg'.format(name, ind))
                
        #urllib.urlretrieve(item['link'], '/Users/sanieaakhtar/VirtualEnvs/imagedata/images/audia3/{}_{}.jpg'.format(name, res['items'].index(item)))

    print ('\nQuery: {}'.format(query))
    #print ('\nQuery: {}'.format(res['queries']['request'][0]['searchTerms']))

if __name__ == '__main__':
    main()
