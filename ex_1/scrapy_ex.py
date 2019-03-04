from scrapy import Spider

class Example(Spider):
    name = "Example"
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/"
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                "text" : quote.css('span.text::text').extract(),
                "author" : quote.css('small.author::text').extract(),
                "tags" : quote.css('div.tags a.tag::text').extract(),
            }

### Execute com o comando "scrapy runspider scrapy_ex.py -o data.json"
### Será gerado um arquivo contendo um json com os dados das páginas
