"""
Formatação de Strings com o método format

"""

a = "aaaa"
b = "BBBBBB"
c = 1.1

string = "b={1} b={1} b={1} b={1} b={1} a={0} b={1} c={2:.2f}" # Significa que quer que apareça 2 casas décimais após a vírgula
formato = string.format( a,b,c)
print(formato)

a = 8
b = "jOAO"
print (a + b)