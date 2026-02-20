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
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    print()
    if opcao == 1:
        nome_prod = str(input("Qual produto deseja cadastrar? "))
        produto.append(nome_prod)
        quant = int(input(f"Quantas unidades de {nome_prod} deseja cadastrar? "))
        quant_prod.append(quant)
    elif opcao == 2:
        
        print(f"{'ID':<10}{'Produto':<20}{'Quant.':>10}")
        print()

        for i in range(len(produto)):
            print(f"{i:<10}{produto[i]:<20}{quant_prod[i]:>10}")
    elif opcao == 3:
        print(f"{'ID':<10}{'Produto':<20}{'Quant.':>10}")
        print()

        for i in range(len(produto)):
            print(f"{i:<10}{produto[i]:<20}{quant_prod[i]:>10}")
        print()
        alterar=int(input("Qual produto deseja alterar [ID]:  "))
        posicao = produto.index(produto[alterar])
        print()
        print("O que deseja alterar: ")
        print()
        print("[0] Nome")
        print("[1] Quantidade")
        print()
        opcao_alterar = int(input("Digite a opção a ser alterada: "))
        
        if alterar == posicao:
            if opcao_alterar == 0:
                produto[posicao] = str(input("Digite o novo nome: "))
                
                
            if opcao_alterar == 1:
                quant_prod[posicao] = int(input("Digite a nova quantidade: "))
    elif opcao == 4:
        print(f"{'ID':<10}{'Produto':<20}{'Quant.':>10}")
        print()

        for i in range(len(produto)):
            print(f"{i:<10}{produto[i]:<20}{quant_prod[i]:>10}")
        print()

        remover = int(input("Qual produto deseja remover[ID]: "))    
        del produto[remover]
    elif opcao == 0:
        break   
            
        
 