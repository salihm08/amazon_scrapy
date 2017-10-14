# -*- coding: utf-8 -*-
import scrapy

from amazon.items import AmazonItem
class Amazon1Spider(scrapy.Spider):
    name = 'amazon1'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/b?node=4510749031']

    def parse(self, response):
        LINK = "//a[@class='a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal']//@href"
        plink = response.xpath(LINK).extract()
        for link in plink :
        	yield scrapy.Request(url=link,callback=self.parse_product)
        NEXT ="//a[@class='pagnNext']//@href"
        next = response.xpath(NEXT).extract_first()
        next = 'https://www.amazon.in'+next if next else None
        if next is not None:
        	yield scrapy.Request(url=next,callback=self.parse)

    def parse_product(self,response):
    	PNME = "//span[@id='productTitle']/text()"
    	pnme = response.xpath(PNME).extract()
    	pnme = [a.strip() for a in pnme]
    	pnme = "".join(pnme)
    	DESCP = "//div[@id='feature-bullets']/ul/li/span/text()"
    	descp = response.xpath(DESCP).extract()
    	descp = [a.strip() for a in descp]
    	descp = "".join(descp)
    	PRICE = "//span[@id='priceblock_ourprice']/text()"
    	price = response.xpath(PRICE).extract()
    	price = [a.strip() for a in price]
    	price = "".join(price)
    	IMG = "//img[@id='landingImage']//@src"
    	img = response.xpath(IMG).extract()
    	img = [a.strip() for a in img]
    	img = "".join(img)
    	yield AmazonItem(pnme=pnme,descp=descp,price=price,img=img)