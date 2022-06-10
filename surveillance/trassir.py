from surveillance.models import VideoSrv
from valley.models import Valley
import requests
import json

# {'hls_player_version': 1, 'success': 1, 'token': 'QPZOMi0C'}
# {'hls_player_version': 1, 'success': 1, 'token': 'typNCCc2'}
# {'hls_player_version': 1, 'success': 1, 'token': 'is8W802Z'}

url = '192.168.1.100' #:1557/


def camera():
    cams = []
    cam_id = ['bw1VN7ee', 'K2078ygW', 'mXM7PSi0']

    url_sid = 'https://192.168.1.100:18082/login?username=Test&password=12345'
    jdata = requests.get(url_sid, verify=False)
    sid = json.loads(jdata.text)
    sid = sid['sid']

    for row in cam_id:
        url_token = 'https://192.168.1.100:18082/get_video?channel={}&container=mjpeg&quality=70&stream=sub&framerate=0&sid={}'.format(row, sid)
        jdata = requests.get(url_token, verify=False)
        token = json.loads(jdata.text)
        token = token['token']
        cams.append('http://192.168.1.100:1557/' + token)

    return cams

def videoUrl(vall1, vall2=0):
    if vall2 != 0:
        valleyLst = Valley.objects.all().in_bulk([vall1, vall2]).values()
    else:
        valleyLst = Valley.objects.all().in_bulk([vall1]).values()

    return valleyLst

for row in videoUrl(1, 2):
    print(row)