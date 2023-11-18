import json

import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList


class QuotesSpider(scrapy.Spider):
    """
    Creates a file quotes.json with quotes, authors and tags.
    """

    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse):
        """
        Sample target HTML:
            <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
                <span>by <small class="author" itemprop="author">Albert Einstein</small>
                <a href="/author/Albert-Einstein">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world">

                    <a class="tag" href="/tag/change/page/1/">change</a>

                    <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>

                    <a class="tag" href="/tag/thinking/page/1/">thinking</a>

                    <a class="tag" href="/tag/world/page/1/">world</a>

                </div>
            </div>
        """

        for div_quote in response.css("div.quote"):
            quote: list[str] = div_quote.css("span.text::text").getall()
            quote = [q.replace("\u201c", "").replace("\u201d", "") for q in quote]
            author: list[str] = div_quote.css("span small.author::text").getall()
            tags: list[str] = div_quote.css("div.tags a.tag::text").getall()
            yield {"quote": quote, "author": author, "tags": tags}
