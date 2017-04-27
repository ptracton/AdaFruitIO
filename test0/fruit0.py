#! /usr/bin/python3

import configparser
import datetime
import random
import time
from Adafruit_IO import Client

if __name__ == "__main__":
    config_file = "/home/pi/.ucla.cfg",
    config = configparser.RawConfigParser()
    config.read(config_file)
    ADAFRUIT_AIO_KEY = config.get("ADAFRUIT", "AIO_KEY")
    ADAFRUIT_USER = config.get("ADAFRUIT", "USER")
    
    # Create an instance of the REST client.
    aio = Client(ADAFRUIT_AIO_KEY)
    
    try:
        while True:
            value = random.randint(0, 100)
            now = datetime.datetime.now()
            now_string = now.strftime("%m-%d-%Y_%H-%M-%S")
            print("Data = {} {}".format(value, now_string))
            aio.send('Sensor0', value)
            time.sleep(10)
    except:
        print("All Done")
