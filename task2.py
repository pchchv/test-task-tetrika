import requests
from bs4 import BeautifulSoup


def get_data():
    """Получить с русской википедии список всех животных (https://inlnk.ru/jElywR),
    вывести количество животных на каждую букву алфавита.
    Результат должен получиться в следующем виде:
    А: 642
    Б: 412
    В:....
    """
    animals = []
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    page = requests.get(url).text
    while True:
        soup = BeautifulSoup(page, 'lxml')
        links = soup.find('div', id='mw-pages').find_all('a')
        for animal in links:
            if animal.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + animal.get('href')
                page = requests.get(url).text
            elif animal.text != 'Предыдущая страница':
                animals.append(animal.text)
    return animals


a = get_data()
print(a)
