# Задание: Получить курс нескольких валют за текущую дату
import requests


def main():
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
    txt = requests.get(url).json()
    for i in txt:
        while len(i['Cur_Name']) < 40:
            i['Cur_Name'] += '_'
        print(f"За {i['Date'].split('T')[0]} число, цена на 1 {i['Cur_Abbreviation']}",
              f"{i['Cur_Name']} составила {i['Cur_OfficialRate']} BYN белорусских рублей.")


if __name__ == '__main__':
    main()
