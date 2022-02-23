#C:\Users\ASUS\Desktop\Omdena_Scraping\env

import scrapy
from urllib.parse import  urlencode
import json
from scrapy.crawler import CrawlerProcess
import csv


class RedditspiderSpider(scrapy.Spider):
    name = 'redditSpider'
    baseURL="https://gateway.reddit.com/desktopapi/v1/subreddits/Roadcam?"
    params={'rtj': 'only',
            'redditWebClient': 'web2x',
            'app': 'web2x-client-production',
            'allow_over18': '',
            'include': 'prefsSubreddit',
            'after': 't3_rvimfv',
            'dist': '8',
            'forceGeopopular': 'false',
            'layout': 'card',
            'sort': 'hot'}
    recursive_calls=120

    def start_requests(self):
        url=self.baseURL + urlencode(self.params)

        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        jsonData=json.loads(response.text)


        postKeys=[x for x in list(jsonData['posts'].keys()) if len(x)<13]
        try:
            links=[jsonData['posts'][i]['source']['url'] for i in postKeys]
        except:
            links=[]

        with open('reddit_roadcam.txt', 'a') as f:
            for i in links:
                f.write(i+'\n')


        self.params['after']=jsonData['token']
        self.params['dist']=jsonData['dist']

        url = self.baseURL + urlencode(self.params)

        if self.recursive_calls>0:
            self.recursive_calls-=1
            yield scrapy.Request(url, callback=self.parse)


        pass




process=CrawlerProcess()
process.crawl(RedditspiderSpider)
process.start()
