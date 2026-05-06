def is_year_leap(num):
    if num % 4 == 0:
        return "True"
    else:
        return "False"


year = int(input("Введите год: "))

result = is_year_leap(year)

print(f"год {year}: {result}")
