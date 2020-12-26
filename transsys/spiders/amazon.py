import scrapy
import time


print('crawler process starting here!!!')
class AmazonSpider(scrapy.Spider):

    name = 'amazon'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.in/gp/bestsellers/electronics/1389432031/ref=zg_bs_unv_e_3_1805560031_1']
    temp_var = "https://www.amazon.in"


    def parse(self, response):
        all_data = response.xpath("//ol[@id='zg-ordered-list']")
        urls = []
        for data in all_data:
            data = data.xpath("//li[@role='gridcell']/span[@class='a-list-item']//a[@class='a-link-normal']/@href").extract()

            if isinstance(data, list):
                for x in data:
                    product_url = self.temp_var + x
                    urls.append(product_url)
        for url in urls:   
            # time.sleep(3)
            print(scrapy.Request(url=url, callback=self.parse_page2, errback=self.check_code))

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
