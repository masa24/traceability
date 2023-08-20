from flask import Flask, render_template, redirect, make_response, request
import sqlite3




app = Flask(__name__)

class database_handler:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

    def run_query(self,query:str):
        self.cursor.execute(query)
        self.connection.commit()

def create_database():
    print('start')
    db = database_handler("grape.db")
    query_info = """ CREATE table if not exists info (
        id INTEGER PRIMARY KEY,
        sweet TEXT NOT NULL,
        maker TEXT,
        type TEXT,
        location TEXT,
        planting TEXT,
        area TEXT,
        pot_num TEXT,
        date TEXT,
        weight TEXT,
        check_date TEXT
    )
    """
    query_maker = """ CREATE table if not exists maker (
            id INTEGER PRIMARY KEY,
            maker_id integer,
            maker TEXT,
            word TEXT,
            quote TEXT,
            product TEXT,
            image TEXT
        )
        """

    db.run_save(query_info)
    db.run_save(query_maker)
    db.close()

def get_info(id):
    print(id)
    db = database_handler("grape.db")
    data = db.search(f"Select * from info where id = {id}")
    print(data)
    data = data[0]
    #print(id, sweet, maker, type, location)
    return data

def get_maker(id):
    print(id)
    db = database_handler("grape.db")
    name = db.search(f"Select maker from info where id = '{id}'")

    name = str(name[0][0])
    print(name)
    if name == 'tanaka':
        print('match')

    data = db.search(f"Select * from maker where maker = '{name}'")
    print(data)
    data = data[0]
    print(f'final{data}')


    print(data)
    return data

@app.route('/')
def landing_check():  # Redirection to the login page
    response = make_response(redirect('/home/0'))
    return response

@app.route('/home/<int:id>')
def home(id):  # Redirection to the login page
    result = get_info(id)
    print(f"result: {result}")
    maker_info = get_maker(id)
    id = result[0]
    sweet = result[1]
    maker = result[2]
    type = result[3]
    location = result[4]
    date = result[8]
    weight = result[9]
    check_date = result[10]
    word = maker_info[3]
    quote = maker_info[4]
    product = maker_info[5]
    image = maker_info[6]

    result += maker_info
    print(result)

    return render_template('info.html', id = id,
                           sweet = sweet,
                           maker = maker,
                           type = type,
                           location = location,
                           date = date,
                           weight = weight,
                           check_date = check_date,
                           word = word,
                           quote = quote,
                           product = product,
                           image = image

    )

@app.route('/history/<int:id>')
def history(id):  # Redirection to the login page
    result = get_info(id)
    return render_template('history.html', id = result[0],
                           maker = result[2],
                           planting = result[5],
                           area = result[6],
                           pot_num = result[7])

@app.route('/pesticide/<int:id>')
def pesticide(id):  # Redirection to the login page
    print(id)
    db = database_handler("grape.db")
    data = db.search(f"Select * from info where id = {id}")
    print(data)
    data = data[0]

    id = data[0]
    sweet = data[1]
    maker = data[2]
    type = data[3]
    location = data[4]
    print(id, sweet, maker,type,location)
    return render_template('unuse/pesticide.html', id = id, sweet = sweet, maker = maker, type = type, location = location)

@app.route('/redirect')
def re():
    response = make_response(redirect('https://grape-base.co.jp/'))
    return response




create_database()
if __name__ == '__main__':
    app.run()
