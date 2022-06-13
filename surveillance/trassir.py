from surveillance.models import VideoSrv
from valley.models import Valley
import requests
import json

# {'hls_player_version': 1, 'success': 1, 'token': 'QPZOMi0C'}
# {'hls_player_version': 1, 'success': 1, 'token': 'typNCCc2'}
# {'hls_player_version': 1, 'success': 1, 'token': 'is8W802Z'}

url = '192.168.1.100'  #:1557/


def camera():
    cams = []
    cam_id = ['bw1VN7ee', 'K2078ygW', 'mXM7PSi0']

    url_sid = 'https://192.168.1.100:18082/login?username=Test&password=12345'
    jdata = requests.get(url_sid, verify=False)
    sid = json.loads(jdata.text)
    sid = sid['sid']

    for row in cam_id:
        url_token = 'https://192.168.1.100:18082/get_video?channel={}&container=mjpeg&quality=70&stream=sub&framerate=0&sid={}'.format(
            row, sid)
        jdata = requests.get(url_token, verify=False)
        token = json.loads(jdata.text)
        token = token['token']
        cams.append('http://192.168.1.100:1557/' + token)

    return cams


class VideoUrl:
    def __init__(self, val1, val2=0):
        self._val1 = val1
        self._val2 = val2

    def _videoDict(self):
        _vall = []
        _urls = []
        _vall.append(VideoSrv.objects.get(id=self._val1))
        if self._val2 != 0:
            _vall.append(VideoSrv.objects.get(id=self._val2))

        for row in _vall:
            _sidUrl = 'https://{}:{}/login?username={}&password={}'.format(row.videosrv_addr, row.videosrv_http,
                                                                           row.videosrv_user, row.videosrv_password)
            jdata = requests.get(_sidUrl, verify=False)
            sid = json.loads(jdata.text)
            sid = sid['sid']
            _tokenUrl = 'https://{}:{}/get_video?channel={}&container=mjpeg&quality=70&stream=sub&framerate=0&sid={}'\
                .format(row.videosrv_addr, row.videosrv_http, Valley.objects.get(id=self._val1).valley_camera, sid)
            jdata = requests.get(_tokenUrl, verify=False)
            token = json.loads(jdata.text)
            token = token['token']
            _urls.append('http://{}:{}/{}'.format(row.videosrv_addr, row.videosrv_video, token))


        return _urls

    @property
    def valleyCam(self):
        return self._videoDict()

    @property
    def pumpCam(self):
        _cams = {0: [1, 'bw1VN7ee']}
        return _cams


ttt1 = VideoUrl(1)
print(ttt1.valleyCam)
