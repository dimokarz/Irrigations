from surveillance.models import VideoSrv
from valley.models import Valley
import requests
import urllib3
import json

urllib3.disable_warnings()


class VideoUrl:
    def __init__(self, val1, val2):
        self._val1 = val1
        self._val2 = val2

    def _valleyCam(self):
        urls = []
        urls.append(Valley.objects.get(id=self._val1).valley_camera)
        if self._val2 != 0:
            urls.append(Valley.objects.get(id=self._val2).valley_camera)
        return urls

    def _sids(self):
        pass

    @property
    def valleySub(self):
        return self._valleyCam()

    @property
    def pumpSub(self):
        return 'http://192.168.1.100:1557/bw1VN7ee?container=mjpeg&stream=sub'


class CamPTZ:
    pass
