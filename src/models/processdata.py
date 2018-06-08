from flask import session
import geocoder
import requests
import socket

class LookUpSC(object):
    def __init__(self,t1):
        self.t1=t1

    @classmethod
    def LatLong(cls,t1):
        g = geocoder.google(t1)
        glat = g.latlng[0]
        glong=g.latlng[1]
        return (cls,glat,glong)

    @staticmethod
    def LocMissing():
        x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        x.connect(("www.google.com", 80))
        y = x.getsockname()[0]
        ipurl = ("http://freegeoip.net/json/?y")
        oo = requests.get(ipurl, None)
        jsonFormatted = oo.json()
        glat = jsonFormatted["latitude"]
        glong = jsonFormatted["longitude"]

        return (glat, glong)


