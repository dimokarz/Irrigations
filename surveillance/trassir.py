from surveillance.models import VideoSrv
from valley.models import Valley
import requests
import urllib3
from urllib.parse import urlparse
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

    def _ptz(self):
        ptz = []
        urls = self._valleyCam()
        sid = ''
        for row in urls:
            urlCan = urlparse(row).path[1:]
            urlHost = urlparse(row).hostname
            if urlCan == 1557:
                urlPort = 18082
            else:
                urlPort = 18083
            ptzPath = 'https://{}:{}/login?password=12345'.format(urlHost, urlPort)
            jData = requests.get(ptzPath, verify=False)
            sid = json.loads(jData.text)
            sid = sid['sid']
            # urlPort = urlparse(row).port
            ptzPath = 'https://{}:{}/ptz?command=open&channel={}&sid={}'.format(urlHost, urlPort, urlCan, sid)
            jData = requests.get(ptzPath, verify=False)
            ptzPath = 'https://{}:{}/ptz?command=turn&speed_x=XXX&speed_y=YYY&sid={}'.format(urlHost, urlPort, urlCan)
            ptz.append(ptzPath)
        return ptz

    @property
    def valleySub(self):
        return self._valleyCam()

    @property
    def pumpSub(self):
        return 'http://192.168.1.100:1557/bw1VN7ee?container=mjpeg&stream=sub'

    @property
    def ptz(self):
        return self._ptz()

# https://192.168.1.200:8080/ptz?command=open&channel=FByNlKIq&sid=fjMlBJ0I
# https://192.168.1.200:8080/ptz?command=turn&speed_x=1&speed_y=-1&sid=fjMlBJ0I