class Site:
    def __init__(self, name='index'):
        f = open(name + '.html', 'w')
        f.write('<!DOCTYPE html>')
        f.write('<html>')
        f.write('<head>')

        f.write('</head>')
        f.write('<body>')
        f.write('<h1>yeeted</h1>')
        f.write('</body>')
        f.write('</html>')

    def output(self):
        pass

    def addEl(self):
        pass

    # add closing tags?
    def close(self):
        pass

temp = Site()
