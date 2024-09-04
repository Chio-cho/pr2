class Dish:
    def __init__(self, name, category, price, weight):
        self.name = name
        self.category = category
        self.price = int(price)
        self.weight = int(weight)

    def __str__(self):
        return f"Dish: {self.name}, Категория: {self.category}, Стоимость: {self.price}, Вес: {self.weight}"

class Menu:
    def __init__(self, f="aaaa.txt"):
        self.menu_dict = self.read(f)
        self.count = len(self.menu_dict)
    def appendDish(self, line):
        parts = line.strip().split(', ')
        if len(parts) == 4:
            name, category, price, weight = parts
            try:
                price = int(price)
                weight = int(weight)
                if name not in self.menu_dict:
                    self.menu_dict[name] = Dish(name, category, price, weight)
                    self.count += 1
                else:
                    print(f"Блюдо '{name}' уже существует.")
            except ValueError:
                print(f"Некорректная стоимость или вес для блюда: {name}")
        else:
            print(f"Некорректная строка: {line.strip()}")
    def read(self, f):
        dishes = {}
        try:
            with open(f, 'r') as file:
                for line in file:
                    name, category, price, weight = line.strip().split(', ')
                    price = int(price)
                    weight = int(weight)
                    dishes[name] = Dish(name, category, price, weight)
        except FileNotFoundError:
            print(f"Файл '{f}' не найден.")
        return dishes
