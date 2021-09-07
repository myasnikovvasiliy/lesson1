#одно условие
""" balance = 5

print(bool(balance < 0))

if balance < 0:
    print("Пополните баланс!") """


#Не сколько условий

""" balance = 5
price = 10

print(bool(balance < 0 or price > balance))

if balance < 0 or price > balance:
    print("Пополните баланс!") """

#Конструкция else
""" balance = 10
price = 9

if balance > price:
    print("Спасибо за покупку!")
else:
    print("Пополните баланс!") """

#Конструкция elif
""" temperature = 16

if temperature <= 0:
    print("На улице холодно")
elif 1 <= temperature <= 15:
    print("На улице прохладно")
elif 16 <= temperature <= 25:
    print("На улице тепло")
else:
    print("На улице жарко") """

#Заварачиваем в функцию
""" def weather(temperature):
    if temperature <= 0:
        return "На улице холодно" 
    elif 1 <= temperature <= 15:
        return "На улице прохладно"
    elif 16 <= temperature <= 25:
        return "На улице тепло"
    else:
        return "На улице жарко"
print(weather(-2))
print(weather(5))
print(weather(16))
print(weather(30)) """

#Формируем правильное условие, с помощью конструкцию or
""" phone1 = {'name': 'Iphone 12 Plus', 'stock': 24, 'price': 65432.1, 'discount': 15}#словаь описывающий телефон
phone2 = {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 10}#словаь описывающий телефон

def discounted(price, discount, max_discount=20, name=""):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount >= 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or "iphone" in name.lower():#задаем условие что на айфон не было скидки
        return price
    else:
        return price - (price * discount / 100)
    
apple_desc = discounted(phone1["price"], phone1["discount"], name=phone1["name"])
print(apple_desc)#для айфона

android_desc = discounted(phone2["price"], phone2["discount"], name=phone2["name"])
print(android_desc)#для андройда """

#С использованием not
phone1 = {'name': 'Iphone 12 Plus', 'stock': 24, 'price': 65432.1, 'discount': 15}#словаь описывающий телефон
phone2 = {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 10}#словаь описывающий телефон
phone3 = {'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}#словаь описывающий телефон

def discounted(price, discount, max_discount=20, name=""):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount >= 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or "iphone" in name.lower() or not name:#задаем условие что теф без имини не было скидки
        return price
    else:
        return price - (price * discount / 100)
    
apple_desc = discounted(phone1["price"], phone1["discount"], name=phone1["name"])
print(apple_desc)#для айфона

android_desc = discounted(phone2["price"], phone2["discount"], name=phone2["name"])
print(android_desc)#для андройда

noname_desc = discounted(phone3["price"], phone3["discount"], name=phone3["name"])
print(noname_desc)#для noname