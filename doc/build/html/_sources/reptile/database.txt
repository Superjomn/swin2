.. highlightlang:: python

数据库设计
============

*******************
Introduction
*******************

本系统外存信息均采用数据库存储，利用Sqlite单文件存储。我们在设计的时候，特别注意了整个系统的结构简洁性，这体现在数据库设计上，单文件及操作的高度抽象。

***********
数据库结构
***********
.. note::
    此部分采用Sqlite及Django的数据库层进行存储和操作。

site_info::
    
    id
    title
    url

html_info::

    id
    siteid      #标志不同的网站
    title

html_source::

    id
    source
    parsed_source

img_info::

    id
    docid
    siteid
    url

img_source::
    
    id
    source








