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

.. module:: reptile
.. class:: Reptile
    
    爬虫单线程

.. attribute:: __urlist
    
    内有一个List，判断是否重复,同时在CentreServ也设置一个中央List,负责总体上的path判断重复

.. attribute:: __urlQueue

    UrlQueue
    存储从CentreServ传下来的path任务

.. attribute:: __urlInQueue

    将从html source中解析到的path list。 对应存储到 **urlInQueue** 中对应的UrlQueue

.. note:: 此处将要将url转化为标准path ，先转化为绝对地址，然后拆分为path

.. attribute:: __curSiteID
    
    用于标志整个进程下载的站点的ID，可以由外界动态改变。 通过引用传入 **__temSiteID=[0]** 以在此进程下所有的线程保持一致。

.. attribute:: __temSiteID
    
    标志此爬虫线程爬取的站点的ID，与 **__curSiteID** 进行对比，用于在进程下载站点ID发生变化时，刷新conn.

.. attribute:: continueRun
    
    引用传入，用于在外界控制所有线程运行和终止。

.. method:: conn()
    
    TCP连接，存储DNS缓存。 通过__siteID和__curSiteID判断是否更新DNS和连接。

.. method:: requestSource(path)
    
    通过conn()取得source。 用于html和img及其他一切资源的底层方法。

.. method:: getPage(path)
    
    通过requestSource()取得html页面。

.. method:: addNewInQueue(pageStdUrl)

    将当前下载page中的path添加到__urlInQueue中相应的queue中。

.. method:: run()
    
    运行主程序，由continueRun控制线程是否退出。 当__urlQueue为空时，会由Queue的线程阻塞控制其推出，并引发Empty异常。
    

