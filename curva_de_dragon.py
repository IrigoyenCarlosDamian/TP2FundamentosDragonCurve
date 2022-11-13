import click
import turtle
from random import randrange
from click.types import INT, STRING, IntParamType, IntRange

reglas = {
    'X':'X+YF+',
    'Y':'-FX-Y'
}
bgclor="black"
color="green"
angulo=90
segmento=8

def graficar(cadena):
    # Creo una instancia de turtle
    ventana = turtle.Screen()
    ventana.setup(width=1.0, height=1.0, startx=None, starty=None)
    ventana.title('Curva De Dragon')
    ventana.screensize(1920 * 3, 1080 * 3)
    ventana.setup(width=1.0, height=1.0, startx=None, starty=None)
    tortuga = turtle.Turtle()
    tortuga.screen.bgcolor(bgclor)
    tortuga.color(color)
    tortuga.speed(200)
    try:
        for simbolo in cadena:
            if simbolo=='F': #DIBUJO UN SEGMENTO
                tortuga.forward(segmento)
                
            elif simbolo=='+': #ME MUEVO A LA DRECHA EN UN ANGULO DE 90
                tortuga.right(angulo)

            elif simbolo=='-': #ME MUEVO A LA IZQUIERDA EN UN ANGULO DE 90
                tortuga.left(angulo)
            else:
                turtle.backward(segmento)

    except Exception as e:
        print("algo paso")
    finally:
        print("la tortuga se canso de caminar y desidio terminar el programa")




def procesar_cadena(iteraciones):
    resultado = 'FX' #iteracion 0
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
    graficar(cadena)
if __name__ == '__main__':
    inicio()