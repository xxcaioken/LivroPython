#aprovado ou não
mediaParaPassar = 7
nota1 = float(input("insira sua primeira nota de matematica:"))
nota2 = float(input("insira sua segunda nota de matematica:"))
nota3 = float(input("insira sua terceira nota de matematica:"))
nota1b = float(input("insira sua primeira nota de LP:"))
nota2b = float(input("insira sua segunda nota de LP:"))
nota3b = float(input("insira sua terceira nota de LP:"))
nota1c = float(input("insira sua primeira nota de SI:"))
nota2c = float(input("insira sua segunda nota de SI:"))
nota3c = float(input("insira sua terceira nota de SI:"))
calculoDaMedia = ((nota3+nota2+nota1)/3)
calculoDaMedia1 = ((nota3b+nota2b+nota1b)/3)
calculoDaMedia2= ((nota3c+nota2c+nota1c)/3)
mediareal1 = str(calculoDaMedia)
mediareal2 = str(calculoDaMedia1)
mediareal3 = str(calculoDaMedia2)

if (calculoDaMedia>mediaParaPassar and calculoDaMedia2>mediaParaPassar and calculoDaMedia1>mediaParaPassar):
    print("parabéns você passou com media: ", mediareal1,"em matematica","e com media: "+mediareal2," em LP ","e com media: "+mediareal3," em SI")
else:print("voce rodou com media: ", mediareal1,"em matematica","e com media: "+mediareal2," em LP ","e com media: "+mediareal3," em SI")