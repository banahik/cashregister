import sqlite3



class Product:

    product_list  = []

    def __init__(self, name, name_ru, price, image_data):
        self.name = name
        self.name_ru = name_ru
        self.price = price
        self.image_data = image_data

        if hasattr(self, 'product_list'):
            Product.product_list.append(self)
        else:
            Product.product_list = [self]

    @classmethod
    def load_data(self):
        """
        Загрузить данные из базы данных
        """

        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute(f"""SELECT * FROM Products;""")
        data = self.cursor.fetchall()

        self.connection.commit()
        self.connection.close()


        for product in data:
            Product(name=product[0],
                    name_ru=product[1],
                    price=product[2],
                    image_data=product[3])
            
    @classmethod
    def get_product_by_name(cls, name):

        for one_product in cls.product_list:
            if one_product.name == name:
                return one_product
            
        return cls.product_list[0]


