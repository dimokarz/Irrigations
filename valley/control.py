# class ControlBtn:
#
#     def __init__(self):
#         self._btn = [
#             {'rele': '7-9', 'eng': 'Start', 'rus': 'Старт'},{'rele': '8-9', 'eng': 'Stop', 'rus': 'Стоп'},
#             {'rele': '7-10', 'eng': 'Forward', 'rus': 'Вперёд'},{'rele': '8-10', 'eng': 'Revers', 'rus': 'Назад'},
#             {'rele': '7-11', 'eng': 'Water On', 'rus': 'Вода Вкл'},{'rele': '8-11', 'eng': 'Water Off', 'rus': 'Вода Выкл'},
#             {'rele': '7-12', 'eng': 'Sis On', 'rus': 'Автостоп Вкл'},{'rele': '8-12', 'eng': 'Sis Off', 'rus': 'Автостоп Выкл'}
#         ]
#
#     @property
#     def rusButtons(self):
#         _btnLang = []
#         for row in self._btn:
#             del row['eng']
#             row['title'] = row.pop('rus')
#             _btnLang.append(row)
#         return _btnLang
#
#     @property
#     def engButtons(self):
#         _btnLang = []
#         for row in self._btn:
#             del row['rus']
#             row['title'] = row.pop('eng')
#             _btnLang.append(row)
#         print(_btnLang)
#         return _btnLang


class ControlBtn:

    def __init__(self):
        self._btn = [
            {'rele': '7-9', 'eng': 'Start', 'rus': 'Старт'},{'rele': '8-9', 'eng': 'Stop', 'rus': 'Стоп'},
            {'rele': '7-10', 'eng': 'Forward', 'rus': 'Вперёд'},{'rele': '8-10', 'eng': 'Revers', 'rus': 'Назад'},
            {'rele': '7-11', 'eng': 'Water On', 'rus': 'Вода Вкл'},{'rele': '8-11', 'eng': 'Water Off', 'rus': 'Вода Выкл'},
            {'rele': '7-12', 'eng': 'Sis On', 'rus': 'Автостоп Вкл'},{'rele': '8-12', 'eng': 'Sis Off', 'rus': 'Автостоп Выкл'}
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


btn = ControlBtn().engButtons
for row in btn:
    print(row)


