print('Programa para calcucular REAL para DÓLAR')
print()

real = float(input('Digite um valor em reais: '))

dolar = float(input('Digite o valor do DÓLAR atual (em REAIS): '))

valor_convert = real/dolar
print('R$ {0:.2f} valem: U$ {1:.2f}'.format(real,valor_convert))