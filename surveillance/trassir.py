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

    def _videoDict(self):
        _vall = []
        _urls = []

        videoId1 = Valley.objects.get(id=self._val1).valley_videosrv_id
        _vall.append(VideoSrv.objects.get(id=videoId1))
        if self._val2 != 0:
            videoId2 = Valley.objects.get(id=self._val1).valley_videosrv_id
            _vall.append(VideoSrv.objects.get(id=videoId2))
        i = 1
        for row in _vall:
            _sidUrl = 'https://{}:{}/login?username={}&password={}'.format(row.videosrv_addr, row.videosrv_http,
                                                                           row.videosrv_user, row.videosrv_password)
            jdata = requests.get(_sidUrl, verify=False)
            sid = json.loads(jdata.text)
            sid = sid['sid']
            if i == 1:
                _tokenUrl = 'https://{}:{}/get_video?channel={}&container=mjpeg&quality=70&stream=sub&framerate=0&sid={}' \
                    .format(row.videosrv_addr, row.videosrv_http, Valley.objects.get(id=self._val1).valley_camera, sid)
            else:
                _tokenUrl = 'https://{}:{}/get_video?channel={}&container=mjpeg&quality=70&stream=sub&framerate=0&sid={}' \
                    .format(row.videosrv_addr, row.videosrv_http, Valley.objects.get(id=self._val2).valley_camera, sid)
            jdata = requests.get(_tokenUrl, verify=False)
            token = json.loads(jdata.text)
            token = token['token']
            _urls.append('http://{}:{}/{}'.format(row.videosrv_addr, row.videosrv_video, token))
            i += 1
        return _urls

    def _pumpUrl(self):
        sidUrl = 'https://192.168.1.100:18082/login?username=Test&password=12345'
        jdata = requests.get(sidUrl, verify=False)
        sid = json.loads(jdata.text)
        sid = sid['sid']
        url_token = \
            'https://192.168.1.100:18082/get_video?channel=bw1VN7ee&container=mjpeg&quality=70&stream=sub&framerate=0&sid=' + sid
        jdata = requests.get(url_token, verify=False)
        token = json.loads(jdata.text)
        token = token['token']
        return 'http://192.168.1.100:1557/' + token

    @property
    def valleyCam(self):
        return self._videoDict()

    @property
    def pumpCam(self):
        return self._pumpUrl()


# ttt1 = VideoUrl(1, 4)
# print(ttt1.valleyCam)
# print(ttt1.pumpCam)

class CamPTZ:
    pass
