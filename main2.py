from math import *

def exemple2():
    monnom="khalaldi"
    monprenom="redouane"
    monnom1="elkaissouni"
    monnom2="jihad"
    age=30
    age2=29.5
    pays="FRANCE"
    pays2="MAROC"

    resulta = "{0} {1} et {2} {3} ont {4} et {5}". format(monnom,monprenom,monnom2,monnom1,age,age2)
    resultat = "{0} {1} et {2} {4} ont {3} et {5}". format(monnom,monprenom,monnom2,monnom1,age,age2)
    resultatt = "{0} {1} et {2} {4} ont {3} et {5}". format(monnom,monprenom,monnom1,monnom2,age,age2)
    resultattm = "{0} {1} et {2} {4} ont {3} et {5}". format(monnom,monprenom,monnom1,monnom2,age,age2)

    print(resulta)
    print(resultat)
    print(resultatt)
    print(resultattm.upper())

    #print(monnom[5])
    print(monnom[:3])
    print(monnom[3:])
    print(monnom[2:4])
    #print(monnom[2:3])
    #print(monnom[2:5])
    #print(monnom[2:5:3])
    #print(monnom[2::4])
    print(monnom[-2:4])
    print(monnom.find("i"))

    i="da"*(5//2)
    print(i)
    j=monnom+"\t"+monprenom
    print(j)
    print(monnom,"\t",monprenom)

    x=1
    x=x+1
    x+=1
    print(x)
    x-=1

    print(x)


    a,b=4,3
    y=3*a+2*b
    x=z=6
    print("a={0},b={1},x={2},y={3},z={4}".format(a,b,x,y,z))
    print("a={},b={},x={},y={},z={}".format(a,b,x,y,z))
    resultattm = "{} {} et {} {} ont {} et {}".format(monnom, monprenom, monnom1, monnom2, age, age2)
    print(resultattm)

    liste=[j,]

    print(asin(0.4))


exemple2()

def exemple3 ():
    x=2
    y=2.0
    z="2"
    print(type(x))
    print(type(y))
    t=True
    calcul=int("3")+float("3.2")
    calcull=int("jiji")+float("3.2")
    print(calcull)

    print(calcul)









