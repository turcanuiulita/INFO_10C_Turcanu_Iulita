class Anotimp(enumerate):
 PRIMAVARA=1
VARA=2
TOAMNA=3
IARNA=4
Cod=int(input())
anotimp_ales=Anotimp(Cod)
print(anotimp_ales.name)
print(anotimp_ales.value)