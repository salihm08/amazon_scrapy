# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random


class AmazonSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
    
    def process_request(self,request,spider):
        u_agent = random.choice(settings.get("USER_AGENT_LIST'))
        if u_agent:
            request.headers['User-Agent']=u_agent
        
