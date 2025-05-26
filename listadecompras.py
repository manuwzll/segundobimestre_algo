compras = []
while True:
    
    print("o que deseja fazer?")
    print("1-colocar item na lista")
    print("2-remover coisa da lista")
    print("3-ver o que tem na lista")
    print("4-finalizar o programa")
    
    opcao = input ("Escolha um número")

    if opcao == "1":
            item = input(f"escreva o que quer colocar")
            compras.append(item)
            print("item,foi colocado na lista com sucesso!")

    elif opcao ==  "2":
            item = input("o que deseja remover?")
            for i in compras:
                if item == i:
                    compras.remove(item)
                    print(f"O item {item} foi removido com sucesso!")
            else:
                print("este item não está na lista")

    elif opcao =="3":
        print ("Estes itens estão na lista:")
        print(compras)
        
    elif opcao == "4":   
        print("programa finalizado")
        