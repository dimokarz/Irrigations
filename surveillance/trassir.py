from surveillance.models import VideoSrv
from valley.models import Valley
import requests
import json

# {'hls_player_version': 1, 'success': 1, 'token': 'QPZOMi0C'}
# {'hls_player_version': 1, 'success': 1, 'token': 'typNCCc2'}
# {'hls_player_version': 1, 'success': 1, 'token': 'is8W802Z'}

# url = '192.168.1.100' #:1557/
#
#
# def camera():
#     cams = []
#     cam_id = ['bw1VN7ee', 'K2078ygW', 'mXM7PSi0']
#
#     url_sid = 'https://192.168.1.100:18082/login?username=Test&password=12345'
#     jdata = requests.get(url_sid, verify=False)
#     sid = json.loads(jdata.text)
#     sid = sid['sid']
#
#     for row in cam_id:
#         url_token = 'https://192.168.1.100:18082/get_video?channel={}&container=mjpeg&quality=70&stream=sub&framerate=0&sid={}'.format(row, sid)
#         jdata = requests.get(url_token, verify=False)
#         token = json.loads(jdata.text)
#         print(token)
#         token = token['token']
#         cams.append('http://192.168.1.100:1557/' + token)
#
#     return cams
#
#
# print(camera())

def videoUrl(cam1, cam2=0):
    pass