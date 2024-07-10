class Torre:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        
    def imprimir(self):
        print(f"Nome: {self.nome}\nEndereço: {self.endereco}")

class Apartamento:
    def __init__(self, numero):
        self.numero = numero
        self.torre = None
        self.vaga = None
        self.proximo = None

    def cadastrar(self, torre):    
        self.torre = torre
        print("Torre cadastrada.")
        return 
    def __str__(self):
        estacionamento = ""
        if self.vaga == None:
            estacionamento = "sem vaga de garagem"
        else:
            estacionamento = f"{self.vaga}"
        return f"Apto: {self.numero} | Prédio: {self.torre.imprimir()} | Vaga: {estacionamento}\n"
