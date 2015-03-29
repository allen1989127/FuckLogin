import os

class HelloTwitter:

    url = 'www.twitter.com'

    '''just ping twitter.com to say hi'''
    def hey(self) :
        res = os.system('ping -c3 ' + self.url)
        return res
