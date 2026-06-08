from flask import Flask, render_template , request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/simular', methods=['POST'])
def simular():
    valor_inicial = float(request.form.get('investimento_inicial'))
    taxa_juros = float(request.form.get('taxa_juros_mensal'))
    
    duracao_investimento = int(request.form.get('duracao_investimento'))

    valor_final = valor_inicial
    for _ in range(duracao_investimento * 1):
        
        valor_final += valor_final * (taxa_juros / 100) / 1

    valor_total_investido = valor_inicial + (taxa_juros / 100) * duracao_investimento * 1
    ganho_total = valor_final - valor_total_investido

    return render_template('index.html', valor_final=f"{valor_final:.2f}", valor_total_investido=f"{valor_total_investido:.2f}", ganho_total=f"{ganho_total:.2f}")
if __name__ == '__main__':
    app.run(debug=True , port=5000 , host='0.0.0.0')
