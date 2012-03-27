# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('../')
from reptilelib.reptile import Reptile
from sourceparser.htmlparser import HtmlParser
from sourceparser.urlparser import UrlParser
from datalist.urlist import List 
from datalist.urlqueue import Queue, UrlQueue
sys.path.append('../../')
from debug import *


class debug_Reptile:
    def __init__(self):
        homeUrls = [
            'http://www.cau.edu.cn',
            'http://google.com.hk',
            'http://www.baidu.com',
        ]
        self.urlQueue = Queue()
        self.urlist = List()
        self.urlInQueue = UrlQueue(len(homeUrls))
        self.continueRun = [True]
        self.curSiteID = [0]

        self.reptile = Reptile(
            name = "reptile", 
            urlQueue = self.urlQueue,
            urlist = self.urlist,
            urlInQueue = self.urlInQueue,
            Flock = None,
            homeUrls = homeUrls,
            curSiteID = self.curSiteID,
            continueRun = self.continueRun
        )

    @dec
    def conn(self):
        print "conn"
        print self.reptile.conn()

    def requestSource(self):
        pass

    def getPage(self):
        data = self.reptile.getPage('')
        print 'data'
        print data

    @dec
    def run(self):
        url = ["中国农业大学", '']
        self.urlQueue.put(url)
        self.reptile.run()
        
        


if __name__ == '__main__':
    reptile = debug_Reptile()
    reptile.conn()
    #reptile.getPage()
    reptile.run()
