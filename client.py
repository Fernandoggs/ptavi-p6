#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Metodo que quiere enviar el cliente
METHOD = sys.argv[1]
# Cadena con informacion del destinatario
log_str = str(sys.argv[2])
# Dirección IP del servidor.
SERVER = 'localhost'
SERVER2 = log_str[log_str.find('@')+1:log_str.find(':')]
NICK = log_str[:log_str.find('@')]
#Puerto SIP
PORT = 6001
SIP_PORT = int(log_str[log_str.find(':')+1:])

#########################################################################
#METODO = sys.argv[1]
#cadena = str(sys.argv[2])
#LOGIN = cadena[:cadena.find('@')]
#IP = cadena[cadena.find('@')+1:cadena.find(':')]
#PUERTO = int(cadena[cadena.find(':')+1:])

#LINE = METODO + ' sip:'+LOGIN+'@'+IP+' SIP/2.0\r\n'
#LINE2 = 'ACK sip:'+LOGIN+'@'+IP+' SIP/2.0\r\n'
#LINE3 = 'BYE sip:'+LOGIN+'@'+IP+' SIP/2.0\r\n'
#########################################################################
# Contenido que vamos a enviar
LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))
#TRAZA#####################################
print("METODO introducido: " + METHOD)
print("NICK introducida: " + NICK)
print("IP introducida: " + SERVER2)
print("PUERTO SIP introducido: " + SIP_PORT)
#TRAZA#####################################
print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
