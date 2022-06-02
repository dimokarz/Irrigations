class ControlBtn:

    def __init__(self):
        self._btn = [
            {'rele': '7-9', 'eng': 'Start', 'rus': 'Старт', 'br': '0', 'class': 'btn_start btn-outline-success'},
            {'rele': '8-9', 'eng': 'Stop', 'rus': 'Стоп', 'br': '1', 'class': 'btn_stop btn-outline-danger'},
            {'rele': '7-10', 'eng': 'Forward', 'rus': 'Вперёд', 'br': '0', 'class': 'btn_start btn-outline-secondary'},
            {'rele': '8-10', 'eng': 'Revers', 'rus': 'Назад', 'br': '1', 'class': 'btn_start btn-outline-secondary'},
            {'rele': '7-11', 'eng': 'Water On', 'rus': 'Вода Вкл', 'br': '0', 'class': 'btn_start btn-outline-secondary'},
            {'rele': '8-11', 'eng': 'Water Off', 'rus': 'Вода Выкл', 'br': '1', 'class': 'btn_start btn-outline-secondary'},
            {'rele': '7-12', 'eng': 'Sis On', 'rus': 'Cтоп Вкл', 'br': '0', 'class': 'btn_start btn-outline-secondary'},
            {'rele': '8-12', 'eng': 'Sis Off', 'rus': 'Cтоп Выкл', 'br': '1', 'class': 'btn_start btn-outline-secondary'}
        ]

    def _selLng(self, selLng):
        if selLng == 'rus':
            delLng = 'eng'
        else:
            delLng = 'rus'
        _btnLang = []
        for row in self._btn:
            del row[delLng]
            row['title'] = row.pop(selLng)
            _btnLang.append(row)
        return _btnLang

    @property
    def rusButtons(self):
        return self._selLng('rus')

    @property
    def engButtons(self):
        return self._selLng('eng')


