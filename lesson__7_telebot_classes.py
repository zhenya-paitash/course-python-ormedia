from tokenbot_req import token
from time import sleep
from bs4 import BeautifulSoup
import requests

# ------------------------------- переменные --------------------------------------------------
URL = "https://api.telegram.org/bot" + token + "/"
global last_update_id
last_update_id = 0


# ------------------------------- main() ------------------------------------------------------
class Main():
    def main(self):
        """ тело цикла. Главный блок """
        while True:
            last = Message().get_message()  # *** message{'id':id, 'text':text} ***
            if last != None:
                id, text = last['chat_id'], last['text']  # чат айди/текс для сообщения
                Bot().function_select(id, text)
                sleep(2)
            else:
                continue


# ------------------------------- class Bot ---------------------------------------------------
class Bot():
    """ обробатывает запрос пользователя """

    def __init__(self):
        pass

    def function_select(self, id, text):
        if text == '/help':
            Message().send_message(id, '/help - помощь\n/valut - курс валют\n/valutdate - курс на момент указанной '
                                       'даты\n/anekdot - травлю не хуже Петросяна\n/afisha - фильмы в прокате\n'
                                       '/pogoda - погода в минске\n/lostfilm - последние новости сериалов\n'
                                       '/cosmos - последние новости космоса')
        if text == '/anekdot':
            Work().anekdot(id)
        if text == '/afisha':
            Work().afisha(id)
        if text == '/valut':
            Message().send_message(id, '/aud  -  австралийский доллар\n/bgn  -  болгарский лев\n/uah  -  гривня\n'
                                       '/dkk  -  датские кроны\n/usd  -  доллар сша\n/eur  -  евро\n/pln  -  злоты\n'
                                       '/irr  -  иранские риалы\n/isk  -  исландские кроны\n/jpy  -  йен\n'
                                       '/cad  -  канадский доллар\n/cny  -  китайский юань\n/kwd  -  кувейтский динар\n'
                                       '/mdl  -  молдавский леев\n/nzd  -  новозеландский доллар\n/nok  -  норвежский крон'
                                       '\n/rub  -  российский рубль\n/xdr  -  сдр (специальные права заимствования)\n'
                                       '/sgd  -  сингапурcкий доллар\n/kgs  -  сом\n/kzt  -  тенге\n/try  -  турецкий лир'
                                       '\n/gbp  -  фунт стерлингов')
        if text[1:4].upper() in Work().code_id and len(text) == 4:
            Work().money(id, text)
        if text == '/valutdate':
            Message().send_message(id, 'Укажите дату формата: /валюта_год-месяц-день,\nнапример: "/usd_2016-5-21". '
                                       'Если дата указана неверно,\nвозвращает курс на текущий момент.')
        if (text.split('_')[0])[1:4].upper() in Work().code_id and len(text) >= 13:
            Work().money_on_date(id, text)
        if text == '/pogoda':
            Work().pogoda(id)
        if text == '/lostfilm':
            Work().lostfilm(id)
        if text == '/cosmos':
            Work().cosmos(id)


# ------------------------------- class Message -----------------------------------------------
class Message():
    """ обрабатывает ввод и вывод запросов пользователя"""

    def __init__(self):
        pass

    def get_updates(self):
        url = URL + 'getupdates'
        r = requests.get(url)
        return r.json()

    def get_message(self):
        data = self.get_updates()
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

    def send_message(self, chat_id, text='Wait,please...'):
        url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
        requests.get(url)


# ------------------------------- class Work --------------------------------------------------
class Work():
    """ выполняет требуемый запрос """

    def __init__(self):
        self.code_id = {'AUD': 170, 'BGN': 191, 'UAH': 290, 'DKK': 291, 'USD': 145, 'EUR': 292, 'PLN': 293, 'IRR': 303,
                        'ISK': 294, 'JPY': 295, 'CAD': 23, 'CNY': 304, 'KWD': 72, 'MDL': 296, 'NZD': 286, 'NOK': 297,
                        'RUB': 298, 'XDR': 299, 'SGD': 119, 'KGS': 300, 'KZT': 301, 'TRY': 302, 'GBP': 143, 'CZK': 305,
                        'SEK': 306, 'CHF': 130}

    def anekdot(self, id):
        url = "https://nekdo.ru/random/"
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        anek = soup.find('div', class_="text").text
        Message().send_message(id, anek)

    def afisha(self, id):
        url = 'https://afisha.tut.by/movie-premiere/?utm_source=afisha.tut.by&utm_medium=films&utm_campaign=premiere_block'
        txt = requests.get(url).text
        soup = BeautifulSoup(txt, 'lxml')
        film = soup.find('div', class_="events-block js-cut_wrapper").find('ul',
                                                                           class_="b-lists list_afisha col-5").text.split()
        afisha = ''
        for i in film:
            if i == '11':
                afisha += '\n'
            afisha = afisha + ' ' + i
        Message().send_message(id, afisha)

    def money(self, id, text):
        code_id = self.code_id
        abb = code_id[text[1:4].upper()]
        url = "http://www.nbrb.by/API/ExRates/Rates/" + str(abb)
        html = requests.get(url).json()
        money = "Сегодня 1 {} стоит {} BYN".format(str(html["Cur_Abbreviation"]), str(html['Cur_OfficialRate']))
        Message().send_message(id, money)

    def money_on_date(self, id, text):
        try:
            code_id = self.code_id
            abb = code_id[(text.split('_')[0])[1:4].upper()]  # /usd
            date = text.split('_')[1]  # 2016-5-5
            url = "http://www.nbrb.by/API/ExRates/Rates/" + str(abb) + "?onDate=" + str(date)
            html = requests.get(url).json()
            money_date = "{} числа 1 {} имел курс {} BYN".format(date, str(html["Cur_Abbreviation"]),
                                                                 str(html['Cur_OfficialRate']))
            Message().send_message(id, money_date)
        except:
            Message().send_message(id, 'даты нет в базе')

    def pogoda(self, id):
        url = 'https://yandex.by/pogoda/minsk'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        pogoda = soup.find('div', class_="fact__temp-wrap").find('span', class_="temp__value").text
        Message().send_message(id, pogoda)

    def lostfilm(self, id):
        url = 'https://www.lostfilm.tv/'
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        lostfilm = soup.find('div', class_="f-news--links").text
        Message().send_message(id, f"Новости сериалов с хостинга lostfilm.tv:\n{lostfilm}")

    def cosmos(self, id):
        url = 'https://hi-news.ru/tag/kosmos'
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        cosmos = soup.find('div', class_="items-wrap tag")
        for y in range(1):
            end = cosmos.find_all('h2')
            n = 0
            for i in end:
                x = i.text
                n += 1
                Message().send_message(id, f"{n}. {x}")
        Message().send_message(id, "Эти и другие новости ищите тут\nhttps://hi-news.ru/tag/kosmos")


# ------------------------------- запуск цикла ------------------------------------------------
if __name__ == "__main__":
    Main().main()
