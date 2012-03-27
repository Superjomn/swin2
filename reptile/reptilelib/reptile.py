# -*- coding: utf-8 -*-
import threading  
import chardet
import httplib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#self
sys.path.append('../')
from sourceparser.htmlparser import HtmlParser
from sourceparser.urlparser import UrlParser
from datalist.urlist import List 
from datalist.urlqueue import Queue, UrlQueue
from datalayer.htmldb import HtmlDB
sys.path.append('../../')
from debug import *

class Reptile(threading.Thread):
    '''
    单个线程
    '''
    def __init__(self, name, urlQueue, urlist, urlInQueue, Flock, homeUrls ,curSiteID = [0], continueRun = [True]):
        threading.Thread.__init__(self, name = name )  
        #own data
        self.__homeUrls = homeUrls
        self.__urlist = urlist
        self.__urlQueue = urlQueue
        self.__urlInQueue = urlInQueue
        self.__Flock = Flock
        self.__curSiteID = curSiteID
        self.__temSiteID = -1
        self.__conn = None
        self.__homeurl = None
        self.continueRun = continueRun
        #---------------------
        self.urlparser = UrlParser(homeUrls)
        self.htmlparser = HtmlParser(self.urlparser)
        self.htmldb = HtmlDB(self.htmlparser)

    @dec
    def conn(self):
        '''
        DNS缓存
        '''
        if self.__curSiteID[0] != self.__temSiteID:
            '''
            更新DNS
            '''
            self.__temSiteID = self.__curSiteID[0]
            self.__homeurl = self.__homeUrls[self.__temSiteID]
            netloc = self.urlparser.transNetloc(self.__homeUrls[self.__temSiteID])
            print netloc
            self.__conn = httplib.HTTPConnection(netloc, 80, timeout = 10)
        return self.__conn
            
    @dec
    def requestSource(self, path):
        conn = self.conn()
        conn.request("GET", path)
        r1 = conn.getresponse()
        data = r1.read()
        #需要对data的返回转台进行解析
        return data

    @dec
    def getPage(self, path):
        return self.requestSource(path)

    @dec
    def run(self):
        '''
        运行主程序 
        '''
        self.conn()
        while(True):
            #外界控制是否继续运行
            if not self.continueRun[0]:
                return
            newPathInfo = self.__urlQueue.get(timeout=5)
            pageStdUrl = self.urlparser.transToStdUrl(self.__homeurl, newPathInfo[1])
            print 'start download: ',pageStdUrl
            #[title, path]
            source = self.getPage(newPathInfo[1])
            #判断是否为html源码
            if not self.htmlparser.init(source):
                '''
                图片或其他文件
                '''
                continue
            #解析和存储
            self.addNewInQueue(pageStdUrl)
            self.htmldb.saveHtml(newPathInfo[0], pageStdUrl, source)

    @dec
    def addNewInQueue(self, pageStdUrl):
        '''
        直接从html source中提取出path列表
        直接添加到各自的inqueue
        '''
        urlist = self.htmlparser.getLinks()
        for urlInfor in urlist:
            #[title, path]
            stdUrl = self.urlparser.transToStdUrl(pageStdUrl, urlInfor[1])
            siteId = self.urlparser.judgeUrl(pageStdUrl, urlInfor[1])
            path = self.urlparser.transPathByStd(stdUrl)
            #判断是否为本平台url
            if siteId != -1:
                if not self.__urlist.find(path):
                    self.__urlInQueue.put(siteId, urlInfor[1], path)


