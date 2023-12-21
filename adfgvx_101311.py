def trouver_nombre(diviseurs):
    n = 1
    while True:
        compteur_diviseurs = 0
        diviseurs_liste = []
        for i in range(1, n + 1):
            if n % i == 0:
                compteur_diviseurs += 1
                diviseurs_liste.append(i)
        if compteur_diviseurs == diviseurs:
            return n, diviseurs_liste,compteur_diviseurs
        n += 1

# Test de la fonction avec 16 diviseurs
nombre, diviseurs,compt = trouver_nombre(81)
print("Le nombre recherché est :", nombre)
print("Les diviseurs de", nombre, "sont :", diviseurs)
print("Les nombre de fois", compt)

print('__________________________________________________________________________')
count=0
for revise in range(2,nombre+1,2):
    if nombre%revise==0:
        count+=1
        print(revise)
print(count)

        