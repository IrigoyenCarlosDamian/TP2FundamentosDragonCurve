reglas = {
    'X':'X+YF+',
    'Y':'-FX-Y'
}
def procesar_cadena(iteraciones):
    resultado = 'FX'
    for i in range(0, iteraciones):
        for caracter in resultado:
            if caracter in reglas:
                resultado += reglas[caracter]
                print(resultado)
            else:
                resultado += caracter
    return resultado

def inicializar():
    cadena=''
    cadena+=procesar_cadena(10)
    input('\nPresione ENTER para mostrar la cadena.')
    print(cadena)

if __name__ == '__main__':
    inicializar()
