class Bookstore:

    def __init__(self, title, author, price, stock, id):
        self._title = title
        self._author = author
        self._price = price
        self._stock = stock
        self._id = id
    
    def show_info(self):
        return (f"\n Título: {self._title} \n Autor: {self._author} \n Price: {self._price} 🟡 \n Stock: {self._stock} 🟡\n ID: {self._id}")

    def test(self):
        pass 

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if price > 0:
            self._price = price
        else: 
            print("⛔ No puedes ingresar un valor inferior a 0 ⛔")

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, stock):
        if stock >= 0:
            self._stock = stock
        else: 
            print("⛔ No puedes ingresar un valor inferior a 0 ⛔")
        
# book1 = Bookstore("Mis inventos", "Nikola Tesla", "80.05", 500, 1 )
# book2 = Bookstore("1984", "G.Orwell", 55.03, 1000, 2)
# print(book1.show_info())
# book1.price = 5
# print(book1.show_info())
# book1.stock = 5
# print(book1.show_info())