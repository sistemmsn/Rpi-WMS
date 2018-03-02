import Adafruit_DHT
from time import sleep
import Adafruit_BMP.BMP085 as BMP085
import requests

while True:
      try:
            hum, temp = Adafruit_DHT.read_retry(11, 14)#DHT_11->11 and 8th pin BCM14
            sensor = BMP085.BMP085()
            prsr=sensor.read_pressure()
            requests.post("http://api.thingspeak.com/update?api_key=[write api key]&field1="+str(temp)+"&field2="+str(hum)+"&field3=1"+str(prsr))
      except:
            print("Error reading values")
      sleep(10)
