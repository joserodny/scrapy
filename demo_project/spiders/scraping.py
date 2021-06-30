import  scrapy
from ..items import DemoProjectItem

class Manilaairport(scrapy.Spider):
     name = 'flights'
     start_urls = ['https://mnlairport.ph/flights/arrivals']

     def parse(self, response):

          items = DemoProjectItem()

          flightInfo = response.xpath("//div[@class='primary-flight-details']")
         
          for info in flightInfo:   
               #flightTime
               flightTime           = info.css('div.flight-time strong').css('::text').extract()

               #details
               flightCode           = info.css('div.flight-details strong').css('::text').extract()
               flightOrigin        = info.css('div.flight-details p').css('::text').extract()
               flightAirlines      = info.css('div.flight-details').css('::text').extract()[1].replace('\n', '')

               #flightTerminal
               flightTerminal       = info.css('div.flight-status span.terminal').css('::text').extract()


               #flightTime    
               items['flightTime']      = flightTime

               #details
               items['flightCode']      = flightCode
               items['flightOrigin']    = flightOrigin
               items['flightAirlines']  = [flightAirlines]
               
               #flightTerminal
               items['flightTerminal']  = flightTerminal
              
               
               yield items
               

  
     

             
           