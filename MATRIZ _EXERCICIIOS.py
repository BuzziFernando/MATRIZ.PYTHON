mat = [[0]*3 for i in range(5)]

# cria matriz
for lin in range(4):
    for col in range(3):
        print("arm:", lin+1,"Prod", col+1)
        print(" digite  a quantidade")
        mat[lin][col]= float(input())
# aqui para na linha 4 e anda na coluna
for col in range(3):
    print("prod",col+1)
    print("digite o valor")
    mat[4][col] = float(input())

# aqui so
totalarma = 0
for lin in range(4):
    for col in range(3):
        totalarma += mat[lin][col]
    print("arm",lin ,"valor total e", totalarma)
    totalarma = 0
# LOGICA DO MAIOR
omaior = 0
armazemmaior = 0
for lin in range(4):
    if omaior < mat [lin][1]:
        omaior = mat [lin][1]
        armazemmaior = lin+1
print(" a maior qtdade e",armazemmaior\
      "tem a maior quantidade ",omaior)
# AQUI LOGICA DO MENOR
totalam = 0
oarmazemenor= 0
for lin in range(4):
    for col in range(3):
        totalarma+= mat[lin][col]
    if lin==0:
        omenor = totalam
    else:
        if omenor>totalam:
            omenor=totalarma
            omenor =lin +1
    totalam = 0
print(" o armazem ", oarmazemenor)
print("posui o menor quantidade de ",omenor)

# AQUI MULTIPLICA!!! CUSTO TOTAL DE CADA PRODUTO
somaquantidade = 0
for col in range(3):
    for lin in range(4):
        somaquantidade+= mat[lin][col]
    custototal = somaquantidade * mat[4][col]
    print("produto ",col,"custo total",custototal)
    somaquantidade = 0

#AUQUI SOMA AS
somacustoarma = 0
for lin in range(4):
    for col in range(3):
        somacustoarma=somacustoarma+(mat[lin][col] * mat[4][col])
    print("armazem", lin+1,"custo total de",somacustoarma)
    somacustoarma = 0




