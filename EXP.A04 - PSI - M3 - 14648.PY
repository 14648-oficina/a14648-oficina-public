import datetime
from os import close
from colorama import Fore

def guardar_pedidos(pedidos):
    for id_pedido, info in pedidos.items():
        pedido = pedidos[id_pedido]
        PedidosGuardados = open("Pedidos.txt", "a")
        PedidosGuardados.write(Fore.WHITE + f"\nPedido #{id_pedido} - Descrição: {pedido['descricao']}, Estado: {pedido['estado']}, Data: {pedido['data']}")
        PedidosGuardados.close()
    
def eliminar_pedido(pedidos):
    id_pedido = int(input("Qual é o ID do Pedido que quer Apagar: "))
    if id_pedido in pedidos:
        pedidos.pop(id_pedido)
        print("Pedido Apagado Com Sucesso")
    else:
        print("Pedido não encontrado")
    

def registar_pedido(pedidos):
    id_pedido = len(pedidos) + 1
    descricao = input("Descrição do problema: ")
    estado = (Fore.RED + "Pendente" + Fore.WHITE)
    data1 = datetime.datetime.now()
    data2 = (data1.strftime("%d/%m/%Y"))
    pedidos[id_pedido] = {"descricao": descricao, "estado": estado, "data": data2}
    print(f"Pedido #{id_pedido} registado com sucesso!")


def consultar_pedido(pedidos):
    id_pedido = int(input("ID do pedido a consultar: "))
    if id_pedido in pedidos:
        pedido = pedidos[id_pedido]
        print(f"Pedido #{id_pedido} - Descrição: {pedido['descricao']}, Estado: {pedido['estado']}, Data: {pedido['data']}")
    else:
        print("Pedido não encontrado.")

def atualizar_estado(pedidos):
    id_pedido = int(input("ID do pedido a atualizar: "))
    if id_pedido in pedidos:
        novo_estado = input("Novo estado (Pendente/Em Andamento/Concluído/Custom): ")
        if novo_estado in ["Pendente", "Em Andamento", "Concluído"]:
            if novo_estado == "Pendente":
                pedidos[id_pedido]["estado"] = (Fore.RED + novo_estado + Fore.WHITE)
                print(f"Estado do pedido #{id_pedido} atualizado para '{novo_estado}'.")
            elif novo_estado == "Em Andamento":
                pedidos[id_pedido]["estado"] = (Fore.YELLOW + novo_estado + Fore.WHITE)
                print(f"Estado do pedido #{id_pedido} atualizado para '{novo_estado}'.")
            elif novo_estado == "Concluído":
                pedidos[id_pedido]["estado"] = (Fore.GREEN + novo_estado + Fore.WHITE)
                print(f"Estado do pedido #{id_pedido} atualizado para '{novo_estado}'.")
        elif novo_estado in ["Custom"]:
            novo_estado = input("Estado Custom: " )
            pedidos[id_pedido]["estado"] = (Fore.MAGENTA  + novo_estado + Fore.WHITE)
            print(f"Estado do pedido #{id_pedido} atualizado para '{novo_estado}'.")
        else:
            print("Estado inválido.")
    else:
        print("Pedido não encontrado.")

def exibir_pedidos(pedidos):
    print("\nLista de Pedidos:")
    print("ID\tDescrição\tEstado\t\tData")
    print("-" * 50)
    for id_pedido, info in pedidos.items():
        print(f"{id_pedido}\t{info['descricao'][:18]}\t{info['estado']}\t\t{info['data']}")
def main():
  pedidos = {}
  while True:
      print("\nSistema de Gestão de Pedidos - Manutenção")
      print("1. Registar Pedido")
      print("2. Consultar Pedido")
      print("3. Atualizar Estado")
      print("4. Exibir Todos os Pedidos")
      print("5. Eliminar Pedido")
      print("6. Guardar Pedidos")
      print("7. Sair")
      opcao = input("Escolha uma opção: ")

      if opcao == "1":
          registar_pedido(pedidos)
      elif opcao == "2":
          consultar_pedido(pedidos)
      elif opcao == "3":
          atualizar_estado(pedidos)
      elif opcao == "4":
          exibir_pedidos(pedidos)
      elif opcao == "5":
          eliminar_pedido(pedidos)
      elif opcao == "6":
          guardar_pedidos(pedidos)
      elif opcao == "7":
          print("Encerrando o sistema...")
          break
      else:
          print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
