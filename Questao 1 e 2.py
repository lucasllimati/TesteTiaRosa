# Questão 01: Calculadora de adição e subtração

def CalculadoraAdicaoSubtracao (numero, outronumero, operacao):
  # Observações
    # N1 = numero
    # N2 = outronumero
    # Sinal = operacao


  # Se operacao tiver o sinal '+', será feito a soma do N1 + N2
  if operacao == '+':
    return numero + outronumero

  # Se operacao tiver o sinal '-', será feito a soma do N1 - N2
  elif operacao == '-':
    return numero + outronumero

  # Se operacao tiver o sinal diferente de '+' ou '-', irá retornar 0
    return 0

#############################################################################

# Questão 02: Multiplicação da lista por 3

def tripleTheChances (chances):
  # Observações
    # chances = Lista com vários número
      # ex: chances = [2, 3, 5, 8, 10]

  # Para cada item da lista ele irá multiplicar por 3
  res = [x * 3 for x in chances]

# Funcionalidade
  # x = 1 (Irá multiplicar 2 * 3 = 6)
  # x = 2 (Irá multiplicar 3 * 3 = 9)
  # x = 3 (Irá multiplicar 5 * 3 = 15)
  # x = 4 (Irá multiplicar 8 * 3 = 24)
  # x = 5 (Irá multiplicar 10 * 3 = 30)


  # res = Nova lista que possui o resultado da lista 'chances' sendo multiplicada por 3
  # res = [6, 9, 15, 24, 30]

#############################################################################


