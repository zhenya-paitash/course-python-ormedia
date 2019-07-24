from tokenbot_req import token
from time import sleep
from bs4 import BeautifulSoup
import requests
import sys
import re

# пара переменных
URL = "https://api.telegram.org/bot" + token + "/"
global last_update_id
last_update_id = 0


def internet_connection():
    """ проверка на internet-соединение """
    while True:
        try:
            requests.get('https://www.google.com/')
            break
        except Exception:
            print(f"{sys.exc_info()[0]}\n{'~' * 50}Отсутствует интернет соединение!{'~' * 50}")
            sleep(10)
            continue


# ====================================================================================================================
# ↓--------------↓--------------↓--- main() ---↓---------------↓-----------------↓----------------↓--- *** *** *** ***
# ====================================================================================================================
class Main():
    """ главный цикл """

    def main(self):
        """ тело цикла """
        while True:
            last = Message().get_message()  # *** message{'id':id, 'text':text} ***
            if last != None:
                id, text = last['chat_id'], last['text']  # чат айди/текс для сообщения
                Bot().function_select(id, text)
                sleep(2)
            else:
                continue


# ====================================================================================================================
# ---↓-----------↓--------------↓--- class Message ---↓------------↓--------------↓---------------↓--- *** *** *** ***
# ====================================================================================================================
class Message():
    """ обрабатка ввода и вывода запросов """

    def get_updates(self):
        """ получение истории """
        url = URL + 'getupdates'
        r = requests.get(url)
        return r.json()

    def get_message(self):
        """ получение данных последнего сообщения пользователя """
        data = self.get_updates()
        # ↓---------------↓-------------↓--- проверка на ошибку URL ---↓--------------↓--------------↓
        try:
            data['result'][-1]
        except KeyError:
            sys.exit("ВНИМАНИЕ! Обнаружена ошибка: KeyError: 'result'\nВероятно ошибка адреса строки URL")
        # ↑---------------↑-------------↑--- проверка на ошибку URL ---↑-------------↑---------------↑
        last_object = data['result'][-1]
        current_update_id = last_object['update_id']
        global last_update_id
        if last_update_id != current_update_id:
            last_update_id = current_update_id
            chat_id = data['result'][-1]['message']['chat']['id']
            text = last_object['message']['text']
            message = {'chat_id': chat_id,
                       'text': text}
            return message
        return None

    def check_response(self, url):
        """ получение и обработка get() запроса с сервера """
        html = requests.get(url)
        if str(html) == '<Response [200]>':
            print('OK <Response [200]>')
        else:
            print(f'ERROR - {html}')
            id = Message().get_updates()['result'][-1]['message']['chat']['id']
            Message().send_message(id, f"ERROR {html}")  # если парсинг невозможент, отправить отчёт об ошибке
            Main().main()
        return html

    def send_message(self, chat_id, text='Wait,please...'):
        """ отправка результирующего сообщения пользователю """
        url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
        requests.get(url)


# ====================================================================================================================
# ---↓-----------↓--------------↓--- class Bot ---↓------------↓-------------------↓--------------↓--- *** *** *** ***
# ====================================================================================================================
class Bot():
    """ обробатка запроса пользователя """

    def function_select(self, id, text):
        """ обработка запроса и отправка данных на выполнение в класс Work """
        if text == '/help':
            Work().help(id)
        if text == '/anekdot':
            Work().anekdot(id)
        if text == '/afisha':
            Work().afisha(id)
        if text == '/valut':
            Work().valut(id)
        if text[1:4].upper() in Work().code_id and len(text) == 4:
            Work().money(id, text)
        if text == '/valutdate':
            Work().valutdate(id)
        if (text.split('_')[0])[1:4].upper() in Work().code_id and len(text) > 12:  # лучше через регулярки :)
            Work().money_on_date(id, text)
        if text == '/pogoda':
            Work().pogoda(id)
        if text == '/lostfilm':
            Work().lostfilm(id)
        if text == '/cosmos':
            Work().cosmos(id)
        if text == '/log':
            Work().loginfo(id)
        if 'что я писал' in text.lower():
            Work().log(id, text)
        if text == '/test':
            Work().test()
        if '/habr' in text:
            Work().habr(id, text)


