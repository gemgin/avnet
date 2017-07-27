# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductItem
import re
import json
class ProSpider(scrapy.Spider):
    name = "pro"
    allowed_domains = ["www.avnet.com"]
    start_urls = (
        'https://products.avnet.com/shop/SearchDisplay?searchTerm=MAX764CSA+&storeId=10151',
    )

    def parse(self, response):
        item = ProductItem()
        item['search'] = response.xpath("//title").re("\w+")[1]
        item['urlhead'] = response.xpath("//input[@id='shopHomePageURL']/@value").extract_first()
        item['storeid'] = response.xpath("//input[@name='storeId']/@value").extract_first()
        url = 'https://www.avnet.com/search/resources/store/%s/productview/bySearchTerm/select?searchType=102&profileName=Avn_findProductsBySearchTermCatNav_Ajax&searchSource=Q&searchTerm=%s' % (item['storeid'], item['search'])
        yield scrapy.Request(url, self.parse_detail, meta={'item': item})
    def parse_detail(self, response):
        item = response.meta['item']
        s = json.loads(response.body)['catalogEntryView'][0] 
        item['furl'] = item['urlhead'] + "/" + s['avn_pdp_seo_path']
        yield item
