import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self):
        Squadre = DAO.getSquadre()

    def handle_graph(self, e):
        pass
    def handle_details(self, e):
        pass
    def handle_tifosi(self,e):
        pass