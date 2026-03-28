letra = input(" digite uma letra:").title()
vogais = "aeiouAEIOU"
if (letra in vogais ):
    print (f" {letra} é uma vogal")
elif (letra.isalpha() ):
    print(f" {letra} é uma consoante")
else :
    print(" não está nestes grupos. ")