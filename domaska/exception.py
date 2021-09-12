
def discounted(price, discount, max_discount=20):
        try:
            price = abs(int(price))
            discount = abs(int(discount))
            max_discount = abs(int(max_discount))
            if max_discount >= 100:
                raise ValueError('Слишком большая максимальная скидка')
            if discount >= max_discount:
                print(price)
            else:
                result = price - (price * discount / 100)
                print(result)
        except ValueError:
            print('Введите цифры . Не верный формат данных')
    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))