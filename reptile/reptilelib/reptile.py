# -*- coding: utf-8 -*-
import threading  
import chardet
import httplib
import sys
#self
sys.path.append('../')
from parser.htmlparser import HtmlParser
from parser.urlparser import UrlParser
from datalist.urlist import List 
from datalist.urlqueue import Queue, UrlQueue

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
        self.continueRun = continueRun
        #---------------------
        self.urlparser = UrlParser(homeUrls)
        self.htmlparser = HtmlParser(self.urlparser)

    def conn(self):
        '''
        DNS缓存
        '''
        if self.__curSiteID[0] != self.__temSiteID:
            '''
            更新DNS
            '''
            self.__temSiteID = self.__curSiteID[0]
            netloc = self.transNetloc(self.__home_urls[self.__temSiteID])
            self.__conn = httplib.HTTPConnection(netloc, 80, timeout = 10)
        return self.__conn
            
    def requestSource(self, path):
        conn = self.__conn()
        conn.request("GET", path)
        r1 = conn.getresponse()
        data = r1.read()
        #需要对data的返回转台进行解析
        return data

    def getPage(self, path):
        return self.requestSource(path)

    def run(self):
        '''
        运行主程序 
        '''
        while(True):
            #外界控制是否继续运行
            if not self.continueRun[0]:
                return
            newPathInfo = self.urlQueue.get(timeout=80)
            #[title, path]
            source = self.getPage(newPathInfo[1])
            #判断是否为html源码
            if not self.htmlparser.init(source):
                '''
                图片或其他文件
                '''
                continue

    def addNewInQueue(self, pageStdUrl, urlist):
        '''
        直接从html source中提取出path列表
        直接添加到各自的inqueue
        '''
        for urlInfor in urlist:
            #[title, path]
            stdUrl = self.urlparser.transToStdUrl(pageStdUrl, urlInfor[1])
            siteId = self.urlparser.judgeUrl(pageStdUrl, urlInfor[1])
            path = self.urlparser.transPathByStd(stdUrl)
            #判断是否为本平台url
            if siteId != -1:
                if not self.urlist.find(path):
                    self.urlInQueue.put(siteId, urlInfor[1], path)

    def saveHtml(self):
        '''
        将html信息存储到数据库中
        '''
        






                
            


            

            





