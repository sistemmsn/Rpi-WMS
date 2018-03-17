import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

from time import sleep
import requests
import python-firebase

while True:
      try:
            hum, temp = Adafruit_DHT.read_retry(11, 27)#DHT_11->11 and 27th GPIO pin
            sensor = BMP085.BMP085()
            prsr=sensor.read_pressure()
            requests.post("http://api.thingspeak.com/update?api_key=[write api key]&field1="+str(temp)+"&field2="+str(hum)+"&field3=1"+str(prsr))
      except:
            print("Error reading values")
      sleep(10)
