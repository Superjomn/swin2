class Judger
==============
.. module:: judger

.. class:: Judger
.. data:: __homeUrls

.. method:: transToStdUrl(homeurl, newUrl)

    将任意一个url转化为绝对地址

.. method:: transSiteID(url)

    返回url属于的siteID

.. method:: transPath(pageStdUrl, url)
    
    将一个网页内的任意一个url转化为path，将会先转化为绝对url，然后转化为路径

    最终结果可以直接用于conn，request source。

.. method:: judgeUrl(pageUrl, newUrl)
    
    判断一个url是否在收录范围内
    如果在，则返回对应站点id
    

    

