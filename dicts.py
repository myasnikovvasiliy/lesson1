""" from pprint import pprint

product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1,
}
phones = ["iPhone 12 Pro", "Samsung Galaxy S21", "Xiomi Mi11"]
product["recomended"] = phones
pprint(product)
product["recomended"].append("iPhone 9")
pprint(product) """

from pprint import pprint

stock = [
    {'name': 'Iphone 12 Plus', 'stock': 24, 'price': 65432.1,
        'recomended': ['Samsung Galaxy S21', 'Iphone 12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiami Mi11', 'stock': 42, 'price': 38000.5}
]
#pprint(stock[0]["recomended"][0]) #выводим из словаря 0 обьект из списка
#stock[0]["recomended"].append("Xiomi Mi11")
#stock[2]["price"] = stock[2]["price"] - 30000 #из 3 словоря отимаем 30 тысяч
#pprint(stock)

#узнааем типы
print(type(stock))
print(type(stock[0]))
print(type(stock[0]["recomended"]))
