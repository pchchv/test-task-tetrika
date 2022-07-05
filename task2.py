import requests
from bs4 import BeautifulSoup


def get_data():
    letters = {}
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    page = requests.get(url).text
    while True:  # Получения списка животных
        soup = BeautifulSoup(page, 'lxml')
        links = soup.find('div', id='mw-pages').find_all('a')
        for animal in links:
            if animal.text == 'Следующая страница':  # Получение ссылки на следующую страницу
                url = 'https://ru.wikipedia.org/' + animal.get('href')
                page = requests.get(url).text
            elif animal.text != 'Предыдущая страница':
                first_letter = animal.text[0]  # Первая буква названия животного
                if first_letter == 'A':
                    return letters
                count = letters.setdefault(first_letter, 0)
                if count == 0:
                    letters[first_letter] = 1
                else:
                    letters[first_letter] = count + 1


def task():
    """Получить с русской википедии список всех животных (https://inlnk.ru/jElywR),
    вывести количество животных на каждую букву алфавита.
    Результат должен получиться в следующем виде:
    А: 642
    Б: 412
    В:....
    """
    letters = get_data()
    for animal, count in letters.items():
        print(animal + ':', count)


task()
