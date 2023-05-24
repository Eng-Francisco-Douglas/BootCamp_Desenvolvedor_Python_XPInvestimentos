# Definir o valor de PI
pi = 3.14564

# Calcula a area do quadrado
def quadrado(l):
    return l ** 2

# Calcula a area de um triangulo
def triangulo(b, h):
    return(b * 2) /2

# Calcula a area de um circulo
def circulo(r):
    return pi * (r ** 2)

# Calcula a area de uma elipse
def elipse(a, b):
    return pi * a * b

# Calcula a area de um trapezio
def trapezio(B, b, h):
    return (B+b) * h / 2
