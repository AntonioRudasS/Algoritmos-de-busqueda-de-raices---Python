import math

def secante(fun, x_a, x_b, steps = 50):
    
    if fun(x_a) * fun(x_b) >= 0:
        print("El metodo secante no aplica")
        return None
    
    for n in range(steps+1):
        x_n = x_a - fun(x_a) * (x_b - x_a)/(fun(x_b) - fun(x_a))

        if fun(x_n) == 0:
            return x_n
        
        if fun(x_a) * fun(x_n) < 0:
            x_b = x_n
        else:
            x_a = x_n
        
    return x_n


f = lambda x: x - math.cos(x)

print(secante(f, 0, 5, 15))