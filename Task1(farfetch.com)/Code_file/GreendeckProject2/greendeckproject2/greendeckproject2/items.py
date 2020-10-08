# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Greendeckproject2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # We are defining our items here
    product_name = scrapy.Field()
    product_brand = scrapy.Field()
    product_price = scrapy.Field()
    product_imageUrl = scrapy.Field()
    product_productUrl = scrapy.Field()
    pass
