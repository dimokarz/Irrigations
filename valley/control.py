### Список кнопок для упрощенной панели
class ControlSimple:

    def __init__(self):
        self._btn = [
            {'rele': '7-9', 'eng': 'Start', 'rus': 'Старт', 'br': '0', 'class': 'btn-outline-success'},
            {'rele': '8-9', 'eng': 'Stop', 'rus': 'Стоп', 'br': '1', 'class': 'btn-outline-danger'},
            {'rele': '7-10', 'eng': 'Forward', 'rus': 'Вперёд', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '8-10', 'eng': 'Revers', 'rus': 'Назад', 'br': '1', 'class': 'btn-outline-secondary'},
            {'rele': '7-11', 'eng': 'Water On', 'rus': 'Вода Вкл', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '8-11', 'eng': 'Water Off', 'rus': 'Вода Выкл', 'br': '1', 'class': 'btn-outline-secondary'},
            {'rele': '7-12', 'eng': 'Sis On', 'rus': 'Cтоп Вкл', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '8-12', 'eng': 'Sis Off', 'rus': 'Cтоп Выкл', 'br': '1', 'class': 'btn-outline-secondary'}
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


### Список кнопок для полной панели
class ControlFull:

    def __init__(self):
        self.__btn1 = [
            {'rele': '1-9', 'eng': 'Prog', 'rus': 'Прог', 'br': '1', 'class': 'btn-outline-primary'},
            {'rele': '1-10', 'eng': 'Diag', 'rus': 'Диаг', 'br': '1', 'class': 'btn-outline-primary'},
            {'rele': '1-11', 'eng': 'Opt', 'rus': 'Настр', 'br': '1', 'class': 'btn-outline-primary'},
            {'rele': '1-12', 'eng': 'Syst', 'rus': 'Сист', 'br': '1', 'class': 'btn-outline-primary'},
        ]

        self.__btn2 = [
            {'rele': '2-9', 'eng': '1', 'rus': '1', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '3-9', 'eng': '2', 'rus': '2', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '4-9', 'eng': '3', 'rus': '3', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '5-9', 'eng': '⇧', 'rus': '⇧', 'br': '1', 'class': 'btn-outline-primary'},
            {'rele': '2-10', 'eng': '4', 'rus': '4', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '3-10', 'eng': '5', 'rus': '5', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '4-10', 'eng': '6', 'rus': '6', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '5-10', 'eng': '⇩', 'rus': '⇩', 'br': '1', 'class': 'btn-outline-primary'},
            {'rele': '2-11', 'eng': '7', 'rus': '7', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '3-11', 'eng': '8', 'rus': '8', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '4-11', 'eng': '9', 'rus': '9', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '5-11', 'eng': '-', 'rus': '-', 'br': '1', 'class': 'btn-outline-primary'},
            {'rele': '2-12', 'eng': '.', 'rus': '.', 'br': '0', 'class': 'btn-outline-primary'},
            {'rele': '3-12', 'eng': '0', 'rus': '0', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '4-12', 'eng': '⇐', 'rus': '⇐', 'br': '0', 'class': 'btn-outline-primary'},
            {'rele': '5-12', 'eng': 'Esc', 'rus': 'Esc', 'br': '0', 'class': 'btn-outline-danger'},
        ]

        self.__btn3 = [
            {'rele': '6-9', 'eng': 'Percent', 'rus': 'Проц', 'br': '0', 'class': 'btn-outline-primary'},
            {'rele': '6-10', 'eng': 'Depth', 'rus': 'Глуб', 'br': '0', 'class': 'btn-outline-primary'},
            {'rele': '', 'eng': '', 'rus': '', 'br': 'disabled', 'class': ''},
            {'rele': '6-12', 'eng': 'Enter', 'rus': 'Enter', 'br': '0', 'class': 'btn-outline-success'},
        ]

        self.__btn4 = [
            {'rele': '7-9', 'eng': 'Start', 'rus': 'Старт', 'br': '0', 'class': 'btn-outline-success'},
            {'rele': '8-9', 'eng': 'Stop', 'rus': 'Стоп', 'br': '1', 'class': 'btn-outline-danger'},
            {'rele': '7-10', 'eng': 'Forward', 'rus': 'Вперёд', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '8-10', 'eng': 'Revers', 'rus': 'Назад', 'br': '1', 'class': 'btn-outline-secondary'},
            {'rele': '7-11', 'eng': 'Water On', 'rus': 'Вода Вкл', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '8-11', 'eng': 'Water Off', 'rus': 'Вода Выкл', 'br': '1', 'class': 'btn-outline-secondary'},
            {'rele': '7-12', 'eng': 'Sis On', 'rus': 'Cтоп Вкл', 'br': '0', 'class': 'btn-outline-secondary'},
            {'rele': '8-12', 'eng': 'Sis Off', 'rus': 'Cтоп Выкл', 'br': '1', 'class': 'btn-outline-secondary'}
        ]

    def __selLng(self, col, selLng):
        if col == 1:
            currCol = self.__btn1
        elif col == 2:
            currCol = self.__btn2
        elif col == 3:
            currCol = self.__btn3
        elif col == 4:
            currCol = self.__btn4

        if selLng == 'rus':
            delLng = 'eng'
        else:
            delLng = 'rus'
        _btnLang = []
        for row in currCol:
            del row[delLng]
            row['title'] = row.pop(selLng)
            _btnLang.append(row)
        return _btnLang

    @property
    def rusButtons1(self):
        return self.__selLng(1, 'rus')

    @property
    def engButtons1(self):
        return self.__selLng(1, 'eng')

    @property
    def rusButtons2(self):
        return self.__selLng(2, 'rus')

    @property
    def engButtons2(self):
        return self.__selLng(2, 'eng')

    @property
    def rusButtons3(self):
        return self.__selLng(3, 'rus')

    @property
    def engButtons3(self):
        return self.__selLng(3, 'eng')

    @property
    def rusButtons4(self):
        return self.__selLng(4, 'rus')

    @property
    def engButtons4(self):
        return self.__selLng(4, 'eng')