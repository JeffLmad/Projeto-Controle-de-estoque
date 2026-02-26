"""
Projeto: Controle de estoque 
Autor: Jefferson Luiz de Oliveira Madeira
Descrição:
    Um pequeno projeto para demonstrar conhecimentos em python
"""
#fazer amanhã o tratamento de erro do bloco 3 - alteração de produto
import time

produto = []
quant_prod = []


while True:
    print("-"*50)
    print(f"{"CONTROLE DE ESTOQUE:":^50}")
    print("-"*50)
    time.sleep(0.5)
    print("1 - Cadastrar produto")
    print("2 - Listar produto")
    print("3 - Alterar  produto")
    print("4 - Remover produto")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    resp = opcao
    print()
    if opcao == 1:
        while True:
            time.sleep(0.5)
            print("-"*50)
            print(f"{"CADASTRO DE PRODUTO: ":^50}")
            print("-"*50)
            print()
            time.sleep(0.5)
            nome_prod = str(input("Qual produto deseja cadastrar? ")).capitalize()
            while nome_prod.strip() == "": #Bloco para validar a entrada do nome do produto sem espaço ou vazio
                print()
                print("x"*50)
                print(f"{"Nome invalido, tente novamente ":^50}")
                print("x"*50)
                print()
                nome_prod = str(input("Qual produto deseja cadastrar? ")).capitalize()
            produto.append(nome_prod)
            print()
            time.sleep(0.5)
            quant = int(input(f"Quantas unidades de {nome_prod} deseja cadastrar? "))
            quant_prod.append(quant)
            print()
            time.sleep(0.5)
            print("<"*50)
            print(f"{f"{nome_prod.upper()} Cadastrado com sucesso ":^50}")
            print("<"*50)
            print()
            time.sleep(0.5)
            print("Deseja:")
            resp = input("[0] Voltar ao menu ""\n[1] Cadastrar outro produto ")
            while resp != "0" and resp != "1":
                print()
                print("x"*50)
                print(f"{"Opção inválida, tente novamente ":^50}")
                print("x"*50)
                print()
                resp = input("[0] Voltar ao menu\n[1] Cadastrar outro produto ")
                if resp == "0": 
                    break
            if resp == "0": 
                break         
    elif opcao == 2:
        print("-"*50)
        print(f"{"PRODUTOS CADASTRADOS:":^50}")
        print("-"*50)
        time.sleep(0.5)
        print(f"{'ID':<10}{'Produto':<20}{'Quant.':>10}")
        print()
        
        for i in range(len(produto)):
            print(f"{i:<10}{produto[i]:<20}{quant_prod[i]:>10}")
        print("-"*50)
        time.sleep(0.5)
        print("Deseja:")
        resp = input("[0] Voltar ao menu ")
        while resp != "0":
            print()
            print("x"*50)
            print(f"{"Opção inválida, tente novamente ":^50}")
            print("x"*50)
            print()
            resp = input("[0] Voltar ao menu ")
            if resp == "0": 
                break
    elif opcao == 3:
        while True:
            time.sleep(0.5)
            print("-"*50)
            print(f"{"ALTERAÇÃO DE PRODUTO:":^50}")
            print("-"*50)
            print(f"{'ID':<10}{'Produto':<20}{'Quant.':>10}")
            print()
            for i in range(len(produto)):
                print(f"{i:<10}{produto[i]:<20}{quant_prod[i]:>10}")
            print("-"*50)
            print()
            time.sleep(0.5)
            alterar=int(input("Qual produto deseja alterar [ID]:  "))
            print()
            time.sleep(0.5)
            posicao = produto.index(produto[alterar])
            time.sleep(0.5)
            print("O que deseja alterar? ")
            print()
            time.sleep(0.5)
            print("[0] Nome ")
            time.sleep(0.5)
            print("[1] Quantidade ")
            print()
            time.sleep(0.5)
            opcao_alterar = int(input("Digite a opção a ser alterada: "))       
            if alterar == posicao:
                if opcao_alterar == 0:
                    time.sleep(0.5)
                    print()
                    produto[posicao] = str(input("Digite o novo nome: "))
                    print()
                    time.sleep(0.5)
                    print("="*50)
                    print(f"{"Nome alterado com sucesso ":^50}")
                    print("="*50)
                    time.sleep(0.5)
                    print()      
                if opcao_alterar == 1:
                    time.sleep(0.5)
                    print()
                    quant_prod[posicao] = int(input("Digite a nova quantidade: "))
                    print()
                    time.sleep(0.5)
                    print("="*50)
                    print(f"{"Quantidade alterada com sucesso ":^50}")
                    print("="*50)
                    time.sleep(0.5)
                    print()
            print("Deseja:")
            resp = input("[0] Voltar ao menu ""\n[1] Alterar outro produto ")
            while resp != "0" and resp != "1":
                    print()
                    print("x"*50)
                    print(f"{"Opção inválida, tente novamente ":^50}")
                    print("x"*50)
                    print()
                    resp = input("[0] Voltar ao menu\n[1] Alterar outro produto ")
                    if resp == "0": 
                        break
            if resp == "0": 
                break        
    elif opcao == 4:
        print("-"*50)
        print(f"{"APAGAR PRODUTO:":^50}")
        print("-"*50)
        print(f"{'ID':<10}{'Produto':<20}{'Quant.':>10}")
        print()

        for i in range(len(produto)):
            print(f"{i:<10}{produto[i]:<20}{quant_prod[i]:>10}")
        print()

        remover = int(input("Qual produto deseja remover[ID]: "))    
        del produto[remover]
    elif opcao == 0:
        break   
            
        
 