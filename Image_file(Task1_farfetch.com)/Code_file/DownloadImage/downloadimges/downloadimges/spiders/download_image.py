import scrapy
from PIL import Image

class DownloadImageSpider(scrapy.Spider):
    page_number=2 #initializing the page_number to 2
    name = 'downloadimage'
    #allowed_domains = ['d']
    start_urls = ['https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?page=1&view=180&scale=282']

    def parse(self, response):
        raw_image_urls= response.css('meta::attr(content)').getall() #it will give the raw link

        # we are keeping the link in list
        clean_image_url=[]
        for image_url in raw_image_urls:
            clean_image_url.append(response.urljoin((image_url)))


        yield{
                'image_urls': clean_image_url
        }

        #This will redirect to next page
        next_page = 'https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?page='+str(DownloadImageSpider.page_number)+'&view=180&scale=282'

        #Check the condition till 87 pages and increase the page_nuber by 1
        if DownloadImageSpider.page_number < 88:
            DownloadImageSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse) # yielding and calling parse function