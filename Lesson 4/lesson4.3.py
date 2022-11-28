 #spisok = [9, 10, 5, 6, 8, 9, 10, 5, 9, 10, 6]
#slovar = {}
#for x in spisok:
#    if slovar.get(x, None):
#        slovar[x] += 1
 #   else:
 #       slovar[x] = 1
#print(slovar)



def slovar(list):
    slovar = {}
    for x in list:
        if x in slovar:
            slovar[x] += 1
        else:
            slovar[x]=1
    return slovar

u = 7, 7, 7, 9, 8, 8, 9
print(slovar(u))