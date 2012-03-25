# -*- coding: utf-8 -*-
import urlparse

class UrlParser:
    '''
    对url的一系列操作
    '''
    def __init__(self, homeUrls):
        self.__homeUrls = homeUrls

    def transToStdUrl(self, homeurl, newurl):
        '''
        将任意一个url转化为绝对地址
        '''
        if newurl[:7] == 'http://':
            '''
            测试是否已经为绝对地址
            '''
            return newurl
        return urlparse.urljoin(homeurl, newurl)

    def transSiteID(self, url):
        '''
        返回url属于的siteID
        '''
        length = 0
        for i,u in enumerate(self.__homeUrls):
            length = len(u)
            if len(url) > length and url[:length] == u:
                return i
        return -1

    def transPath(self, pageStdUrl, url):
        '''
        将任意一个链接转化为 路径
        '''
        url = self.transToStdUrl(pageStdUrl, url)
        return urlparse.urlsplit(url).path

    def transNetloc(self, stdurl):
        return urlparse.urlsplit(url).netloc



        
        

        
        

        


    
