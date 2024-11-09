from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
      return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product): # tuple
    __file_name = 'products.txt'


    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        print(file)
        file.close()

    def add(self, *products):
        for i in products:
            if i.get_product() not in self.__file_name:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')

    def __str__(self):
        return '\n'.join(str(i) for i in self.products)

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
