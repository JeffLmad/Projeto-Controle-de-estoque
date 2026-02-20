"""
Projeto: Controle de estoque 
Autor: Jefferson Luiz de Oliveira Madeira
Descrição:
    Um pequeno projeto para demonstrar conhecimentos em python
"""

lista_prod = []
produto = []
quant_prod = []
listar_apagar = []

while True:
    print("\n--- Controle de Estoque ---")
    print("1 - Adicionar produto")
    print("2 - Listar produto")
    print("3 - Alterar  produto")
    print("4 - Remover produto")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção: "))
    print()
    if opcao == 1:
        nome_prod = input("Qual produto deseja cadastrar? ")
        listar_apagar.append(nome_prod)
        quant = int(input(f"Quantas unidades de {nome_prod} deseja cadastrar? "))
        listar_apagar.append(quant)
        produto.append(nome_prod)
        quant_prod.append(quant)
        lista_prod.append(listar_apagar[:])
        listar_apagar.clear()

    elif opcao == 2:
        
        print(f"{'ID':<10}{'Produto':<20}{'Quant.':>10}")
        print()

        for i in range(len(lista_prod)):
            print(f"{i:<10}{produto[i]:<20}{quant_prod[i]:>10}")
    elif opcao == 3:
        print(f"{'ID':<10}{'Produto':<20}{'Quant.':>10}")
        print()

        for i in range(len(lista_prod)):
            print(f"{i:<10}{produto[i]:<20}{quant_prod[i]:>10}")
        print()
        alterar=int(input("Qual produto deseja alterar [ID]:  "))
        posicao = lista_prod.index(lista_prod[alterar])
        print()
        print("O que deseja alterar: ")
        print()
        print("[0] Nome")
        print("[1] Quantidade")
        print()
        opcao_alterar = int(input("Digite a opção a ser alterada: "))
        
        if alterar == posicao:
            if opcao_alterar == 0:
                lista_prod[alterar][opcao_alterar] = str(input("Digite a nova quantidade: "))
                
            if opcao_alterar == 1:
                lista_prod[alterar][opcao_alterar] = int(input("Digite a nova quantidade: "))
         
            
        
 