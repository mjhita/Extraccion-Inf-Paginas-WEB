# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from  ExtraccionInfPaginasWEB.items import ItemOSL


class OslSpider(CrawlSpider):
    name = 'osl'
    allowed_domains = ['ugr.es']
    start_urls = ['http://osl.ugr.es/']

    rules = (
        #Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//*[starts-with(@id,"post-")]'), callback='parse_item'),
        #Rule('//*[starts-with(@id,"post-")]/section[1]/header/h2//a/@href', callback='parse_item',follow=True),

    )

    def parse_item(self, response):
        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        itemOSL = ItemOSL()
        itemOSL['titulo'] = response.xpath('//*[starts-with(@id,"post-")]/header/h1/text()').extract()
        itemOSL['autor'] = response.xpath('//*[starts-with(@id,"post-")]/header/div/span/span/a/text()').extract()
        itemOSL['contenido'] = response.xpath('//*[starts-with(@id,"post-")]/section/p/text()').extract()
        itemOSL['listaCategorias'] = response.xpath('//*[starts-with(@id,"post-")]/header/div/a[@class="btn btn-mini btn-tag"]/text()').extract()
        itemOSL['listaEtiquetas'] = response.xpath('//*[@id="post-8330"]/header/div/a[@class="btn btn-mini btn-tag"]/text()').extract()
           
        return itemOSL

