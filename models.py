class Pizza:
    name = ""
    ingredients= ""
    price = 0.0
    veggi = False

    def __init__(self, name, ingredients, price, veggi):
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.veggi = veggi

    def get_dictionnary(self):
        return {"name": self.name,
                "ingredients": self.ingredients,
                "price": self.price,
                "veggi": self.veggi
                }
