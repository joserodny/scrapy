# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import mysql.connector
# useful for handling different item types with a single interface
import mysql.connector
class DemoProjectPipeline(object):
      def __init__(self):
          self.create_connection()

      def create_connection(self):
               #connect to database
          self.conn = mysql.connector.connect(
              host = 'localhost',
              user = 'root',
              password = 'onlyadmin',
              database = 'scraping'
          )
          self.cursor = self.conn.cursor()   

      def process_item(self, item, spider):
          self.store_db(item)
          return item


      def store_db(self, item):
                #query insert data
                self.cursor.execute("""INSERT INTO website_urls (flightAirlines, flightCode, flightOrigin, flightTerminal, flightTime) VALUES (%s, %s, %s, %s, %s)"""
                ,(
                       
                        #details
                        item['flightAirlines'][0],
                        item['flightCode'][0],
                        item['flightOrigin'][0],
                        #flightTerminal
                        item['flightTerminal'][0],
                         #flightTime    
                        item['flightTime'][0],
                ))
                self.conn.commit()
           
           
