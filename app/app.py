from flask import Flask, render_template, request, jsonify 
import json
import os
import model as mod


app = Flask(__name__) # директива __name__ указывает на имя файла

# Обработчик, Декоратор
@app.route("/index")  
@app.route("/")  
def index():
    return render_template('index.html')

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
        'Company\xa0 (Maker-if known)': [company],
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
  

  
