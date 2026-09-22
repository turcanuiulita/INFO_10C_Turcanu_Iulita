import math
unghi_grade=int(input('Dati valoarea unghiului in grade: '))
unghi_rad=math.radians(unghi_grade)
print(math.sin(unghi_rad))
print('Sinus', unghi_grade, '=', math.sin(unghi_rad))
print(round(math.sin(unghi_rad), 2))
print('Sinus de ', unghi_grade, 'grade', '=', round(math.sin(unghi_rad), 4))
print('Cosinus de ', unghi_grade, 'grade', '=', round(math.cos(unghi_rad), 4))