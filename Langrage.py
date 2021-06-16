def mianownik_phi_Langrage(trasa):
    mian = []
    xn = []

    for row in trasa[1:]:
        xn.append(row[0])  # lista probek

    for i in range(len(xn)):
        if i == 0:  # mianownik =x1-x2 lub xi-x1
            mianownik = xn[0] - xn[1]
            for j in range(2, len(xn)):
                if i != j:
                    mianownik *= (xn[i] - xn[j])
        else:
            mianownik = xn[i] - xn[0]
            for j in range(1, len(xn)):
                if i != j:
                    mianownik *= (xn[i] - xn[j])

        mian.append(mianownik)  # obliczony mianownik do listy phi

    return mian


def licznik_phi_Langrage(trasa):
    licz = []
    xn = []
    licznik = []
    for row in trasa[1:]:
        xn.append(row[0])  # lista probek

    for i in range(len(xn)):
        if i == 0:
            licznik =[1, -xn[1]]
            for j in range(2,len(xn)):
                if i != j:
                    licznik = pol_multiply(licznik, [1, -xn[j]])
        else:
            licznik = [1, -xn[0]]
            for j in range(1,len(xn)):
                if i != j:
                    licznik = pol_multiply(licznik, [1, -xn[j]])
        licz.append(licznik)  # lista wielomanow

    return licz


def langrage(trasa):
    yn = []
    wynik =[]

    for row in trasa[1:]:
        yn.append(row[1])  # lista wysokosci

    mianownik = mianownik_phi_Langrage(trasa)
    licznik = licznik_phi_Langrage(trasa)


    #dzielenie licznika przez mianownik
    #budujemy wielomian w liczniku oprócz sumowania wielomianow phi
    for i in range(len(trasa)-1):
        for j in range(len(trasa) - 1):
            licznik[i][j] = licznik[i][j]/mianownik[i]
            licznik[i][j] *= yn[i]   #mnozymy przez wartosc funkcji

    for i in range(len(trasa)-1):
        tmp = 0
        for j in range(len(trasa) - 1):
            tmp += licznik[j][i] #sumujemy odpowiednie wspolczynniki
        wynik.append(tmp)

    return wynik


def pol_multiply(p1, p2):
    p1.reverse()
    p2.reverse()
    res = [0]*(len(p1)+len(p2)-1)
    for x1, i in enumerate(p1):
        for x2, j in enumerate(p2):
            res[x1+x2] += i*j
    res.reverse()
    return res
