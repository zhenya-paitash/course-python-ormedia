import requests


def get_text(url):
    r = requests.get(url)
    return r.json()


def main():
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
    result = get_text(url)  # равносильно записи <=>  result = requests.get(url).json() без доп.функции
    for i in result:
        while len(i['Cur_Name']) < 40:
            i['Cur_Name'] += '_'
        print(f"За {i['Date'].split('T')[0]} число, цена на 1 {i['Cur_Abbreviation']}",
              f"{i['Cur_Name']} составила {i['Cur_OfficialRate']} BYN белорусских рублей.")


if __name__ == '__main__':
    main()
