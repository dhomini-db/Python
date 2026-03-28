a1 = float (input("digite sua 1° nota:"))
a2 = float (input("digite sua 2° nota:"))
a3 = float (input("digite sua 3° nota:"))
soma = (a1 + a2 + a3) / 3
if (soma >= 7.0):
    print(f" {soma:.2f} Parabéns! Sua média é alta.")
elif (soma >= 5.0 ):
    print(f" {soma:.2f} Sua média é razoável.")
else:
    print (f" {soma:.2f} Sua média é baixa. É uma boa oportunidade para melhorar.")