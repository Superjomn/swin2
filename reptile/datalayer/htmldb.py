# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('../')
from datetime import date
#使用django的模型
from django.core.management import setup_environ
sys.path.append('../../../')
import swin.settings as settings
setup_environ(settings)
from swin.reptile.models import HtmlInfo, HtmlSource
sys.path.append('../../')
from debug import *

class HtmlDB:
    '''
    Html处理及存储层
    '''
    def __init__(self, htmlparser):
        #此处urlparser 和 htmlparser都已经在外界更新过
        self.htmlparser = htmlparser

    @dec
    def saveHtml(self, _title, stdUrl, _source):
        _source = self.htmlparser.transcode(_source)
        today = date.today()
        #_date = today.strftime("%y-%m-%d")
        #存储网页信息
        htmlinfo = HtmlInfo(title=_title, url=stdUrl, date=today)
        htmlinfo.save()
        xmltext = self.htmlparser.transXML(stdUrl)
        htmlsource = HtmlSource(source=_source, parsed_source=xmltext, info=htmlinfo)
        htmlsource.save()



        


