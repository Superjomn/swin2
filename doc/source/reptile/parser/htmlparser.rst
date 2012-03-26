Class HtmlParser
=================
对html做相关的解析及修改操作。

.. module:: htmlparser
    :synopsis: Html parse
.. moduleauthor:: Chunwei

.. versionadded:: 0.1

.. class:: HtmlParser
.. attribute:: d

    全局PyQuery对象

.. method:: init(source)
    
    更新d

.. method:: getLinks
    
    取得html源码中的链接，不做任何处理。

.. method:: getSrcs

    取的html源码中的图片地址src，不做如何处理。

.. method:: getTextNodes(tagname)
    
    取得任意节点的文本列表。 如[b1, b2, b3]

.. note::

    只是简单文本标签，对于A等不适用。

.. method:: transXML
    
    将html source解析成xml格式，进行存储

xml::

    <html>
        <h1>
            <node attr="attr"/>
            <node attr="attr"/>
        </h1>
        <h2>
            <node attr="attr"/>
            <node attr="attr"/>
        </h2>
        <b>
            <node attr="attr"/>
            <node attr="attr"/>
        </b>
        <urls>
            <url title="title" href="url"/>
        </urls>
    </html>





