import scrapy #importing the scrapy framework
from ..items import Greendeckproject2Item #importing the items.py classes i.e Greendeckproject2Item

class GreendeckProject2Spider(scrapy.Spider):  # This method usually parses the response, extracting the scraped data as dicts and also finding new URLs to follow and creating new requests from them.

    name = 'greendeck2' #It identifies the Spider. It must be unique within a project, i.e., we can’t set the same name for different Spiders.

    page_number= 2

    # A List of urls where the spider will begin to crawl from.
    start_urls = ['https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?page=1&view=180&scale=282']

    def parse(self, response):

        items= Greendeckproject2Item() # this is the instance of the class Greendeckproject2Item

        #field of items is defined in items.py file so that we can use here.
        product_name = response.css('p._d85b45').css('::text').extract() #text is availabe in <p class='_d85b45'> and extracting only text while inspecting
        product_brand = response.css('h3._346238::text').extract() #text is availabe in <h3 class='_346238'> and extracting only text while inspecting
        product_price = response.css('div._6356bb').css('::text').extract()  #text is availabe in <div class='_6356bb'> and extracting only text while inspecting
        product_imageUrl= response.css('meta::attr(content)').extract() #Url is available in <meta> and inspecting only 'content' attribute
        product_productUrl= response.css('a::attr(href)').extract()  #Url is availabe in <a> and extracting only 'href' attribute

        # Using our items
        items['product_name'] = product_name
        items['product_brand'] = product_brand
        items['product_price'] = product_price
        items['product_imageUrl'] = product_imageUrl
        items['product_productUrl'] = product_productUrl

        yield items #It's like return, except the function will return a generator.

        # This will redirect to next page
        next_page= 'https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?page='+str(GreendeckProject2Spider.page_number)+'&view=180&scale=282'

        # Check the condition till 87 pages and increase the page_nuber by 1
        if GreendeckProject2Spider.page_number < 88:
            GreendeckProject2Spider.page_number += 1
            yield response.follow(next_page, callback= self.parse) # yielding and calling parse function







