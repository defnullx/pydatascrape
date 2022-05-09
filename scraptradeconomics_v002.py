from datetime import datetime
import scrapy
from scrapy.http import TextResponse
from scrapy.http import HtmlResponse

csvfile01 = "tbl01"
csvfile02 = "tbl02"
csvfile03 = "tbl03"


class scraptbl(scrapy.Spider):
    name = "scraptbl"
    start_urls = [
        'https://tradingeconomics.com/country-list/interest-rate?continent=world']

    def parse(self, response):
        tableheader = '//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//thead//tr//th'
        tablecountry = '//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//tr//td/a'
        tablevalues = '//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//tr'

        for sel in response.xpath(tableheader):
            dataheader = sel.xpath('normalize-space(.)').get()
            print("header: "+dataheader)

        for sel in response.xpath(tablecountry):
            datacountry = sel.xpath('normalize-space(.)').get()
            print("country: "+datacountry)

        for sel in response.xpath(tablevalues):
            #datavalues = sel.xpath('normalize-space(.)').get()
            data1 = sel.xpath('normalize-space(./td[2]/.)').get()
            data2 = sel.xpath('normalize-space(./td[3]/.)').get()
            data3 = sel.xpath('normalize-space(./td[4]/.)').get()
            
            objtostr = str(data3)
            print("data3: "+objtostr)
            data3totime = datetime.strptime(objtostr, '%b%y')

            #data3totime = pd.to_datetime(data3, format='%y-%m-%d', infer_datetime_format=True)
            
            #print("datetotime: "+data3totime)

            #datavalues = str(data1)+","+str(data2)+","+str(data3totime)
            

            #print("values: "+str(data1)+","+str(data2)+","+str(data3))
            #print("values: "+datavalues)

