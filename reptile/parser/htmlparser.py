# -*- coding: utf-8 -*-
import chardet

class HtmlParser:
    def __init__(self):
        pass

    def init(self):
        pass

    def transcode(self, source):
        '''
        转码 自动转化为utf8
        '''
        res = chardet.detect(source)
        confidence = res['confidence']
        encoding = res['encoding']
        p = re.compile("&#(\S+);")
        source = p.sub("",source)
        print 'transcode', res
        if encoding == 'utf-8':
            return source
        if confidence < 0.6:
            return False
        else:
            return unicode(source, encoding, 'ignore')


