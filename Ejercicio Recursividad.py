class Recursividad:

    def SepararNumeros(self, num):
        if (num < 10 and num > 0):
            return num
        else:
            return (int((num / 10) / 10)) + (int((num / 10) % 10)) + num % 10

Rec = Recursividad()
a = [687, 135, 439, 852, 363]
c = []

for b in range(0, len(a)):
    g = Rec.SepararNumeros(a[b])
    c.append(g)
print(c)