Putere=int(input('Dati puterea in (W): '))
Timp=int(input('Dati timpul in (h): '))
Energia=Putere*Timp/1000
print(f"Spre achitare: {Energia:.2f} kWh")
Tarif=float(input(' Dati tariful actual (lei/kWh): '))
Cost=Energia*Tarif
print(f"Costul total este: {Cost:.2f} lei")