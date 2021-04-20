

# a = 0
# a=eval(input("donner un chiffre entre 1 et 3"))
#
# while (a>3 or a<1):
#
#     print("mauvaise reponse, re-essayer")
#     a = eval(input("donner un chiffre entre 1 et 3"))
#
# print(a)

# Rédiger un algorithme demandant à l'utilisateur un nombre compris entre 10 et 20, jusqu’à ce que la réponse
# convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! », et
# inversement, « Plus grand ! » si le nombre est inférieur à 10.

# n=0
# while n<10 or n>20 :
#     n=eval(input("saisir un nombre entre 10 et 20:"))
#     if n<10 :
#         print("plus grand")
#     else:
#         if n>20 :
#             print("plus petit")

# Rédiger un algorithme demandant à l'utilisateur un nombre de départ, et qui ensuite affiche les dix nombres
# suivants. Par exemple, si l'utilisateur entre le nombre 17, le programme affichera les nombres de
# 18 à 27.


# n=eval(input("saisir un nombre :"))
# for i in range(1,11):
#     print(n+i)

# stop = n+10
#
# while (n<stop):
#     n = n+1
#     print(n)


# Rédiger un algorithme qui demandant à l'utilisateur un nombre de départ, et qui calcule la somme des entiers
# jusqu’à ce nombre. Par exemple, si l’on entre 4, le programme doit calculer :
# 1 + 2 + 3 + 4 = 10


# n = eval(input("donner un nombre:"))
# s=0
#
# for i in range(1,n+1):
#     s = s+i
#
# print(s)


# n=eval(input("saisir un nombre:"))
# f=1
# for i in range(1,n):
#
#     f=i*f
# age=30
# print("mineur") if age <20 else print("majeur")
#
# if(age>20):
#     print("mineur")
# else:
#     print("majeur")

# a,b=eval(input("1er nb")),eval(input("2éme nb"))
# print("min",min(a,b))
# print("max :",max(a,b))

# n=eval(input("saisir un nb"))
# for i in range(1,11) :
#     print(i,"*",n,"=",i*n)


# n = eval(input("donner chi baraka fi sabil llah: "))
#
# i=0
# while (i<n-1):
#     print("iteration ", i)
#     i=i+1
#
# print(i)

# Constituez une liste semaine contenant les 7 jours de la semaine.
#semaine =["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
# 1. À partir de cette liste, comment récupérez-vous seulement les 5 premiers jours de la semaine d’une part, et ceux du
# week-end d’autre part ? Utilisez pour cela l’indiçage.
#print(semaine[0:5])
#print(semaine[5:7])
# 2. Cherchez un autre moyen pour arriver au même résultat (en utilisant un autre indiçage).
#print(semaine[-7:-2])
#print(semaine[-2:])
# 3. Trouvez deux manières pour accéder au dernier jour de la semaine.
#print(semaine[-1])
#print(semaine[6])
# 4. Inversez les jours de la semaine en une commande.
#print(semaine[-1:-8:-1])

#Affichez la table de multiplication par 9 en une seule commande avec les instructions range() et list().
print(list(range(9,82,9)))
#Répondez à la question suivante en une seule commande. Combien y a-t-il de nombres pairs dans l’intervalle [2, 10000] inclus ?

print(len(list(range(2,10001,2))))
a=0
for i in range(2,10001) :
    if i%2==0 :
        a+=1
print(a)