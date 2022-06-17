import requests

pinShift = 30


def pin2Rele(addr, rele1, rele2):
    try:
        reqStr = requests.get('http://{}/{}'.format(addr, rele1), timeout=2).status_code
        if rele2 != 0:
            reqStr = requests.get('http://{}/{}'.format(addr, rele2), timeout=2).status_code
    except:
        reqStr = 'Fail'
    return reqStr


def pin1Rele(addr, rele, status):
    try:
        reqStr = requests.get('http://{}/{}/{}'.format(addr, rele, status), timeout=2).status_code
    except:
        reqStr = 'Fail'
    return reqStr


def pinInput(addr, pin):
    try:
        reqStr = requests.get('http://{}/{}'.format(addr, pin), timeout=2).text
    except:
        reqStr = 'Fail'
    return reqStr

