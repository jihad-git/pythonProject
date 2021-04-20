##############################################
#Module : ModuleFormation01
##############################################

from ModuleFormation02 import *

def doubler(x):
    return 2*x



def calculminmax(a,b) :
     if a < b :
        return a,b
     else :
        return b,a

def cube(x) :
     return x*x*x

def addition(x,y) :
    return x*y



def sommeEntiers(n) :
    somme=0
    for i in range(0,n+1):
        somme = somme+i
    return somme








