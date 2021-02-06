# -*- coding: utf-8 -*-
import scrapy
from scrapyscraper.items import AmazonItem

class AmazonProductSpider(scrapy.Spider):
    name = "AmazonProducts"
    allowed_domains = ["amazon.com"]

    start_urls = [
        "https://www.amazon.com/dp/B003PMQMK2"
    ]

    def parse(self, response):
        items = AmazonItem()

        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        price = response.xpath('//span[contains(@class,"a-color-price") or contains(@id,"price_inside_buybox") or contains(@id,"priceblock_ourprice")]/text()').extract()

        items['product_name'] = ''.join(title).strip()
        items['product_price'] = ''.join(price).strip()

        yield items
