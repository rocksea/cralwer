# -*- coding: utf-8 -*-
import scrapy
import json
import time
import re
from datetime import datetime, timedelta
from crawler.items import NaverKinItem

class NaverKinSpider(scrapy.Spider):
    name = "NaverKinCrawler"
    otaId = 1
    def start_requests(self):
        now = datetime.now()
	
        for page in range(1) :
           params = {'kin_start':(page*10)+1}
           url = "https://search.naver.com/search.naver?where=kin&kin_display=10&query=%EC%84%9C%EC%9A%B8%EB%8C%80&sm=tab_pge&kin_start={}".format(params['kin_start'])
           request = scrapy.Request(url, self.parse_data)
           request.meta['params'] = params
           yield request

    def parse_data(self, response):
        item = NaverKinItem()

        #print("#### Resp Body: \n %s" % response.body)

        title = response.xpath(r'//*[@id="elThumbnailResultArea"]/li[1]/dl/dt/a')[0].extract()
        title = re.sub(r'<.*?>','',title) #strip html
        print("#### title : %s" % title)

        content = response.xpath(r'//*[@id="elThumbnailResultArea"]/li[1]/dl/dd[2]')[0].extract()
        content = re.sub(r'<.*?>','',content) #strip html
        print("#### content : %s" % content)

        qDt = response.xpath(r'//*[@id="elThumbnailResultArea"]/li[1]/dl/dd[1]/text()')[0].extract()
        qDt = re.sub(r'([0-9]{4}.[0-9]{2}.[0-9]{2}).*',r'\1',qDt).replace('.','-') #Formatting DateType
        print("#### question Date : %s" % qDt)

        aContent = response.xpath(r'//*[@id="elThumbnailResultArea"]/li[1]/dl/dd[3]')[0].extract()
        aContent = re.sub(r'<.*?>','',aContent) #strip html
        print("#### answer : %s" % aContent)

        #Setting item
        item['qTitle'] = title
        item['qContent'] = content
        item['qDt'] = qDt
        item['aDt'] = ''

        time.sleep(5)

        yield item
