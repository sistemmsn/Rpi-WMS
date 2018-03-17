import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from time import sleep

cred = credentials.Certificate('FirebaseServiceKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://rpi-wms.firebaseio.com'
})

root = db.reference()

while True:
      try:
            hum, temp = Adafruit_DHT.read_retry(11, 27)
            sensor = BMP085.BMP085()
            prsr=sensor.read_pressure()
            root.child('data').update({
                  'temperature': str(temp),
                  'humidity': str(hum),
                  'pressure': str(prsr) 
            })
      except:
            print("Error reading values")
      sleep(5)


