Aparelho = str(input("Qual aparelho você deseja usar para o cálculo "))
potencia = float(input("Qual a potência do aparelho em wats? "))
tm = float(input("Qual o tempo médio que seu aparelho é usado diariamente em horas? "))

consumomensal = (potencia * tm * 30)/100
print("O aparelho",Aparelho,"tem  um consumo estimado de", consumomensal,"kwh por mês")