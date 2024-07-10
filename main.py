from classes import *
from vagas import * 

lista = ListaEncadeada()
fila = FilaEspera()
torre1 = Torre("Torre 1", "Rua Pato Pelado, 321")
torre2 = Torre("Torre 2", "Rua Cacetinho azul, 1995")
torre3 = Torre("Torre 3", "Rua Roberto Silva, 86")

def novo_apto():
    num = input("Digite o número do apartamento: ")
    print('\n')
    torre1.imprimir()
    torre2.imprimir()
    torre3.imprimir()
    torre = int(input("\nDigite o número da torre deste apartamento: "))
    
    if torre == 1:
        torre = torre1
    elif torre == 2:
        torre = torre2
    elif torre == 3:
        torre = torre3
    
    apto = Apartamento(num)
    apto.cadastrar(torre)
    
    if lista.quantidade < 10:
        lista.adicionar(apto)
    else:
        fila.adicionar(apto)

def liberar_vaga():
    vaga = int(input("Digite o número da vaga a ser liberada: "))
    apto_removido = lista.remover_por_vaga(vaga)
    if apto_removido:
        print(f"Apartamento {apto_removido.numero} da Torre {apto_removido.torre.nome} foi removido da vaga {vaga}.")

        if fila.quantidade > 0:
            apto_fila = fila.remover()
            apto_fila.vaga = vaga
            lista.adicionar(apto_fila)
            print(f"Apartamento {apto_fila.numero} da Torre {apto_fila.torre.nome} foi movido para a vaga {vaga}.")

def menu():
    while True:
        opcao = int(input("""
                          
                        ===================================
                              ꧁ঔৣ☬ M E N U ☬ঔৣ꧂    
                        ===================================
                          
                          1 - Adicionar Apartamento 
                          2 - Mostrar Apartamentos com Vaga 
                          3 - Mostrar Apartamentos sem Vaga
                          4 - Liberar Vaga

                          5 - SAIR\
                          
                          selecione a opção desejada:"""))
            
        if opcao == 5:
            break
              
        elif opcao == 1:
            novo_apto()
            print('\nApartamento adicionado com sucesso!')
                 
        elif opcao == 2:
            lista.imprimir()
              
        elif opcao == 3:
            fila.imprimir()
              
        elif opcao == 4:
            liberar_vaga()
                                        
if __name__ == "__main__":
      menu()

