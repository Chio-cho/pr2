class Dish:
    def __init__(self, name, category, price, weight):
        self.name = name
        self.category = category
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"Блюдо: {self.name}, Категория: {self.category}, Стоимость: {self.price}, Вес: {self.weight}"

class Menu:
    def __init__(self, f="aaaa.txt"):
        self.menu = self.read(f)

    def read(self, f):
        dishes = {}
        with open(f, 'r') as file:
            for line in file:
                name, category, price, weight = line.strip().split(', ')
                price = int(price)
                weight = int(weight)
                dishes[name] = Dish(name, category, price, weight)
        return dishes
    
    def addDish(self):
        name = input("Название блюда: ")
        category = input("Категория: ")
        price = int(input("Цена: "))
        weight = int(input("Вес: "))
        new= Dish(name, category, price, weight)
        self.menu[name] = new
        self.update_file()

    def delDish(self, name):
        if name in self.menu:
            del self.menu[name]
            self.update_file()

    def editDish(self, name):
        if name in self.menu:
            new_name = input("Введите новое название блюда: ")
            new_category = input("Введите новую категорию: ")
            new_price = int(input("Введите новую цену блюда: "))
            new_weight = int(input("Введите новый вес блюда: "))
            self.menu[name].name = new_name
            self.menu[name].category = new_category
            self.menu[name].price = new_price
            self.menu[name].weight = new_weight
            self.update_file()

    def update_file(self):
        with open('aaaa.txt', 'w') as file:
            for dish in self.menu.values():
                file.write(f"{dish.name}, {dish.category}, {dish.price}, {dish.weight}\n")

def write(menu, c, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        recursive(menu, c, file)

def recursive(menu, c, file):
    for name, dish in menu.items():
        if dish.category == c:
            file.write(f"{dish.name},{dish.price},{dish.weight}\n")

def sort(menu, c, max_price):
    dishes = []
    for name, dish in menu.items():
        if dish.category == c and dish.price <= max_price:
            dishes.append(dish)
    dishes.sort(key=lambda dish: dish.price)
    return dishes

def search(menu, n):
    l = []
    for name, dish in menu.items():
        if dish.name == n:
            l.append(dish)
    return l

def display_menu(menu):
    for name, dish in menu.items():
        print(dish)
