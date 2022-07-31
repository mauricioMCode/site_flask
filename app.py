from flask import Flask, request

empregados = [
                {'nome':'Mauricio', 'cargo':'analista', 'salario':5000},
                {'nome':'Nelma', 'cargo':'analista', 'salario':3000},
                {'nome':'Osvaldo', 'cargo':'dba', 'salario':4000}
             ]

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bem-vindo ao Flask</h1>"

@app.route("/empregados")
def get_empregados():
    return {'empregados': empregados}

@app.route("/empregados/<cargo>")
def get_empregados_cargo(cargo):
    out_empregados = []
    for empregado in empregados:
        if cargo == empregado['cargo'].lower():
            out_empregados.append(empregado)
    return {'empregados': out_empregados}

@app.route("/empregados/<info>/<value>")
def get_empregados_info(info, value):
    out_empregados = []
    for empregado in empregados:
        if info in empregado.keys():
            value_empregado = empregado[info]

            if type(value_empregado) == str:
                if value == value_empregado.lower():
                    out_empregados.append(empregado)
            if type(value_empregado) == int:
                if int(value) == value_empregado:
                    out_empregados.append(empregado)
    return {'empregados': out_empregados}

@app.route("/informations", method=['POST'])
def get_empregados_post():

    info = request.form['info']
    value = request.form['value']

    out_empregados = []
    for empregado in empregados:
        if info in empregado.keys():
            value_empregado = empregado[info]

            if type(value_empregado) == str:
                if value == value_empregado.lower():
                    out_empregados.append(empregado)
            if type(value_empregado) == int:
                if int(value) == value_empregado:
                    out_empregados.append(empregado)
    return {'empregados': out_empregados}

if __name__ == "__main__":
    app.run(debug=True)

    