import random
import time
from alerts import send_email_alert

def motion_sensor_check():
    while True:
        if random.choice([True, False]):
            send_email_alert("Motion detected near Lab Block!")
        time.sleep(10)