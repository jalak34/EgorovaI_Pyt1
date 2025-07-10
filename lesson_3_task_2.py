from smartphone import Smartphone

catalog = (
    [Smartphone("Xiaomi","Readmi", "+79213458724"),
    Smartphone("Apple", "iPhone13","+79118872456"),
    Smartphone("Samsung", "GalaxyA06", "+79049876543"),
    Smartphone("HUAWEI", "novaY6", "+79214875601"),
    Smartphone("Motorola", "Moto G05", "+79990983487")
    ]
)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
