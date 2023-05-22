from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior

from http_client import HttpClient
from models import Pizza
from storage_manager import StorageManager


class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    veggi = BooleanProperty()

    def get_veggi(self, veggi):
        if veggi == True:
            return "Végétarienne"
        else:
            return " "


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error_text = ""
        HttpClient().get_pizzas(self.on_server_data, self.on_server_error, self.on_server_failure)

    def on_parent(self, widget, parent):
        pizzas_dict = StorageManager().load_data("pizzas")
        if pizzas_dict:
            self.recycleView.data = pizzas_dict

    def on_server_data(self, pizza_dict):
        self.recycleView.data = pizza_dict
        StorageManager().save_data("pizzas", pizza_dict)

    def on_server_error(self, error):
        self.error_text = "ERROR : " + error
        print("ERREUR : " + error)

    def on_server_failure(self, failure):
        self.error_text = "SERVER FAILURE : " + failure + " - page not found"
        print("ERREUR serveur: " + failure)


class PizzaApp(App):
    pass


PizzaApp().run()