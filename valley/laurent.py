import requests


# http://192.168.1.44/cmd.cgi?cmd=REL,1,1

def lauRele(addr, rele, status):
    addr = addr + '/cmd.cgi?cmd=REL,'
    try:
        reqStr = requests.get('http://{}{},{}'.format(addr, rele, status), timeout=2).status_code
    except:
        reqStr = 'Fail'
    return reqStr

# lauRele('192.168.1.44', 1, 0)
# http://192.168.1.107/cmd.cgi?psw=Laurent&cmd=REL,1,1

# lauRele('192.168.1.107', '1', '0')