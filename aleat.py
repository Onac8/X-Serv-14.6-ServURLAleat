#!/usr/bin/python3

import socket
from webapp import webApp
import random

class aleat(webApp):

    def process(self, parsedRequest):
        num = random.randint(0,1000000000000)
        return ('200 OK', '<html><body><p><a href=' + str(num) + '>Dame otra!</a></p></body></html>')

if __name__ == "__main__": # __name__ programa principal
    servAleat = aleat(socket.gethostname(), 1234)
