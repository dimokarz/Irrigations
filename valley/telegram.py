import requests


def telegram(system, message):
    apiToken = '5342668417:AAEJV4-s4bOHNQsPDQqb2ieDBps4CaG4VVU'
    chatId = '-1001412836934'
    requests.get(
        'https://api.telegram.org/bot{}/sendMessage'.format(apiToken), params=dict(
            chat_id=chatId,
            parse_mode='HTML',
            text='Ситема полива {}: {}'.format(system, message)
        ))