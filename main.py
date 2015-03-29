#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from org.sz.hellotwitter import HelloTwitter
from org.sz.nmcontrol import NMControl
from org.sz.login import Login

import time

VPN_NAME = 'yunti'
NAME = '8432'
PASSWORD = '270059'
URL = 'http://192.168.0.216/auth/Sea/'
REF_ACTION = 'login.php'
ACTION = 'checkin.php'

if __name__ == '__main__':
    vpnc = NMControl(VPN_NAME)
    hellot = HelloTwitter()
    login = Login(NAME, PASSWORD, URL)

    while 1:
        #first need to checkout the network is ok? ping google is easiest
        res = hellot.hey()
        if res == 0:
            print ''
            print 'network is all right at', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print ''
            print ''
            print ''
            time.sleep(12)
            continue

        print 'network is down, let\'s start rebuild it'

        vpnc.down()

        while 1:
            if not login.login(ACTION, REF_ACTION):
                time.sleep(2)
                continue
            else:
                break

        print 'success to login'

        vpnc.up()
