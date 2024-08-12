def calculadora(n1, n2, operacao):
    if operacao == '1':
        return n1 + n2
    elif operacao == '2':
        return n1 - n2
    elif operacao == '3':
        return n1 * n2
    elif operacao == '4':
        return round(n1 / n2, 2)
    else:
        return 0

opcao = input('Escolha qual operação deseja realizar:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n')

primeiroNumero = float(input('Digite o primeiro número: '))
segundoNumero = float(input('Digite o segundo número: '))

print(calculadora(primeiroNumero, segundoNumero, opcao))
