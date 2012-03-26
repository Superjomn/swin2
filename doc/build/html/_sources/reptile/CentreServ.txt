CentreServ 中央控制服务器
============================
*******************
Introduction
*******************

中央控制服务器控制着每一个子平台的工作并接受每个平台的状态。 通过UserFace与用户实现交互。


*******************
TCP Message 消息格式
*******************
CentreServ和ClientServ中间通过TCP传递消息，消息为XML格式。

** CentreServ **

---------   --------------------------------------------
home_urls   CentreServ向ClientServ发送收录站点主地址
new_paths   CentreServ向ClientServ发送新的path任务
halt        中断并存储消息及信号
resume      从外存中恢复内存状态
status      询问ClientServ工作状态
---------   --------------------------------------------

in_paths    ClientServ向CentreServ发送爬取得到的新路径
status      ClientServ回答状态


主要格式::
    
    <signal kind='kind'>
       ... 
    </signal>

控制消息::
    
    <signal kind='kind'/>


home_urls::
    
    <signal kind='home_urls'>
        <home_urls>
            <url title='title' url='url' limit=-1/>
            <url title='title' url='url' limit=-1/>
            <url title='title' url='url' limit=-1/>
        </home_urls>
    </signal>

new_paths::
    
    <signal kind='new_paths'>
        <new_paths siteid=0>
            <path title='title' path='path'/>
            <path title='title' path='path'/>
            <path title='title' path='path'/>
        </new_paths>
    </signal>

in_paths::
    
    <signal kind='in_paths'>
        <in_paths siteid=0>
            <path title='title' path='path'/>
            <path title='title' path='path'/>
            <path title='title' path='path'/>
        </in_paths>
    </signal>
