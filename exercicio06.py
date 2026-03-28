litros = float(input("digite quantos litros:"))
print ("tipo de combustivel alcool ou gasolina")
tipo = input("digite o tipo do combustivel(A/G):").upper()

if (tipo == "A" and litros <= 20 ):
    conta = (litros * 4.98)
    conta = conta - (conta * 0.02)
    print(f"{conta:.1f}")
elif (tipo == "A" and litros > 20 ):
    conta = (litros * 4.98) 
    conta = conta - (conta * 0.05)
    print(f"{conta:.1f}")

elif (tipo == "G" and litros <= 20 ):
    conta = (litros * 5.57)
    conta = conta - (conta * 0.04)
    print(f"{conta:.1f}")
else:
    conta = (litros * 5.57)
    conta = conta - (conta * 0.06) 
    print(f"{conta:.1f}")