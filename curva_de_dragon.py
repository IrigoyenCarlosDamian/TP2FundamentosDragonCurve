import click
import turtle
from random import randrange
from click.types import INT, STRING, IntParamType, IntRange

reglas = {
    'X':'X+YF+',
    'Y':'-FX-Y'
}

def procesar_cadena(iteraciones):
    resultado = 'FX' #iteraccion 0
    for i in range(0, iteraciones):
        for caracter in resultado:
            if caracter in reglas:
                resultado += reglas[caracter]
            else:
                resultado += caracter
           
    return resultado

# Parametros que puede recibir el programa(por ahora solo la cantidad de iteracciones definir que otros parametros se va a enviar)
@click.command()
@click.option('-i', '--iteraciones', 
                required=True, 
                type=click.IntRange(1, 10, clamp=True), 
                help='Cantidad de iteraciones (1..10).')

def inicio(iteraciones):
    print('''Parametros de ejecucion: 
    -> Cantidad de iteraciones: {}'''
    .format(iteraciones))
    cadena=''
    cadena+=procesar_cadena(iteraciones)
    print(cadena)
    print(len(cadena))
if __name__ == '__main__':
    inicio()