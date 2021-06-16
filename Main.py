import numpy as np
import csv

from Spline import spline
from Langrage import langrage
import Plots as p


def trasa_niepelna(trasa, n):
    licznik = 0
    niepelna = [trasa[0]]

    for row in trasa[1:]:
        if licznik % n == 0:
            niepelna.append(row)
        licznik += 1

    return niepelna


def calculate_langrage(x,wielomian):
    y = 0
    n = 0
    wielomian.reverse()
    for coef in wielomian:
        y +=coef*x**n
        n +=1
    wielomian.reverse()
    return y
# a=[4,0,-3,1]
# y=calculate_langrage(-3.35,a)
# print(y)


#format a+b(x-x0)+c(x-x0)^2+d(x-x0)^3
def calculate_spline(x,wielomian,trasa):
    #kazdy wielomian 4 elementy: a b c d
    xsm, w = find_poly(x,trasa)
    w=w-1
    y=0
    y+=wielomian[w*4]
    y+=wielomian[w*4+1]*(x-xsm)
    y+=wielomian[w*4+2]*(x-xsm)**2
    y+=wielomian[w*4+3]*(x-xsm)**3
    return y


def find_poly(x, trasa):#trasa zaczyna sie od 0
    xsm=0#najblizszy wezel mniejszy od x
    w=0#ktory wielomian

    for row in trasa[1:-1]:
        if row[0]<x:
            xsm=row[0]
            w=w+1
    if w==0:
        w=1
    return xsm,w


#czytanie trasy 1 z pliku
trasa = csv.reader(open("trasy/1(,)/SpacerniakGdansk.csv", 'r'))
trasa = list(trasa)

for row in trasa[1:]:
     row[1] = float(row[1])#y wysokosc
     row[0] = float(row[0])#x

#Lagrange
# yl=[]
# xl=[]
# tr=trasa_niepelna(trasa, 25)
# wielomian=langrage(tr)
#
# for row in trasa[1:]:
#     yl.append(calculate_langrage(row[0], wielomian))
#     xl.append(row[0])
#
# p.plots1(trasa[1:])
#p.plots2(xl,yl,tr[1:])

#spline
tr=trasa_niepelna(trasa, 10)
wielomian=spline(tr)
ys=[]
xs=[]
for row in trasa[1:]:
    ys.append(calculate_spline(row[0], wielomian,tr))
    xs.append(row[0])
#p.plots1(tr[1:])
p.plots2(xs,ys,tr[1:])



# dane do sprawdzenia poprawnosci
# (z przykladow z wykladu)

#format ax^n+b^n-1+...zx^0
# print("langrage")
# wielomian=langrage([["0","a"],[0,4],[2,1],[3,6],[4,1]])
# print(wielomian)

#format a+b(x-x0)+c(x-x0)^2+d(x-x0)^3
# print("spline")
# wielomian=spline([["0","a"],[1,6],[3,-2],[5,4]])
# print(wielomian)










