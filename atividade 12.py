# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.
# solicitar as notas do usuario
nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("digite a terceira nota:"))
media = (nota1 + nota2 + nota3)/ 3
if media >= 7.0:
    print("aprovado")
else:
    print("reprovado")
