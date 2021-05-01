#Conversor de taxas de juros
#Estudo de Python - AllRox 2021

import math
ans=True
while ans:
    print("""
    [1] Juros a.a. para a.m.
    [2] Juros a.m. para a.a.
    [3] Juros a.m. para a.d.
    [4] Juros a.d. para a.m.
    [0] Para encerrar.
    """)

    ans=input("Informe o número da conversão desejada: ")

    if ans=="1":
        #Conversão a.a > a.m.
        print("Conversão de juros a.a. para a.m.",end="\n")
        print("---------------------------------------\n")
        tx = float(input("Informe a taxa anual: "))
        tx /= 100
        conv = math.pow((1+tx),(1/12))-1
        print("A taxa a.a. informada equivale a ",round((conv*100),2),"% ao mês", sep="", end="\n\n")
    elif ans =="2":
        #Conversão a.m. > a.a.
        print("Conversão de juros a.m. para a.a.",end="\n")
        print("---------------------------------------\n")
        tx = float(input("Informe a taxa ao mês: "))
        tx /= 100
        conv = (math.pow((1+tx),12)-1)*100
        print("A taxa a.m. informada equivale a ",round((conv),2),"% ao ano", sep="", end="\n\n")
    elif ans =="3":
        #Conversão a.m. > a.d.
        print("Conversão de juros a.m. para a.d.",end="\n")
        print("---------------------------------------\n")
        tx = float(input("Informe a taxa ao mês: "))
        tx /= 100
        conv = math.pow((1+tx),(1/30))-1
        print("A taxa a.m. informada equivale a ",round((conv*100),2),"% ao dia", sep="", end="\n\n")

    elif ans=="4":
        #Conversão a.d. > a.m.
        print("Conversão de juros a.d. para a.m.",end="\n")
        print("---------------------------------------\n")
        tx = float(input("Informe a taxa ao dia: "))
        tx /= 100
        conv = (math.pow((1+tx),30)-1)*100
        print("A taxa a.d. informada equivale a ",round((conv),2),"% ao mês", sep="", end="\n\n")
    elif ans=="0":
        #Comando para encerrar
        quit()
    else:
        print("Escolha inválida digite o número da opção desejada.")