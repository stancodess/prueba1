import telnetlib
import time
import threading
import multiprocessing
from flask import Flask, render_template, request,jsonify, redirect, url_for, flash, session
from api.request_api import RequestsApi

app = Flask( __name__ )
app.secret_key = "1233456789"

HOST = "route-server.he.net."

@app.route( '/' )
def home():
    # Secuencial
    ips = { '181.199.123.174', '181.199.123.173', '216.239.36.21' }
    start_time = time.time()
    output         = []
    #outputParalelo = []
    for ip in ips:
        res = RequestsApi.secuencial(ip)
        output.append( res )
    end_time = time.time()

    print("output")
    print(output)

    time_secuencial = end_time - start_time
    #==========================

    # Paralelo 
    start_time_p = time.time()
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=RequestsApi.paralelo, args = (q, ips))
    p.start()
    outputParalelo = q.get()
    end_time_p = time.time()
    time_paralelo = start_time_p - end_time_p


    return render_template('home.html', secuenciales = output, time_secuencial = time_secuencial, paralelos = outputParalelo ,time_paralelo = time_paralelo)

@app.route( '/pruebaApi', methods=['POST'] )
def about():
    if request.method == 'POST':
        rednetwork = request.get_json()
        print(rednetwork['red'])
        tn = telnetlib.Telnet( HOST )

        comando = 'show bgp ipv4 unicast '

        print ("[!] Conectado a Servidor Telnet -> " + HOST )

        tn.write( comando.encode('ascii') + rednetwork['red'].encode('ascii') + b"\n" )
        tn.write(b"exit\n")
        info = tn.read_all()

        cadena = info.decode()
        separador = "show bgp ipv4 unicast"
        separado = cadena.split(separador)

        respuesta = {
            "data": separado[1]
        }
        return jsonify( respuesta )

if __name__ == '__main__':
    app.run(debug=True)

