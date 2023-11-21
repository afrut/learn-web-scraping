from pathlib import Path

import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList


class QuotesSpider(scrapy.Spider):
    """
    This spider doesn't do much and is demonstrative purposes.
    """

    name = "basics"  # Name of the spider. Must be unique across project

    def start_requests(self):
        """
        Must return an iterable of Iterable[scrapy.Request]
        """
        urls = ["https://quotes.toscrape.com/page/1/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse):
        """
        Function to be called on response of each request

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
        # Refer to the above HTML for the next selectors
        # Use a css selector to get all divs that have the class quote
        quotes: SelectorList = response.css("div.quote")

        # Get the text of small.author elements that are children of span
        # elements that are children of div.quote. .get() gets only the first element
        first_author = response.css("div.quote span small.author::text").get()

        # css selectors can also be chained. The previous selector can be
        # expressed as follows. This getall() retrieves all elements that match,
        # not just the first.
        authors = (
            response.css("div.quote")
            .css("span")
            .css("small.author")
            .css("::text")
            .getall()
        )

        # Get all tags. Get the text of an a.tag that is a child of div.tags.
        tags = quotes.css("div.tags a.tag::text").getall()

        # Another way to get tags. This method retrieves the value of the
        # content attribute of the meta element. Note that in this method, a
        # list of csv's containing the tags are returned.
        tags_csv = quotes.css("div.tags meta.keywords::attr(content)").getall()

        # Write content of response to file
        page = response.url.split("/")[-2]
        filename = f"outputs/quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

        # Follow next link
        next_page = response.css("nav ul.pager li.next a::attr(href)").get()
        if next_page:
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, callback=self.parse)

            # # Alternatively, use response.follow
            # yield response.follow(next_page, callback=self.parse)

        # # response.follow also takes a selector. No need for .get() or .getall()
        # for next_page in response.css("nav ul.pager li.next a::attr(href)"):
        #     yield respoinse.follow(next_page, callback=self.parse)

        # # For a elements, response.follow automatically uses its href attribute
        # for next_page in response.css("nav ul.pager li.next a"):
        #     yield respoinse.follow(next_page, callback=self.parse)

        # # Follow all from an Iterable
        # yield from response.follow_all(
        #     css="nav ul.pager li.next a", callback=self.parse
        # )

        # Log the header used by the request
        self.log(response.request.headers["User-Agent"].decode("utf-8"))
