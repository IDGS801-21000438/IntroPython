"""
Las tuplas son imutables
"""


tupla= ("uno","dos","tres")

print(tupla)
tuplaVariosDatos = (12, True,243.23,"El gato miauuu",9943-12)
print(tuplaVariosDatos)
a,b,c = tupla
print(a)
print(b)
print(c)


tuplaNueva = tupla + tuplaVariosDatos

print(tuplaNueva)

