import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from typing_extensions import override


class MySpider(CrawlSpider):
    """
    Functionally the same as quotes spider. Demonstrates usage of generic spider CrawlSpider
    """

    name = "crawlspider"
    allowed_domains = ["quotes.toscrape.com"]

    # Start from these links
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    rules = [
        Rule(
            # Then extract all links that match all regex in allow in all
            # elements in all html matching the css selectors in restrict_css
            LinkExtractor(
                allow=(r"/page/\d+/",),
                restrict_css=["nav ul.pager li.next a"],
            ),
            # For every such link, execute this callback
            callback="parse",
            # Follow links recursively
            follow=True,
        )
    ]

    # Override the parent's parse_start_url method to parse every element in start_urls
    @override
    def parse_start_url(self, response):
        yield from self.parse(response)

    def parse(self, response):
        for div_quote in response.css("div.quote"):
            quote = div_quote.css("span.text::text").getall()
            quote = [q.replace("\u201c", "").replace("\u201d", "") for q in quote]
            author = div_quote.css("span small.author::text").getall()
            tags = div_quote.css("div.tags a.tag::text").getall()
            yield {"quote": quote, "author": author, "tags": tags}
