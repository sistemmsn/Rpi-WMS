import Adafruit_DHT
from time import sleep
import urllib2
import Adafruit_BMP.BMP085 as BMP085

while True:
      try:
            hum, temp = Adafruit_DHT.read_retry(11, 14)#DHT_11->11 and 8th pin BCM14
            sensor = BMP085.BMP085()
            prsr=sensor.read_pressure()
            print("Humidity: "+str(hum)+"  Temperature: "+str(temp)+"  Pressure: "+str(prsr))
            try:
                url="http://api.thingspeak.com/update?api_key=[write api key]&field1="+str(temp)+"&field2="+str(hum)+"&field3=1"+str(prsr)
                f=urllib2.urlopen(url)
                print(f.read())
                f.close()
            except:
                  print("Error uploading data")
                  pass
            sleep(10)
      except:
            print("Error reading values")
            sleep(10)
 
