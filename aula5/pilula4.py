def calcularResutado():
    n1 = float(input('Nota 1: ')) 
    n2 = float(input('Nota 2: ')) 
    n3 = float(input('Nota 3: ')) 
    media = (n1+n2+n3)/3
    if media < 6:
        rec = float(input('Recuoeração '))
        media = (media + rec) / 2
        
    return media

m = calcularResutado()
if m >= 6:
    print('Aprovado')
else:
    print()