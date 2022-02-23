nome = input("Digite seu nome:")
nomeLimpo = input("o nome: "+nome+" está limpo?   [True] [False]")
idade =int(input("insira sua idade:"))
cpf= input("insira seu cpf")
idadereal = float(idade)
nomeLimpo1 =bool(nomeLimpo)
#print(nomeLimpo1)
#print(type(nomeLimpo1))
salario= float(input("insira o valor do seu sálario mensal:"))

if( nomeLimpo and idade >18 and cpf!=0 and salario >= 5000):
    print("deu boa")
else:
    print("não sera possível fazer o empréstimo pois você ou não tem o perfil minimo ou por falta de informação")