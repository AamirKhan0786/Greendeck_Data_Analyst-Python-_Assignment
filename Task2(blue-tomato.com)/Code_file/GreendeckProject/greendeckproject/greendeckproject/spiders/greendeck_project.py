import scrapy   #importing the scrapy framework

from ..items import GreendeckprojectItem   #importing the items.py file's class i.e Greendeckproject

class GreendeckProjectSpider(scrapy.Spider):  # This method usually parses the response, extracting the scraped data as dicts and also finding new URLs to follow and creating new requests from them.

    name = 'greendeck'  #It identifies the Spider. It must be unique within a project, i.e., we can’t set the same name for different Spiders.

    

    page_number= 2  #assigning the page number as 2 for pagination

    #A List of urls where the spider will begin to crawl from.
    start_urls = ['https://www.blue-tomato.com/de-AT/products/categories/Snowboard+Shop-00000000/gender/boys--girls--men--women/?page=1']

    def parse(self, response): # This method usually parses the response, extracting the scraped data as dicts and also finding new URLs to follow and creating new requests from them.

        items= GreendeckprojectItem()  # this is the instance of the class GreendeckprojectItem

        #field of items is defined in items.py file so that we can use here.

        product_name= response.xpath('//*[@class="productdesc"]//a/@data-productname').extract()
        product_brand= response.xpath('//*[@class="productdesc"]//a/@data-brand').extract()
        product_price= response.css('span.price').css('::text').extract()
        product_imageUrl = response.xpath('//*[@class="productimage"]//img/@src').getall()
        product_productUrl = response.xpath('//*[@class="productdesc"]//a/@href').extract()

        # Using our items
        items['product_name']= product_name
        items['product_brand'] = product_brand
        items['product_price'] = product_price
        items['product_imageUrl'] = product_imageUrl
        items['product_productUrl'] = product_productUrl

        yield items  #It's like return, except the function will return a generator.


        #We are using the pagination such that we can extract all the pages in the website
        #First we are opening the 2nd page as we have page_number=2
        next_page= 'https://www.blue-tomato.com/de-AT/products/categories/Snowboard+Shop-00000000/gender/boys--girls--men--women/?page='+ str(GreendeckProjectSpider.page_number)

        #We are making the condition here that untill and unless we are not reaching the end of the page
        #We will increase the page_number value by 1 and at the same time we are calling the parse function
        #to yield the items.
        if GreendeckProjectSpider.page_number < 36:
            GreendeckProjectSpider.page_number+= 1
            yield response.follow(next_page, callback= self.parse)