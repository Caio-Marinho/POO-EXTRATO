class Cliente:

    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone

    pass

    # metodo get
    def get_nome(self):
        return self._nome

    # metodo set
    def set_nome(self, nome):
         self._nome = nome

    @property
    def nome(self):
        return self._nome
