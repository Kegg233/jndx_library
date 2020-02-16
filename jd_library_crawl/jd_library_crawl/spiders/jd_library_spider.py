# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
i = 400
# 214
# 985

class JdLibrarySpiderSpider(CrawlSpider):
    name = 'jd_library_spider'
    allowed_domains = ['202.195.144.118']
    start_urls = ['http://202.195.144.118:8080/opac/openlink.php?location=ALL&year=1700&doctype=ALL&lang_code=ALL&match_flag=forward&displaypg=1000&showmode=table&orderby=DESC&sort=CATA_DATE&onlylendable=no&count=1061809&with_ebook=on&page=700']

    rules = (
        Rule(LinkExtractor(allow=r'.+location=ALL&year=1700&doctype=ALL&lang_code=ALL&match_flag=forward&displaypg=1000&showmode=table&orderby=DESC&sort=CATA_DATE&onlylendable=no&count=1061809&with_ebook=on&page=\d'), callback="parse_item", follow=True),
        # Rule(LinkExtractor(allow=r".+opac/item\.php\?marc_no=."), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        global i
        url = re.findall(r"item\.php\?marc_no=.+list=1", response.text)
        with open('url2.txt', 'a', encoding='utf-8')as fp:
            fp.write("http://202.195.144.118:8080/opac/"+"\nhttp://202.195.144.118:8080/opac/".join(url)+"\n")
        i = i-1
        fp.close()
        print(str(i)+" 成功")
