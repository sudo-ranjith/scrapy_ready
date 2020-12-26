import scrapy


class RanjithSpider(scrapy.Spider):
    name = 'ranjith'
    allowed_domains = ['adoboloco.com']
    start_urls = ['https://adoboloco.com/hot-sauce/']

    def parse(self, response):
        all_data = response.xpath("//ul[@class='products columns-4']")
        urls = []
        for data in all_data:
            data = data.xpath("//h2[@class='woocommerce-loop-product__title']/a/@href").extract()

            if isinstance(data, list):
                for x in data:
                    product_url =  x
                    urls.append(product_url)
        for url in urls:   
            # time.sleep(3)
            yield scrapy.Request(url=url, callback=self.parse_page2, errback=self.check_code)

    def check_code(self, response):
        func_resp = {}
        print(f"inside new function")
        # func_resp['title1'] = response.xpath('//*[@id="cm_cr-product_info"]/div/div[2]/div/div/div[2]/div[1]/h1/a').extract()
        
        print(f"title is : {response.status}")
        yield func_resp

    def parse_page2(self, response):
        func_resp = {}
        print(f"inside new function")
        # func_resp['title1'] = response.xpath('//*[@id="cm_cr-product_info"]/div/div[2]/div/div/div[2]/div[1]/h1/a').extract()
        func_resp['title'] = response.xpath("//title/text()")
        print(f"title is : {func_resp['title']}")
        yield func_resp

print('crawler process completed......')

