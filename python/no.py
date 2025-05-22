class Node:
    def __init__(self, dado, prox=None):
        self.__dado = dado
        self.__prox = prox

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, novo):
        self.__dado = novo

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, novo):
        self.__prox = novo
