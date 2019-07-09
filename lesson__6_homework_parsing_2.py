# Задание: Получить список статей хабра за месяц ( https://habr.com/top/monthly/ )
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, "lxml")
    pages = soup.find('div', class_="page__footer").find('a',
        class_="toggle-menu__item-link toggle-menu__item-link_pagination toggle-menu__item-link_bordered").get('href')
    total_pages = pages.split('page')[1].split('/')[0]
    return total_pages  # возвращает кол-во страниц


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div', class_="posts_list").find_all('h2', class_="post__title")
    print(f"--------------------------------На этой странице {len(title)} статей--------------------------------\n")
    for ti in title:
        try:
            txt = ti.find('a', class_="post__title_link").text
            print(txt)
        except:
            print('')


def main():
    url = "https://habr.com/top/monthly/"  # неизменная часть на всех страницах
    dop_url = "page"  # url указывающий на страницу
    total_pages = get_total_pages(get_html(url))
    for i in range(1, int(total_pages) + 1):  # поиск по всем страницам
        url_gen = url + dop_url + str(i)
        print('\n', url_gen, '\n')
        html = get_html(url_gen)
        text = get_page_data(html)


if __name__ == "__main__":
    main()
