import scrapy


class GanjiSpider(scrapy.Spider):
    name = "zufang"
    start_urls=['http://bj.ganji.com/fang1/chaoyang/']


    def parse(self,response):
        print(response)
        title_list=response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        money_list= response.xpath(".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        for i,j in zip(title_list,money_list):
            print(i,":",j)




