import telnetlib
from random import randint
from time import strftime
import pymysql.cursors


HOST = "route-server.he.net."
#user = input("Ingrese la ip: ")


tn = telnetlib.Telnet( HOST )
print ("[!] Conectado a Servidor Telnet -> " + HOST )

tn.write(b"show bgp ipv4 unicast 181.39.24.203\n")


tn.write(b"exit\n")

info = tn.read_all()

cadena = info.decode()
separador = "show bgp ipv4 unicast"
separado = cadena.split(separador)

############### CONFIGURAR ESTO ###################
# Abre conexion con la base de datos
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='SCWE1ONQDUT5ojXg13Ed@',
                             database='admin_soporte',
                             cursorclass=pymysql.cursors.DictCursor)
##################################################


#print(info)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `prueba` (`INFORMACION`) VALUES (%s)"
        cursor.execute(sql, (separado[1]))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `ID_PRUEBA`, `INFORMACION` FROM `prueba` ORDER BY `ID_PRUEBA` DESC LIMIT %s"
        cursor.execute(sql, (1,))
        result = cursor.fetchone()
        print(result)



print( "Registro guardado" )