# -*- coding: utf-8 -*-
import Queue as Q

#get() 超时时间
TIMEOUT = 3

class Queue(Q.Queue):
    '''
    url队列
    '''
    def __init__(self):
        '''
        存储格式:
            siteID
            home_url
            相对地址唯一标志一个url
        '''
        Q.Queue.__init__(self)
        self.siteID = -1
        
    def init(self, siteID):
        self.__siteID = siteID

    def getAll(self):
        '''
        返回所有信息
        [
            siteID,
            [
                ['title', 'url'],
                ['title', 'url'],
                ['title', 'url'],
            ]
        ]
        '''
        res = []
        urls = []
        res.append(self.siteID)
        res.append(urls)
        try:
            q = self.get_nowait()
            urls.append(q)
        except:
            pass
        return res

MAX = 100
class UrlQueue:
    def __init__(self, siteNum):
        self.siteNum = siteNum
        self.queue = []
        #统一记录每个Queue的长度
        self.qsize = []
        #扫描指针 从此Queue检测是否符合要求
        self.__index = 0
        
        for i in range(self.siteNum):
            q = Queue()
            q.init(i)
            self.queue.append(q)
    
    def getSize(self, siteID):
        return self.queue[siteID].qsize()

    def getAll(self):
        '''
        从queue中取出所有信息
        '''
        res = []
        for queue in self.queue:
            res.append(queue.getAll())
        return res
    
    def __get_right_siteID(self):
        '''
        取得有一定量url储备的站点id
        '''
        maxn = 0
        max_index = 0
        size = 0
        for i,q in enumerate(self.queue):
            size = q.qsize()
            if size > maxn:
                maxn = size
                max_index = i
        return (max_index, maxn)

    def put(self, siteID, title, path):
        self.queue[siteID].put([title, path])

    def get(self, siteID):
        '''
        如果数据池为空超过 3 s 
        则引发 Queue.empty 错误
        '''
        return self.queue[siteID].get(timeout = 2)
    
    def getUrlList(self, maxsize):
        '''
        从候选队列中选出一个最合适的队列 取出一定量的list
        '''
        qinfo = self.__get_right_siteID()
        idx = qinfo[0]
        size = qinfo[1]
        print 'find the right idx:',idx
        if size == 0:
            return False
        if size > maxsize:
            size = maxsize
        ulist = []
        print 'get size',size
        for i in range(size):
            ulist.append(self.get(idx))
        res = {}
        res['siteID'] = idx
        res['urls'] = ulist
        return res
    
    def show(self):
        print 'show queue'
        size = 0
        for q in self.queue:
            print '-'*50
            size = q.qsize()
            for i in range(size):
                u = q.get() 
                print u[0],u[1]




