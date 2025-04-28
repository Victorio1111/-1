from flask import Flask, render_template, request, jsonify 
import json
import os
import model as mod
import sqlite3


app = Flask(__name__) # директива __name__ указывает на имя файла

def get_db_connection(): # подключение к базе данных
    conn = sqlite3.connect('chocolate.db')  # имя файла базы
    conn.row_factory = sqlite3.Row        # чтобы получать строки в формате словаря
    return conn

# Обработчик, Декоратор
@app.route("/index")  
@app.route("/")  
def index():
    return render_template('index.html')


@app.route("/get_companies") 
def get_companies():
    
    conn = get_db_connection()  # Открываем соединение с базой db.sqlite3
    companies = conn.execute('SELECT id, name FROM companies').fetchall()  # Берем все компании
    conn.close()  # Закрываем соединение (очень важно закрывать соединение!)
    # companies — это список строк из базы данных. Мы превращаем каждую строку в словарь:
    companies_list = [{'id': row['id'], 'name': row['name']} for row in companies]
    
    return jsonify(companies_list)  # Возвращаем список как JSON-объект


# Маршрут для приема данных
@app.route("/submit", methods=['POST'])
def submit():
    # Считываем данные из формы
    cocoa_percent = request.form.get('cocoa_percent')
    company = request.form.get('company')
    bean_origin = request.form.get('bean_origin')
    company_location = request.form.get('company_location')
    bean_type = request.form.get('bean_type')
    broad_bean_origin = request.form.get('broad_bean_origin')
    
    # Собираем данные в json словарь
    user_input = {
        'Cocoa Percent': [float(cocoa_percent)],  # Преобразуем к float
        'Company (Maker-if known)': [company],
        'Specific Bean Origin or Bar Name': [bean_origin],
        'Company Location': [company_location],
        'Bean Type': [bean_type],
        'Broad Bean Origin': [broad_bean_origin]
    }
    
    # Сохраняем в файл (например, в папку проекта)
    with open('submission.json', 'w', encoding='utf-8') as f:
        json.dump(user_input, f, ensure_ascii=False, indent=4)
        
    # Делаем предсказание
    predicted_rating = mod.predict_chocolate_rating(user_input)
    
    # Возвращаем результат
    return jsonify({'predicted_rating': round(predicted_rating, 2)})


if __name__ == '__main__':
    app.run(debug=True) # при debug = True сервер будет автоматически перезапускаться + обработка ошибок
  

  
