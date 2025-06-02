class Node:
    def __init__(self, dado, prox=None):
        self.dado = dado
        self.prox = prox
    
    def __str__ (self):
        return str(self.dado)