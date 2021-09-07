user_vozrast = input('Введите ваш возраст? ')

def vozrast(user_vozrast):

    if user_vozrast <= 5:
        return "Пора в детский сад" 
    elif 6 <= user_vozrast <= 16:
        return "Пора в школу"
    elif 17 <= user_vozrast <= 22:
        return "Пора в универ"
    elif 23 <= user_vozrast <= 65:
        return "Пора бы и на работу сходить:)"
    else:
        return "На конец-то на пенсию!"

opredelim_vozrast = vozrast(float(user_vozrast))#вызываем функцию
print(opredelim_vozrast)
