from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 17 Pro", "+79453647122"),
    Smartphone("Samsung", "Galaxy S26 Ultra", "+79573642745"),
    Smartphone("Xiaomi", "Redmi Note 14", "+7985372166"),
    Smartphone("Realme", "Realme 16 Pro", "+79748397495"),
    Smartphone("Honor", "Honor X5c", "+79648384756")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phoneNumber}")
