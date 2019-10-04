import requests
from bs4 import BeautifulSoup
from Helpers.ParseoHelper import ParseoHelper
from Verificacion.VerificacionCriterio01 import VerificacionCriterio01
from Reglas import WCAGReglas

def MostrarResultados(resultados):
    for resultado in resultados:
        print ("%s\n" % (resultado.Descripcion))
        for elemento in resultado.elementos:
            print ("\t - %s" % (elemento))
        print ("\n")


resultados = list()
url = 'http://www.undav.edu.ar'
respuesta = requests.get(url)

# Parsear HTML y guardar como Objeto BeautifulSoup
contenido = BeautifulSoup(respuesta.text, "html.parser")


# Criterio 1- Controlo textos alternativos para elementos que no sean de tipo texto

for regla in WCAGReglas.dictWCAG2A_1:
    #Parsea elementos
    elementos = ParseoHelper.ObtenerElementos(contenido, WCAGReglas.dictWCAG2A_1[regla][1])

    #Verifico regla y guardo el resultado
    resultado_parcial = VerificacionCriterio01.Verificar(elementos, regla, WCAGReglas.dictWCAG2A_1)

    #Agrego resultado a la lista de fallas
    resultados.append(resultado_parcial)

# Muestra los resultados
MostrarResultados(resultados)
