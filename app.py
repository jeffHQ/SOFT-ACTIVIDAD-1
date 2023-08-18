from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/sumar')
def sumar():
    param1 = int(request.args.get('param1', 0))
    param2 = int(request.args.get('param2', 0))
    resultado = param1 + param2
    return f'La suma de {param1} y {param2} es: {resultado}'

@app.route('/multiplicar')
def multiplicar():
    param1 = int(request.args.get('param1', 1))
    param2 = int(request.args.get('param2', 1))
    resultado = param1 * param2
    return f'El producto de {param1} y {param2} es: {resultado}'

if __name__ == '__main__':
    app.run()
