"""
Exercício FP1: Verificar se um número é positivo, negativo ou zero.
Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
Dica: Usa as estruturas condicionais if, elif e else.


"""

Num = int(input("Insira Um Numero Inteiro: "))
if Num == 0:
  print("O Seu Numero é 0")
elif Num > 0:
  print(f"{Num} é Positivo")
else:
  print(f"{Num} é um numero Negativo")





"""
Exercício FP2: Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %

"""

Num = int(input("Insira Um Numero Inteiro: "))
Resultado = Num % 2

if Resultado == 0:
  print(f"{Num} é par")
else:
  print(f"{Num} é impar")

"""
Exercício FP3: Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:

Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"


"""



Nota_Final = float(input("insira um valor: "))

if Nota_Final < 10.0:
  print(f"A Sua Nota é {Nota_Final}, Estás Reprovado!")
elif Nota_Final >= 10.0 and Nota_Final <= 14.0:
  print(f"A Sua Nota é {Nota_Final}, Suficiente!")
elif Nota_Final > 14.0 and Nota_Final <= 17:
  print(f"A Sua Nota é {Nota_Final}, Bom!")
elif Nota_Final > 17:
  print(f"A Sua Nota é {Nota_Final}, Fantástico!")



"""
[IGNORAR]
Exercício FP4: Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

Fórmulas:

Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15

[IGNORAR]

"""
import math
import random


Question = input("Quer Converter Fahrenheit, Kelvin ou Ambos: ")
if (Question == "Kelvin") or (Question == "kelvin"):
  Num_Cel = float(input("Insira a tempratura em Graus Celsius: "))
  Cel_To_Kel = Num_Cel + 273.15
  print(f"{Num_Cel} Graus Celsius São {Cel_To_Kel:.2f} Graus Kelvin")
elif (Question == "Fahrenheit") or (Question == "faherenheit"):
  Num_Cel = float(input("Insira a tempratura em Graus Celsius: "))
  Cel_To_Fahr = (Num_Cel * (9/5)) + 32
  print(f"{Num_Cel} Graus Celsius valem {Cel_To_Fahr:.2f} Libras")
elif (Question == "Ambos") or (Question == "ambos"):
  Num_Cel = float(input("Insira a tempratura em Graus Celsius: "))
  Cel_To_Fahr = (Num_Cel * (9/5)) + 32
  Cel_To_Kel = Num_Cel + 273.15
  print(f"{Num_Cel} Graus Celsius correspondem a {Cel_To_Fahr:.2f} Graus Fahrenheit e {Cel_To_Kel:.2f} Graus Kelvin ")



"""
Exercício FP4: Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

Fórmulas:

Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15



"""
import math
import random

Num_Cel = float(input("Insira a tempratura em Graus Celsius: "))
Cel_To_Fahr = (Num_Cel * (9/5)) + 32
Cel_To_Kel = Num_Cel + 273.15

Question = input("Quer Converter Fahrenheit (F), Kelvin (K) ou Ambos (A): ")

if (Question == "Kelvin") or (Question == "kelvin") or (Question == "k") or (Question == "K"):
  print(f"{Num_Cel} Graus Celsius correspondem {Cel_To_Kel:.2f} Graus Kelvin")
elif (Question == "Fahrenheit") or (Question == "fahrenheit") or (Question == "F") or (Question == "f"):
  print(f"{Num_Cel} Graus Celsius correspondem a {Cel_To_Fahr:.2f} Graus Fahrenheit")
elif (Question == "Ambos") or (Question == "ambos") or (Question == "a") or (Question == "A"):
  print(f"{Num_Cel} Graus Celsius correspondem a {Cel_To_Fahr:.2f} Graus Fahrenheit e {Cel_To_Kel:.2f} Graus Kelvin")

"""
FP-25
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.


Fórmulas:

Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15

Sal-100
x---10

sal*10
-------
100
Percent = Sal / (100 x 10)
"""
import math
import random

Sal = float(input("Insira os seu salário mensal: "))

if Sal <= 1000:
 print("Isento de Impostos")
elif (Sal >= 1001) and (Sal <= 2000):
  Percent = Sal * 0.1
  Impostos = Sal - Percent
  print(f"O Seu Salario é {Impostos:.2f}€")
elif Sal >2000:
  Percent = Sal * 0.2
  Impostos = Sal - Percent
  print(f"O Seu Salario é {Impostos:.2f}€")

""""Exercício FP6: Imprimir números de 1 a 10.
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10."""

for x in range(1,11):
  print(x)

"""Exercício FP7.
"""

SOMA = 0
CONTADOR = 1

while CONTADOR <= 100:
  SOMA += CONTADOR
  CONTADOR += 1
  print(F"A soma de 1 a 100 é: {SOMA}")



"""Exercício FP8: Contagem de vogais numa string.
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.
"""

texto = input("Escreva Algo")

if "a" or "e" in texto:
  print("Há Vogais no texto")


"""Exercício FP12: Gerar uma lista de números pares.
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.

"""
for x in range(0, 22, 2):
  print(x)

"""Exercício FP13: Inverter uma string.
Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.


"""
name = input("Escreva Uma Palavra:")
reversedname = name[::-1]
print(reversedname)

"""

Exercício FP14: Tabuada de multiplicação
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.

"""
num = int(input("Escreva Um Numero"))
i = 1
while i <= 10:
  print(i * num)
  i += 1

"""Exercício FP15: Fatorial de um número
Escreve um programa que utilize um ciclo while para calcular o fatorial de um número introduzido pelo utilizador. O fatorial de um número n (n!) é o produto de todos os números inteiros positivos até n.



"""
import math
num = int(input("Write a Number: "))
print(math.factorial(num))

"""Exercício FP14: Tabuada de multiplicação
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.

RESOLUÇÃO COM FOR

"""
num = int(input("Escreva Um Numero"))
for i in range(0,11):
  print(i * num)

