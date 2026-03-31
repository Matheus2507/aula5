def verificarCrescimento():
    anterior = float(input('leitura 1: '))
    crescente = True
    
    for i in range(4):
        atual = float(input(f'leitura {i+2}: '))
        if atual <= anterior:
            crescente = False
        anterior = atual
    return crescente

#main
if verificarCrescimento():
    print('Crescente')
else:
    print('Instavel')