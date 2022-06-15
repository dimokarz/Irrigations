import requests

pinShift = 30


def pinRele(addr, rele1, rele2=0):
    try:
        rele1 = str(int(rele1 + pinShift))
        reqStr = requests.get('http://{}/{}'.format(addr, rele1), timeout=2).status_code
        if rele2 != 0:
            rele2 = str(int(rele2 + pinShift))
            reqStr = requests.get('http://{}/{}'.format(addr, rele2), timeout=2).status_code
    except:
        reqStr = 'Fail'
    return reqStr


def pinInput(addr, pin):
    try:
        reqStr = requests.get('http://{}/{}'.format(addr, pin), timeout=2).text
    except:
        reqStr = 'Fail'
    return reqStr