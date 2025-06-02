from node import node
class fila:
    def __init__(self, prox, dado):
        self.__inicio = node(dado)
        self.__fim = self.__inicio
        self.__tamanho = 1
        