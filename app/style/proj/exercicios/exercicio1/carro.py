from veiculo import veiculo

class carro(veiculo):

    def __init__(self,marca:str, ano:int):
        super().__init__(marca,ano)
        