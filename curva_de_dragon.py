import click
import turtle
from random import randrange
from click.types import INT
CADENA_INICIO='FX'
reglas = {
    'X':'X+YF+',
    'Y':'-FX-Y',
    'F':'F',
    '+':'+',
    '-':'-'
}
bgclor="black"
color="green"
angulo=90
segmento=10

def graficar(cadena):
    # Creo una instancia de turtle
    ventana = turtle.Screen()
    ventana.setup(width=1.0, height=1.0, startx=None, starty=None)
    ventana.title('Curva De Dragon')
    ventana.screensize(1280,720)
    ventana.setup(width=1.0, height=1.0, startx=None, starty=None)
    tortuga = turtle.Turtle()
    tortuga.screen.bgcolor(bgclor)
    tortuga.color(color)
    tortuga.speed(200)
    try:
        for simbolo in cadena:
            if simbolo=='+':
                tortuga.right(angle=angulo)
            elif simbolo=='-':
                tortuga.left(angle=angulo)
            elif simbolo=='F':
                tortuga.forward(segmento)
    except Exception as e:
        print("algo paso")
    finally:
        print("la tortuga se canso de caminar y decidió terminar el programa ")
        turtle.write("click to exit", font=("Calibri", 16, "bold"))
        ventana.exitonclick()


def procesar_cadena(cadena):
    resultado=''
    for caracter in cadena:
        resultado+=reglas[caracter]
    return resultado
# Parametros que puede recibir el programa(por ahora solo la cantidad de iteracciones definir que otros parametros se va a enviar)
@click.command()
@click.option('-i', '--iteraciones', required=True,type=click.IntRange(1,1000, clamp=True),help='Cantidad de iteraciones (1..10).')
def inicio(iteraciones):
    print('''Parametros de ejecucion: -> Cantidad de iteraciones: {}'''.format(iteraciones))
    cadena=CADENA_INICIO
    for i in range(0,iteraciones):
         cadena=procesar_cadena(cadena)
    graficar(cadena)
if __name__ == '__main__':
    inicio()