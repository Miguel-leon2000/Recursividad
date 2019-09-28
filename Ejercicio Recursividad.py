"""
Se define el nombre de la clase, en este caso
tiene el nombre del tema a analizar.
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
    Se declara un metodo para sumar los digitos de una
    secuencia de numeros enteros en una lista, estableciendo tambien
    una lista vacia para colocar las sumas de cada digito.
    """
    def SumarDigitos(self):
        a = [687, 135, 439, 852, 363]
        c = []

        """
        Se aplica el metodo iterativo con el ciclo for en el que
        toma el tamaño de la lista (a) y se agregan los resultados de las
        sumas en la nueva lista (c), utilizando la formula del metodo anterior.
        """
        for b in range(0, len(a)):
            g = Rec.SepararNumeros(a[b])
            c.append(g)
        print(c)

        """
        Se implementa la forma para mostrar el numero cuya suma 
        de digitos es mayor.
        """
        d = c.copy()

        d.sort()

        x = d[len(d) - 1]

        i = c.index(x)

        print("El numero mayor es: ", a[i])

Rec = Recursividad()   #Se le asigna un nombre al objeto de la clase
Rec.SumarDigitos()     #Se manda llamar al metodo "SumarDigitos"
