class Recursividad:

    def SepararNumeros(self, num):
        if (num < 10 and num > 0):
            return num
        else:
            return (int((num / 10) / 10)) + (int((num / 10) % 10)) + num % 10