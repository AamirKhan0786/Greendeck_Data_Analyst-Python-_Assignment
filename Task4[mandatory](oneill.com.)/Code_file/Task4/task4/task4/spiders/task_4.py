import scrapy
from ..items import Task4Item
import pandas as pd
from scraper_api import ScraperAPIClient
client = ScraperAPIClient('83e6ebbac1a3ba50c7bcae5dbf215f28')

def read_csv():
    df= pd.read_csv("C:/Users/Amir/Desktop/Task4/Greendeck Business Analyst Assignment Task 4.csv")
    return df['Google Search Code'].values.tolist()

base_url= 'https://www.google.com/search?q={}'


class Task4Spider(scrapy.Spider):
    name = 'task'

    def start_requests(self):
        for google_search_code in read_csv():
            yield scrapy.Request(client.scrapyGet((base_url.format(google_search_code))), self.parse)

    def parse(self, response):
        #price = response.xpath('//*[@id="0A7280-4540-104"]/a/div[2]/span/span[2]/span/@content').get()
        #price.strip('price')
        yield{

            'price': response.xpath("//*[@class='sales']//span/@content").get(),
            'url':  response.xpath('//*[@id="rso"]/div[1]/div/div[1]/a/@href').get()
        }