from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/consultas')
def consultas():
    return render_template('consultas.html')

@app.route('/paineis')
def paineis():
    return render_template('paineis.html')

@app.route('/saibamais')
def saibamais():
    return render_template('saibamais.html')

@app.route('/busca')
def busca():
    return render_template('busca.html')

@app.route('/ouvidoria')
def ouvidoria():
    return render_template('ouvidoria.html')

@app.route('/processos')
def processos():
    return render_template('processos.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)