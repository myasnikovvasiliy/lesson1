#Практика: Сравнение строк
def proverka_na_str(str1, str2):# две строки
    if type(str1) is not str and type(str2) is not str:#
        print (0)
    elif len(str1) == len(str2):
        print (1)
    elif len(str1) > len(str2):
        print (2)
    elif len(str1) != len(str2) and str2 == 'learn':
        print (3)

if __name__ == '__main__':
    proverka_na_str('aaa', 'aaaa')