from __future__ import print_function
from slackclient import SlackClient
import time
import requests
import datetime


class Bot(object):

    def __init__(self, token):
        self.client = SlackClient(token)
        self.username = {}
        self.user_id = {}

    def run(self):
        if self.client.rtm_connect():
            try:
                self.user_id = self.client.api_call("auth.test")['user_id']
                self.username = self.client.api_call("auth.test")['user']
            except Exception as e:
                pass
            while True:
                now = datetime.datetime.now()
                if all((now.hour >= 9, now.hour <= 17,  now.weekday() <= 4)):
                    self.post_inspiration()
                time.sleep(3600)
        else:
            print("Connection failed.")

    def post_inspiration(self):
        """
        Use the inspirobot api to generate a new image
        and post it to the inspiration channel
        """
        r = requests.get('http://inspirobot.me/api?generate=true')
        url = r.text
        self.client.api_call("chat.postMessage",
                             as_user="true",
                             channel="inspiration",
                             text=url)
            
 
