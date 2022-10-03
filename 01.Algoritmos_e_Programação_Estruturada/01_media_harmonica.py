#Calcule a média harmonica dos seguintes números: 3.6, 8.9 e 10.

mediaHarmonica = 3/((1/3.6)+(1/8.9)+(1/10))
print(mediaHarmonica)

#Modifique o exmplo anterior para calcular a média harmônica amortizada dos mesmos números: 3.6, 8.9 e 10. 
# Utilize X = 4 como fator de amortização

mediaHarmonicaATD = (3/((1/(3.6-4))+(1/(8.9-4))+(1/(10-4)))) - 4
print(mediaHarmonicaATD)

