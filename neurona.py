def mycNeuron(x,i,u):
    output = 0
    if len(i) != 0:
        for elemento in i:
            if elemento == 1:
                return output
    sumaX = sum(x)
    if sumaX >= u:
        output = 1
        return output
    return output

def frankRosenblatt(x,w,b):
    output = 0
    h = 0
    tam = len(x)
    if tam != len(w):
        return output
    for i in range(1,tam):
        h = h + x[i] * w[i]
    h = h + b
    if h >= 0:
        output = 1
        return output
    return output

#Modelado de una compuerta and con McCulloch y Ditts
x1 = 1
x2 = 1
Entradas = [x1, x2]
i = 0
u = 1
output = mycNeuron(Entradas,i,u)
print(output)

#Modelado de una compuerta or con McCulloch y Ditts
x1 = 1
x2 = 1
Entradas = [x1, x2]
i = 0
u = 2
output = mycNeuron(Entradas,i,u)
print(output)

