"""
Se define el nombre de la clase, en este caso
tiene el nombre del tema a resolver.
"""
class Recursividad:

    """
    Metodo en que se establece una formula para separar
    los digitos de una secuencia de numeros enteros.
    """
    def SepararNumeros(self, num):
        if (num < 10 and num > 0):
            return num
        else:
            return (int((num / 10) / 10)) + (int((num / 10) % 10)) + num % 10

"""
Se le da un nombre al objeto de la clase y se colccan 
la secuencia de numeros en una lista, estableciendo tambien
una lista vacia para colocar las sumas de cada digito.
"""
Rec = Recursividad()
a = [687, 135, 439, 852, 363]
c = []

"""
Se aplica el metodo iterativo con el ciclo for en el que
toma el tamaño de la lista (a) y agregando los resultados de las
sumas en la nueva lista (c), utilizando la formula anterior.
"""
for b in range(0, len(a)):
    g = Rec.SepararNumeros(a[b])
    c.append(g)
print(c)