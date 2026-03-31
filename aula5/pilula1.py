def validarSenha(senha):
    if len(senha) < 8:
        return 'Senha invalida, muito curta'
    
    temNumero = False
    temMaiuscula = False
    
    for c in senha:
        if c == ' ':
            return 'Senha invalida, não pode conter espaços'
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
            
    if not temNumero:
        return 'Senha invalida, não tem numeros'
    
    if not temMaiuscula:
        return 'Senha invalida, não tem maiuscula'
    
    return 'Senha valida'
#main
senha = input('Digite sua senha: ')
print(validarSenha(senha))