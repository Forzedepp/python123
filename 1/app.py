import datetime
import random
import os
from flask import Flask

app = Flask(__name__)

cars_list = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cat_breeds = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_PATH = os.path.join(BASE_DIR, 'war_and_peace.txt')

def load_words_from_book():
    words = []
    try:
        with open(BOOK_PATH, 'r', encoding='utf-8') as f:
            text = f.read()
            tokens = text.split()
            for token in tokens:
                word = token.strip('.,!?;:()[]{}«»"\'—–-')
                if word:
                    words.append(word)
    except FileNotFoundError:
        pass
    return words

book_words = load_words_from_book()

visits_counter = 0

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/cars')
def cars():
    return ', '.join(cars_list)

@app.route('/cats')
def cats():
    return random.choice(cat_breeds)

@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Точное время: {current_time}'

@app.route('/get_time/future')
def get_time_future():
    future_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    return f'Точное время через час будет {future_time}'

@app.route('/get_random_word')
def get_random_word():
    if not book_words:
        return 'Слова из книги не загружены (проверьте наличие файла war_and_peace.txt)'
    return random.choice(book_words)

@app.route('/counter')
def counter():
    global visits_counter
    visits_counter += 1
    return str(visits_counter)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)

