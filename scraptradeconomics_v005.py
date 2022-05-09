from IPython.display import display
from datetime import datetime
import pandas as pd
import scrapy
from yaml import serialize

csvfile01 = "tbl01"
csvfile02 = "tbl02"
csvfile03 = "tbl03"


class scraptbl(scrapy.Spider):
    name = "scraptbl"
    start_urls = [
        'https://tradingeconomics.com/country-list/interest-rate?continent=world']

    def parse(self, response):
        tableheader = '//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//thead//tr'
        tablevalues = '//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//tr'

        df = pd.DataFrame()

        for sel in response.xpath(tableheader):
            dataheader = sel.xpath('normalize-space(.)').get()
            dataheader = dataheader.replace(" Unit", "")
            #dataheader = dataheader.replace(" ",",")
            dataheader = str(dataheader)
            print("dataheader string: "+dataheader)
            dataheaderlist = list(dataheader.split(" "))
            print(dataheaderlist)
            df = pd.DataFrame(columns=dataheaderlist)
            display(df)

        for sel in response.xpath(tablevalues):
            datacountry = sel.xpath('normalize-space(./td/a/.)').get()
            last = sel.xpath('normalize-space(./td[2]/.)').get()
            previous = sel.xpath('normalize-space(./td[3]/.)').get()
            reference = sel.xpath(
                'normalize-space(./td[4]/.)').extract_first(default="default_value")

            reference = str(reference)
            if reference == "":
                continue

            referencedatetime = datetime.strptime(reference, "%b/%y")
            referencedate, referencetime = str(referencedatetime).split(" ")
            referencedate = datetime.strptime(referencedate, "%Y-%m-%d")
            date_time = referencedate.strftime("%m/%d/%Y")

            print(datacountry, last, previous, date_time)
            datalist = str(datacountry)+","+str(last)+"," + \
                str(previous)+","+str(date_time)
            datalist = list(datalist.split(","))
            dataseries = pd.Series(datalist, index=df.columns)
            print(dataseries)
            df = df.append(dataseries, ignore_index=True)

        display(df)
