def menu():
    while True:
        op = int(input('Menu\n 1 - Soma \n2 - Media \n3 - Sair\nEscolha: '))
        if op == 3:
            break
        n1 = float(input('N1:'))
        n2 = float(input('N2:'))
        if op == 1: print(f'Soma {n1} + {n2} = {n1+n2}')
        elif op == 2:
            print(f'Media de {n1} e {n2} = {(n1+n2)/2}')
        else:
            print('opção errada')

menu()