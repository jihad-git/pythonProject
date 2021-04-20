

def tripler(x):
    return 3*x

def conversionS(h,m,s) :
    s = h*3600+m*60+s
    return s

def multiplicationliste(list0):
    p=1
    for i in list0:
        p*=list0[i]
    return p

def liste(ancienneliste) :
    nouvelleliste=[ ]
    for a in ancienneliste :
        if a not in nouvelleliste:
            nouvelleliste.append(a)
    return nouvelleliste

def estAnneeBissextile(annee) :

    return (( (annee % 400 == 0) ) or \
             ( (annee % 4 == 0) ) and ((annee % 100 != 0 )))

def estAnneeBissextile(annee) :
    estMultipleDe4 = ((annee % 4)==0)
    estMultipleDe400 = ((annee %400)==0)
    estMultipleDe100 = ((annee % 100)==0)

    return (estMultipleDe400) or \
             ( estMultipleDe4  and  not estMultipleDe100)
class Utilisateur:
    statut = "Inscrit"
    age = 30

    def setNom(self,n):
            self.nom = n

class Utilisateur :
    anciennete = 0

    def __init__(self,nom, age):
            self.user_name = nom
            self.user_age = age

    def getNom(self):
            print("salut, je suis ", self.user_name)

class Client(Utilisateur):
    is_client = True
    anciennete = 10

    def __init__(self, nom, age, mail, numclient):
            self.user_name = nom
            self.user_age = age
            self.user_mail = mail
            self.user_numclient = numclient

    def getNom(self):
            print("je suis", self.user_name, ".mon mail est : ",self.user_mail)







