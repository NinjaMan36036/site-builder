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
        f = open('output.html', 'w')
        for i in self.page:
            j = list(str(i))
            j.pop(0)
            j.pop(0)
            j.pop(len(j) - 1)
            msg = ''
            for k in j:
                msg += k
            f.write(msg)
        f.close()

    def read(self, fname):
        f = self.readFile(fname)

    # read file fname and return an array of str for each line
    def readFile(self, fname):
        f = open('{}.html'.format(fname), 'r')
        ans = []
        for i in range(0, self.countLines(fname)):
            ans.append(f.readline())
        f.close()
        print('Succesfully read file {}.'.format(fname))
        return ans

    # returns number of lines in a txt file fname
    def countLines(self, fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        f.close()
        return i + 1

temp = Analyze('https://newsroom.ibm.com/announcements')