# ====================================================================================================================
# ---↓----------↓---------------↓--- class Work ---↓-------------↓-----------------↓--------------↓--- *** *** *** ***
# ====================================================================================================================
class Work():
    """ выполнение запроса """

    def __init__(self):
        self.code_id = {'AUD': 170, 'BGN': 191, 'UAH': 290, 'DKK': 291, 'USD': 145, 'EUR': 292, 'PLN': 293, 'IRR': 303,
                        'ISK': 294, 'JPY': 295, 'CAD': 23, 'CNY': 304, 'KWD': 72, 'MDL': 296, 'NZD': 286, 'NOK': 297,
                        'RUB': 298, 'XDR': 299, 'SGD': 119, 'KGS': 300, 'KZT': 301, 'TRY': 302, 'GBP': 143, 'CZK': 305,
                        'SEK': 306, 'CHF': 130}

    def help(self, id):
        """ /help - помощь """
        Message().send_message(id, '/help - помощь\n/valut - курс валют\n/valutdate - курс на момент указанной '
                                   'даты\n/anekdot - травлю не хуже Петросяна\n/afisha - фильмы в прокате\n'
                                   '/pogoda - погода в минске\n/lostfilm - последние новости сериалов\n'
                                   '/cosmos - последние новости космоса\n/log - логи твоих сообщений\n'
                                   '/test - получение ошибки 404 :)\n/habr - последние статьи хабр')

    def valut(self, id):
        """ /valut - курс валют """
        Message().send_message(id, '/aud  -  австралийский доллар\n/bgn  -  болгарский лев\n/uah  -  гривня\n'
                                   '/dkk  -  датские кроны\n/usd  -  доллар сша\n/eur  -  евро\n/pln  -  злоты\n'
                                   '/irr  -  иранские риалы\n/isk  -  исландские кроны\n/jpy  -  йен\n'
                                   '/cad  -  канадский доллар\n/cny  -  китайский юань\n/kwd  -  кувейтский динар\n'
                                   '/mdl  -  молдавский леев\n/nzd  -  новозеландский доллар\n/nok  -  норвежский крон'
                                   '\n/rub  -  российский рубль\n/xdr  -  сдр (специальные права заимствования)\n'
                                   '/sgd  -  сингапурcкий доллар\n/kgs  -  сом\n/kzt  -  тенге\n/try  -  турецкий лир'
                                   '\n/gbp  -  фунт стерлингов')

    def valutdate(self, id):
        """ /valutdate - курс на момент указанной даты """
        Message().send_message(id, 'Укажите дату формата: /валюта_год-месяц-день,\nнапример: "/usd_2016-5-21". '
                                   'Если дата указана неверно,\nвозвращает курс на текущий момент.')

    def loginfo(self, id):
        """ /log - логи твоих сообщений """
        Message().send_message(id, 'Спроси меня, что ты писал Х сообщений назад.\n'
                                   'Нарпимер: "что я писал тебе 20 сообщений назад?" ')

    def anekdot(self, id):
        """ /anekdot - травлю анекдоты не хуже Петросяна """
        url = 'https://nekdo.ru/random/'
        try:
            html = Message().check_response(url).text
            soup = BeautifulSoup(html, 'lxml')
            anek = soup.find('div', class_="text").text
            Message().send_message(id, anek)
        except Exception:
            print(sys.exc_info())
            Message().send_message(id, "Что-то пошло не так...")

    def afisha(self, id):
        """ /afisha - фильмы в прокате """
        # ↓--------------↓--------------↓--- пример обработки если сайт лежит ---↓-----------------↓-----------↓
        try:
            url = 'https://afisha.tut.by/movie-premiere/?utm_source=afisha.tut.by&utm_medium=films&utm_campaign=premiere_block'
            txt = Message().check_response(url).text
            soup = BeautifulSoup(txt, 'lxml')
            film = soup.find('div', class_="events-block js-cut_wrapper").find('ul',
                                                                               class_="b-lists list_afisha col-5").text.split()
            afisha = ''
            for i in film:
                if i == '11':
                    afisha += '\n'
                afisha = afisha + ' ' + i
            Message().send_message(id, afisha)
        except:
            print(sys.exc_info())
            Message().send_message(id, "Ошибка. Что-то пошло не так...")
        # ↑--------------↑--------------↑--- пример обработки если сайт лежит ---↑--------------↑--------------↑

    def money(self, id, text):
        """ /valut - курс валют """
        code_id = self.code_id
        abb = code_id[text[1:4].upper()]
        url = "http://www.nbrb.by/API/ExRates/Rates/" + str(abb)
        html = Message().check_response(url).json()
        money = "Сегодня 1 {} стоит {} BYN".format(str(html["Cur_Abbreviation"]), str(html['Cur_OfficialRate']))
        Message().send_message(id, money)

    def money_on_date(self, id, text):
        """ /valutdate - курс на момент указанной даты """
        # ↓--------------↓--------------↓--- обработка неверного ввода ---↓-----------------↓-----------↓
        try:
            code_id = self.code_id
            abb = code_id[(text.split('_')[0])[1:4].upper()]  # /usd
            date = text.split('_')[1]  # 2016-5-5
            url = "http://www.nbrb.by/API/ExRates/Rates/" + str(abb) + "?onDate=" + str(date)
            html = Message().check_response(url).json()
            money_date = "{} числа 1 {} имел курс {} BYN".format(date, str(html["Cur_Abbreviation"]),
                                                                 str(html['Cur_OfficialRate']))
            Message().send_message(id, money_date)
        except IndexError:
            Message().send_message(id, 'проверте правильность ввода команды')
            print('Пользователь ввел команду неверно!')
        # ↑--------------↑--------------↑--- обработка неверного ввода ---↑--------------↑--------------↑

    def pogoda(self, id):
        """ /pogoda - погода в минске """
        url = 'https://yandex.by/pogoda/minsk'
        html = Message().check_response(url).text
        soup = BeautifulSoup(html, 'lxml')
        pogoda = soup.find('div', class_="fact__temp-wrap").find('span', class_="temp__value").text
        Message().send_message(id, pogoda)

    def lostfilm(self, id):
        """ /lostfilm - последние новости сериалов """
        url = 'https://www.lostfilm.tv/'
        soup = BeautifulSoup(Message().check_response(url).text, 'lxml')
        lostfilm = soup.find('div', class_="f-news--links").text
        Message().send_message(id, f"Новости сериалов с хостинга lostfilm.tv:\n{lostfilm}")

    def cosmos(self, id):
        """ /cosmos - последние новости космоса """
        url = 'https://hi-news.ru/tag/kosmos'
        soup = BeautifulSoup(Message().check_response(url).text, 'lxml')
        find = soup.find('div', class_="items-wrap tag").find('h2')
        cosmos = re.search(r'\"[a-zA-Z:/.=-]+\"', str(find)).group()
        Message().send_message(id, cosmos)

    def log(self, id, text):
        """ /log - логи твоих сообщений """
        try:
            date = re.search(r'\d+', text).group()
            x = int(date) * -1 - 1
            logs = Message().get_updates()
            last_object = logs['result'][x]['message']['text']
            Message().send_message(id, '{} сообщений назад ты писал(а):\n "{}"'.format(date, last_object))
        except Exception:
            print(sys.exc_info()[1])
            Message().send_message(id, 'Проверь запрос')

    def test(self):
        """ /test - получение ошибки 404 :) """
        url = 'https://www.lostfilm.tv/asafsafsaf'  # тест ошибки <Response [404]>
        Message().check_response(url)

    def habr(self, id, text):
        """ /habr - последние статьи хабр """
        try:
            quest = int(''.join(re.findall(r'\d', text)))
        except:
            quest = 1
        url = "https://habr.com/top/monthly/"  # неизменная часть на всех страницах  # https://habr.com/ru/top/monthly/
        html = Message().check_response(url).text
        soup = BeautifulSoup(html, 'lxml')
        title = soup.find('div', class_="posts_list").find_all('h2', class_="post__title")
        for i in range(quest):
            habr = ''.join(re.findall(r'https:[\/a-z.-9]+', str(title[i])))
            Message().send_message(id, habr)
        Message().send_message(id, 'Подсказка. Вы можете сразу указать\nn-ое кол-востатей формата /habr Х')


# ====================================================================================================================
# ---↓-------------↓------------↓--- запуск цикла ---↓--------------↓-----------------↓-----------↓--- *** *** *** ***
# ====================================================================================================================
if __name__ == "__main__":
    # проверка на internet-соединение
    internet_connection()
    # запуск main-цикла из класса Main
    Main().main()
