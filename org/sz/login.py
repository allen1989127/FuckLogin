import urllib2

from urllib2 import URLError

class Login:

    def __init__(self, name, password, url):
        self.name = name
        self.password = password
        self.url = url

    def login(self, action, ref_action):
        headers = {
            r'User-Agent': r'Mozilla/5.0 (X11; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0',
            r'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            r'Accept-Language': r'en-US,en;q=0.5',
            r'Accept-Encoding': r'gzip, deflate',
            r'Referer': r'http://192.168.0.216/auth/Sea/' + ref_action,
            r'Content-Type': r'multipart/form-data; boundary=---------------------------409036126110349932270895253',
            }

        data = '-----------------------------409036126110349932270895253\r\nContent-Disposition: form-data; name="account_in"\r\n\r\n' + self.name + '\r\n-----------------------------409036126110349932270895253\r\nContent-Disposition: form-data; name="password_in"\r\n\r\n' + self.password + '\r\n-----------------------------409036126110349932270895253--\r\n'

        req = urllib2.Request(self.url + action, data, headers)
        try :
            response = urllib2.urlopen(req)
        except URLError, e:
            print e
            return False

        if response.getcode() != 200:
            return False

        success = False
        for line in response.readlines():
            if 'Sign in successfully!' in line:
                success = True
                break

        return success
