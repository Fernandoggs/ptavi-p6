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
server_aux = log_str.split('@')[1]
SERVER = server_aux.split(':')[0]
#Nick de la persona ala que va dirigido el mensaje
NICK = log_str.split(':')[0]
#Puerto SIP
PORT = int(server_aux.split(':')[1])
# Contenido que vamos a enviar
LINE = METHOD + ' sip:' + NICK + ' SIP/2.0\r\n'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect(('127.0.0.1', PORT))
#TRAZA#####################################
print("METODO: " , METHOD)
print("NICK: " , NICK)
print("IP_SERVER: " , SERVER)
print("PUERTO SIP: " ,PORT)
#TRAZA#####################################
print("Enviando: " , LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
