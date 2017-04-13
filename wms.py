import Adafruit_DHT
from time import sleep
import urllib2
#import Adafruit_BMP.BMP085 as BMP085

while True:
      hum, temp = Adafruit_DHT.read_retry(11, 14)#DHT_11->11 and 8th pin BCM14
      #sensor = BMP085.BMP085()
      #prsr=sensor.read_pressure()
      print("hum: "+str(hum)+"  temp: "+str(temp))#+"  prsr: "+str(prsr))
      try:
          url="http://api.thingspeak.com/update?api_key=[write api key]&field1="+str(temp)+"&field2="+str(hum)+"&field3=100"
          f=urllib2.urlopen(url)
          print(f.read())
          f.close()
      except:
            print("error uploading data")
            pass
      sleep(10)
 
