import click
from  turtle import right,left,forward
import turtle
from click.types import INT,STRING
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


#recibe una cadena,un tamaño de segmento y un angulo de giro  y realiza el grafico correspondiente 
def graficar(cadena,segmento,angulo):
    # Creo una instancia de turtle
    ventana = turtle.Screen()
    ventana.title('Curva De Dragon')
    ventana.screensize(800,600)
    mbappe = turtle.Turtle()
    mbappe.screen.bgcolor(bgclor)
    mbappe.color(color)
    mbappe.speed(200)
    funcionalidad={'F':lambda segmento,angulo:dibuja(segmento),
                   '+': lambda segmento,angulo:giro_izquierda(angulo),
                   '-':lambda segmento,angulo:giro_derecha(angulo),
                   'X':lambda segemeto,angulo:nada(),
                   'Y':lambda segmento,angulo:nada()}

    def dibuja (segmento):
         mbappe.forward(segmento)
    def giro_izquierda(angulo):
        mbappe.left(angle=angulo)
    def giro_derecha(angulo):
        mbappe.right(angle=angulo)
    def nada():
        pass
    
    try:
        for simbolo in cadena: # recorro la cadena y por cada caracter ejecuto alguna accion o giro o dibujo un segmento 
           funcionalidad[simbolo](segmento,angulo)
    except Exception as e:
        print("algo paso",e)
    finally:
        print("mbappe se canso de correr y pidio el cambio ")
        ventana.exitonclick()



"""Recibe una Cadena y devuelve su n-esima derivacion con 1<=n<=20"""
def procesar_cadena(cadena):
    resultado=''
    for caracter in cadena:
        resultado+=reglas[caracter] #remplazo el caracter por su corresponidente regla de derivacion
    return resultado

# Parametros que puede recibir el programa(por ahora solo la cantidad de iteracciones definir que otros parametros se va a enviar)
@click.command()
@click.option('-i', '--iteraciones', required=True,type=click.IntRange(1,23, clamp=True),default=10,help='Cantidad de iteraciones (1..23).',prompt="Ingrese el numero de iteracciones:")
@click.option('-cad', '--cadena-inicial', default='FX', show_default=True,help='Cadena inicial.',prompt="Ingrese La Cadena A Derivar:")
@click.option('-ang', '--angulo', required=True,type=click.IntRange(1,360, clamp=True),default=90,help='Angulo de giro (-90..90).',prompt="Ingrese el angulo de giro:")
#Datos De Entrada
# Iteraciones: numero entro mayor a 1 
# Angulo de giro: numero entero 1<=Angulo De Giro<=360
# Cadena De Inicio: Defult=FX    
def inicio(iteraciones,cadena_inicial,angulo):
    segmento=200
    print('''Parametros de ejecucion: -> Cantidad de iteraciones: {}'''.format(iteraciones))
    cadena=cadena_inicial
    for i in range(0,iteraciones):
         cadena=procesar_cadena(cadena)
    segmento=segmento/iteraciones
    #print(segmento)
    graficar(cadena,segmento,angulo)
if __name__ == '__main__':
    inicio()
