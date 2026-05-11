from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3110", "+79123456789"),
    Smartphone("Xiaomi", "T-34", "+79134567891"),
    Smartphone("Sumsong", "TheLast", "+79141234586"),
    Smartphone("Rus", "MyWay", "+79153216547"),
    Smartphone("Kamaz", "Katusha", "+79169874512"),
]

for smartphone in catalog:
    print (f"{smartphone.mark} - {smartphone.model}. {smartphone.number}")
