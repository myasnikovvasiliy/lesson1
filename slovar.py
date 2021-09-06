slovar = {"city": "Москва", "temperature": "20"}
slovar["temperature"] = "15"
slovar["date"] = "27.05.2019"
print(slovar)
print(slovar.get("country"))
print(slovar.get("country", "Россия"))
print(len(slovar))
