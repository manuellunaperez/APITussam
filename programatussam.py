#encoding=utf-8
import requests
from lxml import etree
from suds.client import Client
import os
import sys
cliente = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)	
linea = int(raw_input("Introduce una linea de Tussam: "))
try:
	respuesta = cliente.service.GetStatusLinea(linea)
except:
	os.system('clear')
	print "¡Huy! Esta linea no existe. Prueba de nuevo..."
else: 
	raiz =  etree.fromstring(respuesta.encode("utf-8"))
	raiz2 = raiz[0][0]
	ns = "{http://tempuri.org/}"
	xml = raiz2.find(ns+"GetStatusLineaResult")
	activos = xml.find(ns+"activos")
	frecuencia = xml.find(ns+"frec_bien")
	graves = xml.find(ns+"graves")
	os.system('clear')
	print "Información sobre la linea de Tussam: %s" % linea
	print "Número de coches actual : %s" % activos.text
	print "Número de coches que van bien de frecuencia: %s" % frecuencia.text
	print "Número de incidencias graves: %s " % graves.text

