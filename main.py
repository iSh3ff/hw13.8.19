num = int(input("Введите количество билетов, которые хотите приобрести:"))
price = 0.0
for i in range(num):

    age = int(input("Введите возраст посетителя:"))
    if age < 18:
        print("Билет бесплатный")
        price = price + 0
    elif 18 <= age < 25:
        print("Цена билета 990 рублей")
        price = price + 990
    else:
        print("Цена билета 1390 рублей")
        price = price + 1390

if num > 3:
        price = price * 0.9
        print("Сумма к оплате", price, "С учетом скидки 10 %")

else:
        print("Сумма к оплате", price)


