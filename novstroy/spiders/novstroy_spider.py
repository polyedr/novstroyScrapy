#!/usr/bin/python
import scrapy
from scrapy_splash import SplashRequest

class AuthorSpider(scrapy.Spider):
    name = 'novstroy'

    start_urls = ['https://www.novostroy-m.ru/baza']


    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')


    def parse(self,response):
        for href in response.css('.description_box a::attr(href)'):
            yield response.follow(href,self.parse_house)

        """
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)
        """

    def parse_house(self,response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield{
            'title': extract_with_css('.card_title::text'),
             'region': extract_with_css('.info_item::text'),
             'prices': extract_with_css('.descrition_price_item::text'),


        }

 
