from flask import Flask, render_template, request

app = Flask(__name__)

saludo = "Bienvenido esto es una calculadora realizada con Flask  en python"

@app.route('/')
def index():
    return render_template('index.html', saludo=saludo)

@app.route('/calculadora' , methods=['GET', 'POST'])
def calculadora():
    instrucciones = "Calculadora simple"
    return render_template('calculadora.html', instrucciones=instrucciones)




if __name__ == '__main__':
    app.run(debug=True)



