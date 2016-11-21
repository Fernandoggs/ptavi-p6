#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os


class SIPHandler(socketserver.DatagramRequestHandler):
    """
    SIP server class
    """
    IP = sys.argv[1]
	PUERTO = sys.argv[2]
	AUDIO = sys.argv[3]
    def handle(self):
        # Leyendo línea a línea lo que nos envía el cliente
        line = self.rfile.read()
        print("El cliente nos manda " + line.decode('utf-8'))
        Request = line.decode('utf-8')
        if Request.startswith('INVITE'):
            self.wfile.write(b"SIP/2.0 100 Trying\r\n")
            self.wfile.write(b"SIP/2.0 180 Ring\r\n")
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        elif Request.startswith('ACK'):
            aEjecutar = 'mp32rtp -i 127.0.0.1 -p 23032 < ' + AUDIO
            print "Vamos a ejecutar", aEjecutar
            os.system(aEjecutar)

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), SIPHandler)
    print("Listening...")
    serv.serve_forever()
