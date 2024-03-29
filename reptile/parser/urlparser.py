# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')
from debug import *
import urlparse

class UrlParser:
    '''
    对url的一系列操作
    '''
    def __init__(self, homeUrls):
        ''' ok '''
        self.__homeUrls = homeUrls

    def transToStdUrl(self, homeUrl, newUrl):
        ''' ok '''
        '''
        将任意一个url转化为绝对地址
        '''
        if newUrl[:7] == 'http://':
            '''
            测试是否已经为绝对地址
            '''
            return newUrl
        return urlparse.urljoin(homeUrl, newUrl)

    def transSiteID(self, stdUrl):
        ''' ok '''
        '''
        返回url属于的siteID
        '''
        length = 0
        for i,u in enumerate(self.__homeUrls):
            length = len(u)
            if len(stdUrl) > length and stdUrl[:length] == u:
                return i
        return -1

    def transPathByStd(self, stdUrl):
        ''' ok '''
        '''
        直接返回绝对地址的path
        '''
        return urlparse.urlsplit(stdUrl).path

    def transPath(self, pageStdUrl, url):
        ''' ok '''
        '''
        将任意一个链接转化为 路径
        '''
        url = self.transToStdUrl(pageStdUrl, url)
        return urlparse.urlsplit(url).path

    def transNetloc(self, stdurl):
        ''' ok '''
        return urlparse.urlsplit(stdurl).netloc

    def judgeUrl(self, stdPageUrl, newUrl):
        ''' ok '''
        '''
        判断一个url是否在收录范围内
        如果在，则返回对应站点id
        '''
        url = self.transToStdUrl(stdPageUrl, newUrl)
        return self.transSiteID(url)







        
        

        
        

        


    
