class FilaEspera:
    def __init__(self):
        self.primeiro = None
        self.quantidade = 0
    
    def adicionar(self, novo_apartamento):
        if self.primeiro is None:
            self.primeiro = novo_apartamento
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_apartamento
        self.quantidade += 1
        
    def remover(self):
        if self.primeiro is None:
            print("Não há nada na fila para remover.")
        
        removido = self.primeiro
        self.primeiro = self.primeiro.proximo
        self.quantidade -= 1
        removido.proximo = None
        return removido
        
    def imprimir(self):
        atual = self.primeiro
        if atual is None:
            print("\nNão há nada na fila.")
        else:
            print("\nApartamentos aguardando vaga:")
            while atual:
                print(f"Apartamento {atual.numero} - {atual.torre.nome}")
                atual = atual.proximo

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.quantidade = 0
        
    def adicionar(self, novo_apartamento):
        if self.primeiro:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_apartamento
        else:
            self.primeiro = novo_apartamento
        self.quantidade += 1
    
    def remover_por_vaga(self, vaga):
        if self.primeiro is None:
            print("A lista está vazia.")
            return None
        
        if self.primeiro.vaga == vaga:
            item_removido = self.primeiro
            self.primeiro = self.primeiro.proximo
            self.quantidade -= 1
            item_removido.proximo = None
            return item_removido
        
        anterior = self.primeiro
        atual = self.primeiro.proximo
        while atual is not None:
            if atual.vaga == vaga:
                anterior.proximo = atual.proximo
                self.quantidade -= 1
                atual.proximo = None
                return atual
            anterior = atual
            atual = atual.proximo
        
        print("Apartamento com a vaga especificada não encontrado.")
        return None
    
    def imprimir(self):
        atual = self.primeiro
        if atual is None:
            print("\nA lista está vazia.")
        else:
            print("\nApartamentos com Vaga:")
            while atual:
                print(f"Apartamento {atual.numero} - {atual.torre.nome}, Vaga {atual.vaga}")
                atual = atual.proximo