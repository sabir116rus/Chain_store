class Store:
    def __init__(self, name, address):

        # Конструктор класса Store, инициализирует название, адрес и пустой словарь товаров.
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):

        # Метод для добавления товара в ассортимент магазина.
        self.items[item_name] = price

    def remove_item(self, item_name):

        # Метод для удаления товара из ассортимента магазина.
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):

        # Метод для получения цены товара по его названию.
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):

        # Метод для обновления цены товара.
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание объектов класса Store
store1 = Store("Прод1", "Митинова 53")
store2 = Store("Прод2", "Пушкина 3")
store3 = Store("Прод3", "Култина 65")

# Добавление товаров в магазины
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)
store2.add_item("апельсины", 0.6)
store2.add_item("груши", 1.2)
store3.add_item("молоко", 1.5)
store3.add_item("хлеб", 2.0)

# Тестирование методов на примере store1
print(f"Начальные товары в {store1.name}: {store1.items}")

# Добавление товара
store1.add_item("вишни", 1.5)
print(f"После добавления вишни: {store1.items}")

# Обновление цены товара
store1.update_price("бананы", 0.8)
print(f"Товары после обновления цены бананов: {store1.items}")

# Удаление товара
store1.remove_item("яблоки")
print(f"Товары после удаления яблок: {store1.items}")

# Запрос цены товара
banana_price = store1.get_price("бананы")
print(f"Цена бананов: {banana_price}")

# Запрос цены отсутствующего товара
apple_price = store1.get_price("яблоки")
print(f"Цена яблок: {apple_price}")
