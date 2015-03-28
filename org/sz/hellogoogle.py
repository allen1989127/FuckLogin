import os

class HelloGoogle :

    url = 'www.google.com'

    '''just ping google.com to say hi'''
    def hey(self) :
        res = os.system('ping -c3 ' + self.url)
        return res
