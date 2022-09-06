#Se importa la libreria para poder usar funciones matematicas complejas
import math


#funcion para el metodo de Bisección
def biseccion(fun, x_a, x_b, eps = None, steps=10):
    #verificar si el metodo de biseccion se puede implementar
    if fun(x_a) * fun(x_b) >= 0:
        print("El metodo de biseccion no puede ser aplicado")
        return None
    
    #calcular el numero de pasos en base a epsilon (eps)
    if eps != None:
        steps = math.ceil(math.log((x_b - x_a) / eps) / math.log(2))
    
    #calcular la raiz con metodo de biseccion
    for n in range(steps +1):
        x_m = (x_a + x_b) / 2

        if fun(x_m) == 0:
            return x_m
        
        if fun(x_a) * fun(x_m) < 0:
            x_b = x_m
        else:
            x_a = x_m

    return (x_a + x_b) / 2

#funcion f(x)
f = lambda x: x - math.cos(x)

print(biseccion(f, 0, 1, 1e-2))