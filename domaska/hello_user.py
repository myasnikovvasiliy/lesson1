
def user_fun():
    while True:
        user_say = input('Как дела? ')
        if user_say == 'Хорошо':
            break#цикл закончен
        else:
            print('Давай ещё {}'.format(user_say))
        
user_fun()