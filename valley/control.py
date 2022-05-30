class ControlBtn:
    btnLst = [
        {'rele': [2, 12], 'eng': '.', 'rus': '.'}, {'rele': [5, 12], 'eng': 'Esc', 'rus': 'Esc'},
        {'rele': [6, 9], 'eng': 'Percent', 'rus': 'Проценты'}, {'rele': [6, 10], 'eng': 'Depth', 'rus': 'Глубина'},
        {'rele': [6, 12], 'eng': 'Enter', 'rus': 'Enter'}, {'rele': [7, 9], 'eng': 'Start', 'rus': 'Старт'},
        {'rele': [8, 9], 'eng': 'Stop', 'rus': 'Стоп' }, {'rele': [7, 10], 'eng': 'Forward', 'rus': 'Вперёд'},
        {'rele': [8, 10], 'eng': 'Revers', 'rus': 'Назад'}, {'rele': [7, 11], 'eng': 'Water On', 'rus': 'Вода Вкл'},
        {'rele': [8, 11], 'eng': 'Water Off', 'rus': 'Вода Выкл'}, {'rele': [7, 12], 'eng': 'Sis On', 'rus': 'Автостоп Вкл'},
        {'rele': [8, 12], 'eng': 'Sis Off', 'rus': 'Автостоп Выкл'}
    ]

    lng = 'ru'

    def __init__(self, btnLst, lng):
        self.btnLst = btnLst
        self.lng = lng

    @property
    def btnLang(self):
        return self.btnLst
    @btnLang.setter
    def btnLst(self, btnLst):
        self.btnLst = btnLst

    def printBtn(self):
        print(self.btnLst)


btn = ControlBtn
# print(btn.btnLst)
# print(btn.lng)
print(btn.btnLang)

