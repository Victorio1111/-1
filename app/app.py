from flask import Flask

app = Flask(__name__) # директива __name__ указывает на имя файла

if __name__ == '__main__':
    app.run(debug=True) # при debug = True сервер будет автоматически перезапускаться + обработка ошибок
  
# Обработчик
@app.rout("/")  
def index():
    return "index"
  
