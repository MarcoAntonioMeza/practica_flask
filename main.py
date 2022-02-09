
from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


items = ['item 1','item 2','item 3','item 4']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.route("/index")
def index():
    usuario_ip = request.remote_addr
    respuesta = make_response(redirect('/mostrar_info'))
    respuesta.set_cookie('ip_usuario',usuario_ip)
    return respuesta

@app.route("/mostrar_info")
def mostrar_informacion():
    ip_usuario=request.cookies.get("ip_usuario")
    contexto ={
        'ip_usuario': ip_usuario,
        'items': items
    }
    return render_template("ip_information.html", **contexto)

app.run(host='0.0.0.0',port=5000, debug=True)