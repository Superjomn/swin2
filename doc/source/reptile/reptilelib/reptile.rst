.. highlightlang:: python

ReptileLib 爬虫库设计
======================
*******************
Introduction
*******************

*******************
Class Reptile
*******************
.. note ::
    注意许多的不同之处
    大家很好的方式里面

.. class:: Reptile
    
    爬虫单线程

.. attribute:: __urlist
    
    内有一个List，判断是否重复,同时在CentreServ也设置一个中央List,负责总体上的path判断重复

.. attribute:: __urlqueue

    UrlQueue
    存储从CentreServ传下来的path任务

Reptile::
    
    class Reptile:
        def __init__(self):
            __urlist
            __urlqueue
            __urlQueue
            __urlInQueue
            __Flock
            __curSiteID
            __temSiteID

**__urlInQueue**
    
存储下载的path. 对应于不同的站点，urlInQueue专门有对应的urlQueue进行存储

**__urlQueue**

UrlQueue
存储从CentreServ传下来的path任务

**__urlist**

内有一个List，判断是否重复,同时在CentreServ也设置一个中央List,负责总体上的path判断重复

**__curSiteID** 和 **__temSiteID**

采用HTTPConnection的DNS缓存，用于过期缓存的刷新


UrlInQueue::

    class UrlInQueue:
        self.urlqueues = [UrlQueue, UrlQueue]




