from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
import db

Window.size = (350, 600)


class MainScreen(Screen):
    pass


class Sp500StocksScreen(Screen):
    pass


class MainScreenManager(ScreenManager):
    pass


class Stock(BoxLayout):
    def __init__(self, ticker, stock_id, **kwargs):
        super().__init__(**kwargs)

        self.ticker = ticker
        self.stock_id = stock_id
        self.orientation = "horizontal"
        self.size_hint = (1, None)
        self.size = (dp(500), dp(50))

        label = Label(
            outline_color=(0, 1, 1, 1),
            text=self.stock_id + '. ' + self.ticker,
            size_hint=(None, None), size=(dp(80), dp(40))
        )
        self.add_widget(label)
        for j in range(0, 6):
            condition_button = Button(text='C'+str(j+1), size_hint=(None, None), size=(dp(40), dp(40)))
            self.add_widget(condition_button)


class StockList(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        is_loaded = BooleanProperty(False)
        data = db.get_df()
        self.stock_ids = data[1]
        self.tickers = data[0]
        self.i = 0
        # self.size_hint = (1, None)
        # self.height = self.minimum_height
        self.adding = Clock.schedule_interval(self.add_stock, 1/1000)
        self.adding()

    def add_stock(self, arg):
        # print(self.tickers[self.i], )
        print(self.i)
        if self.i < max(self.stock_ids):
            self.add_widget(Stock(self.tickers[self.i], str(self.stock_ids[self.i])))
            self.i += 1
        else:
            print('canceled')
            is_loaded = True
            self.adding.cancel()


class GrahamApp(App):
    pass


GrahamApp().run()
