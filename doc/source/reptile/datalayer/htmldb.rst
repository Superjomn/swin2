Class HtmlDB
==============
对Html处理及存储的数据抽象层。 采用了Django的models，便捷而快速地进行数据库的设计和开发。 

本系统希望能够充分利用Sqlite的功能，从而简化对离散数据的管理。

.. module:: htmldb
.. class:: HtmlDB
.. method:: saveHtml(title, stdUrl, source)

    存储html及其信息。 利用了两个表对htmlinfo和htmlsource进行存储。

****************
数据库设计
****************
数据库在reptile App的models定义。 通过django的模型对数据库操作进行了简化。

**HtmlInfo**

+-------+-------------+
| field | type        |
+=======+=============+
| title | CharField   |
+-------+-------------+
| url   | URLField    |
+-------+-------------+
| date  | DateField   |
+-------+-------------+

**HtmlSource**

+---------------+-------------+
| field         | type        |
+===============+=============+
| source        | TextField   |
+---------------+-------------+
| parsed_source | TextField   |
+---------------+-------------+
| info          | HtmlInfo    |
+---------------+-------------+


    


