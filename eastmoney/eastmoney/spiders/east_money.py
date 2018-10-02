# -*- coding: utf-8 -*-
import scrapy
import json
from eastmoney.items  import EastmoneyItem
import requests
import re

class EastMoneySpider(scrapy.Spider):


    name = 'east_money'
    allowed_domains = ['www.eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2017-09-17&ed=2018-09-17&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1']
    # res = requests.get('http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2017-09-17&ed=2018-09-17&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1').text
    # allpage = re.search('allPages:(\d+)', res).group(1)
    # for page in range(int(allpage)):
    #     url  = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2017-09-17&ed=2018-09-17&qdii=&tabSubtype=,,,,,&pi=88&pn=50&dx='+str(page)
    #     start_urls.append(url)


    def parse(self, response):
        allpage = re.search('allPages:(\d+)', response.text).group(1)
        for page in range(int(allpage)):
            url  = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2017-09-17&ed=2018-09-17&qdii=&tabSubtype=,,,,,&pi='+str(page)+'&pn=50&dx=1'
            yield scrapy.Request(url=url, callback=self.parse_info , dont_filter=True)


    def parse_info(self, response):
        url = response.url
        page = re.search('http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2017-09-17&ed=2018-09-17&qdii=&tabSubtype=,,,,,&pi=(.*?)&pn=50&dx=1',url).group(1)
        newpage = re.sub('pageIndex::\d+','')
        html = response.text
        response = html.replace('var rankData = ', '').replace(",allRecords:4246,pageIndex:1,pageNum:50,allPages:85,allNum:4246,gpNum:802,hhNum:2233,zqNum:1015,zsNum:535,bbNum:54,qdiiNum:140,etfNum:0,lofNum:213,fofNum:14};",'}').replace('{datas', '{"datas"').split()
        for datas in response:

            data = json.loads(datas)
            print(data['datas'])
            for content in data['datas']:
                content = content.split(',')
                item = EastmoneyItem()
                item['基金代码'] = content[0]
                item['基金简称'] = content[1]
                item['日期'] = content[3]
                item['单位净值'] = content[4]
                item['累计净值'] = content[5]
                item['日增长率'] = content[6]
                item['近1周'] = content[7]
                item['近1月'] = content[8]
                item['近3月'] = content[9]
                item['近6月'] = content[10]
                item['近1年'] = content[11]
                item['近2年'] = content[12]
                item['近3年'] = content[13]
                item['今年来'] = content[14]
                item['成立来'] = content[15]
                item['手续费'] = content[-3]
                yield item
