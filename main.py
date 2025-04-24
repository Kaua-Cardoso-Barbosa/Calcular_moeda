from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/conversor_de_moedas', methods=['POST'])
def conversor():
    try:
        conversor = float(request.form['Converter'])
        dolar_atual = 5.69
        converter = float(dolar_atual/conversor)


        return render_template('index.html',converter=converter)
    except Exception as e:
        converter = f'Ocorreu um erro inesperado {e}'
        return render_template('index.html',converter=converter)


if __name__=='__main__' :
    app.run(debug=True)