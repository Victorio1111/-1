from flask import Flask, render_template

app = Flask(__name__) # директива __name__ указывает на имя файла

# Обработчик, Декоратор
@app.route("/index")  
@app.route("/")  
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) # при debug = True сервер будет автоматически перезапускаться + обработка ошибок
  

  
