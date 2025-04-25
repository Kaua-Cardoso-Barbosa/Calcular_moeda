from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/conversor_de_moedas', methods=['POST'])
def conversor_de_moedas():
    try:
        conversor = float(request.form['conversor'])
        dolar_atual = 5.69
        converter = round((conversor/dolar_atual),2)
        return render_template('index.html',converter=converter)
    except Exception as e:
        converter = f'Ocorreu um erro inesperado {e}'
        return render_template('index.html',converter=converter)


if __name__=='__main__' :
    app.run(debug=True)
