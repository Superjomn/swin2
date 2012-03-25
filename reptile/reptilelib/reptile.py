# -*- coding: utf-8 -*-
import threading  
import chardet
import httplib
#self
import htmlparser 



class Reptile(threading.Thread):
    '''
    单个线程
    '''
    def __init__(self, name, urlQueue, urlist, urlInQueue, Flock, homeUrls ,curSiteID = [0], continueRun = [True]):
        threading.Thread.__init__(self, name = name )  
        self.__homeUrls = homeUrls
        self.__urlist = urlist
        self.__urlQueue = urlQueue
        self.__urlInQueue = urlInQueue
        self.__Flock = Flock
        self.__curSiteID = curSiteID
        self.__temSiteID = -1
        self.__conn = None

    def conn(self):
        '''
        DNS缓存
        '''
        if self.__curSiteID[0] != self.__temSiteID:
            '''
            更新DNS
            '''
            self.__temSiteID = self.__curSiteID[0]
            

    def requestSource(self, path):
        conn = self.__conn()
        conn.request("GET", path)
        r1 = conn.getresponse()
        data = r1.read()
        #需要对data的返回转台进行解析
        return data



