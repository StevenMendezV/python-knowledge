from bookstore import Bookstore

class Comic(Bookstore):

    def __init__(self, title, author, price, stock, id, illustrator, volumen):
        pass
        super().__init__(title, author, price, stock, id)
        self._illustrator = illustrator
        self._volumen = volumen
    
    def show_info(self):
        # return super().show_info()
        parameters = super().show_info()
        str_illustrator = ",".join(self._illustrator)
        return print(parameters + f""" \n Illustrators: {str_illustrator} \n Volumen: {self._volumen}""")
        # return print(f"\n Título: {self._title} \n Autor: {self._author} \n Price: {self._price} 🟡 \n Stock: {self._stock} 🟡\n ID: {self._id}" + f""" \n Illustrators: {str_illustrator} \n Volumen: {self._volumen}""")

# comic1 = Comic("Batman y Robin", "Cristian Hernandez", 500, 666, 123, ["Steven Mendez","Ricardo Hernandez"], 1)
# comic1.show_info()

