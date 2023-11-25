from typing import List

import scrapy


class QuotesSpider(scrapy.Spider):
    """
    This spider doesn't do much and is demonstrative purposes.
    """

    name = "checkip"  # Name of the spider. Must be unique across project

    def start_requests(self):
        """
        Must return an iterable of Iterable[scrapy.Request]
        """
        urls = ["http://checkip.dyndns.org/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ip: List = response.css("body::text").re(r"(\d+\.\d+\.\d+\.\d+)")
        print(ip[0])
