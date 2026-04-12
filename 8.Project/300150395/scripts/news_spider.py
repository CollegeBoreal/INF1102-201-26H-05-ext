import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()

            yield {
                "title": text,
                "summary": author,
                "url": response.url,
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
