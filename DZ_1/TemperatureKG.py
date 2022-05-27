Osh = float(input("температура Ош: "))
Chuy = float(input("температура Чуй: "))
Talas = float(input("температура Талас: "))
Naryn = float(input("температура Нарын: "))
Ysykkol = float(input("температура Ысык-кол: "))
Batken = float(input("температура Баткен: "))
Djalalabad = float(input("температура Джала-абад: "))

result = (Batken + Osh + Chuy + Talas + Naryn + Ysykkol + Djalalabad) / 7

print("средняя температура КР: ", round(result, 2))