import matplotlib.pyplot as plt

def plots1(punkty):
    x=[]
    y=[]
    for p in punkty:
        x.append(p[0])
        y.append(p[1])

    plt.title('SpacerniakGdansk.csv')
    plt.ylabel('Wysokosc')
    plt.xlabel('Odleglosc')
    plt.plot(x, y,marker=',')
    plt.savefig('SpacerniakGdansk-profil.png')
    plt.show()


def plots2(x,y,punktypob):
    xp=[]
    yp=[]
    for p in punktypob:
        xp.append(p[0])
        yp.append(p[1])

    plt.title('SpacerniakGdansk,co 10 punkt')
    plt.ylabel('Wysokosc[m]')
    plt.xlabel('Odleglosc[m]')
    plt.plot(x, y,label='Interpolowany profil')
    plt.plot(xp, yp,'go',label='Wezly')
    plt.legend()
    #plt.savefig('SpacerniakGdansk_spline_10.png')
    plt.show()
