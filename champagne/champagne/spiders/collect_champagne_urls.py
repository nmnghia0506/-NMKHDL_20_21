import scrapy

class collect_champagne_url(scrapy.Spider):
    name='champagne_urls' 
    DOWNLOAD_DELAY = 1

    custom_settings = {
        'DOWNLOAD_DELAY': 1 ,
        'ROBOTSTXT_OBEY' : True,
    }

    def __init__(self):
        self.offset = 1

    def start_requests(self):
        urls = ['https://winevn.com/ruou-vang/page/1']
        yield scrapy.Request(url=urls[0], callback=self.parse)



    def parse(self, response):
        urls = response.selector.xpath('//*[@id="main"]/ul/li/div/a[1]/@href').getall()
        for link in urls:
            yield {'champagne_url' : link}

        url_string = "https://winevn.com/ruou-vang/page/"
        self.offset += 1
        if self.offset <= 3:
            url_string = url_string + str(self.offset)
            yield scrapy.Request(url=url_string, callback=self.parse)
