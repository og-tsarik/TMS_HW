import shops

table = shops.Table(1530, "Стол", 520, "табурет")
chair = shops.Chair(1823, "Стул", 100, "отсутствует")
cupboard = shops.Cupboard(1401, "Шкаф", 3450, "белый")

furniture_shop = shops.RealShop()

furniture_shop.add_product(table)
furniture_shop.add_product(chair)
furniture_shop.add_product(cupboard)

print(furniture_shop.all_product())
furniture_shop.sell_product(table)
print(f"Продан товар: {table}")
print(furniture_shop.all_product())
