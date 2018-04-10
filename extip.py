from i3pystatus import formatp
from i3pystatus import IntervalModule
import requests
import os
import time


class ExtIp(IntervalModule):
    settings = (
        ('format', 'formatp string'),
        ('color', 'The color of the text'),
        ('status', 'Dictionary mapping status to output'),
    )

    # default settings
    color = '#00ff00'
    interval = 1
    color_not_running = '#ff0000'
    not_running = 'ExtIP[X]'
    last = "X"
    lasttime = -1

    def get_info(self):
        if time.time() - self.lasttime > 10:
            self.extip = requests.get('http://ipinfo.io/ip').text.strip()
            self.lasttime = time.time()
            #extip = "1.2.3.4"
        return "ExtIP[" + self.extip + "]"

    def run(self):
        try:
            response = self.get_info()
            color = self.color
            if self.last != "X" and self.last != response:
                #os.system("notify-send 'External IP has changed'")
                color = self.color_not_running
            self.last = response
            self.output = {"full_text": response, "color": color}
        except:
            self.output = {
                "full_text": self.not_running,
                "color": self.color_not_running
            }
