'''
Author: Daniel Frederick
Date: November 10, 2018
'''

from lxml import html
import requests

'''
print('\nGetting site code from ' + url + ' ... ')
self.page = requests.get(url)
self.tree = html.fromstring(self.page.content)
'''

class Analyze:
    def __init__(self, url):
        print('\nGetting site code from {}...'.format(url))
        self.page = requests.get(url)
        self.tree = html.fromstring(self.page.content)
        print(self.tree)

temp = Analyze('https://newsroom.ibm.com/announcements')
