class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        str_out = ''
        str_out += self.name + ', ' + str(self.weight) + ', ' + (self.category)
        return str_out

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r+')
        file_str = file.read()
        file.close()
        return file_str

    def add(self, *products):
        file = open(self.__file_name, 'a')
        file.close()
        in_file = self.get_products()
        file = open(self.__file_name, 'a')
        for i in products:
            if in_file.find(i.name) == -1:
                file.write(str(i))
                file.write('\n')
            else:
                print(f'Продукт {i.name} уже есть в магазине' )
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

