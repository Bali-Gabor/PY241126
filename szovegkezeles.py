# 4/1 feladat 

# nev='Bali Gábor'
# for betu in nev: print(betu,end=" ")


# 4/2 feladat

# nev='Bali Gábor'
# for c in nev: print(c)


# 4/3 feladat

# nev='Bali Gábor'
# for x in range(len(nev)):
#     print(x*'  '+nev[x])


# 4/4 feladat

# szo=input('Adj meg egy szót!   ')
# for _ in range(len(szo)+2): print('*',end="")
# print(f'\n*{szo}*')
# for _ in range(len(szo)+2): print('*', end="")


# 4/5 feladat

# szo=input('Adj meg egy szót!  ')
# ----------------------------------
# for i in range(len(szo)-1,-1,-1):
#     print(szo[i],end="")
# ----------------------------------
# for x in range(len(szo)):
#     print(szo[len(szo)-x-1],end="")
# ----------------------------------
# print(szo[::-1])
# ----------------------------------
# for x in range(-1,-len(szo)-1,-1):
#     print(szo[x])
# ----------------------------------
# for x in range(len(szo)):
#     print(szo[-(x+1)])
# ----------------------------------
# print(szo[-1:-5:-1])


# 4/6 feladat

# szoveg=input('Adj meg egy szöveget!   ')
# darab=0
# for betu in szoveg.lower():
#     if betu=='e': darab+=1
# print(f'A szövegben {darab} e betű van.')


# 4/7 feladat

# szoveg=input('Adj meg egy szöveget!  ')
# ------------------------------------------
# darab=0
# for c in szoveg:
#     if c==' ': darab+=1
# print(f'A szövegben {darab} szóköz van.')
# ------------------------------------------
# darab=0
# for szo in szoveg:
#     if szo == ' ': darab+=1
# print(f'A szövegben{darab+1} szó van.')
#-------------------------------------------
# print(f'a szövegben: {len(szoveg.split())} szó van.')


# 4/8 feladat

# mondat=input('Írj be egy mondatot!  ')
# match mondat[-1]:
#     case '!': print('A mondat felkiáltó.')
#     case '?': print('A mondat kérdő.')
#     case '.': print('A mondat kijelentő.')


# 4/9 feladat

# szoveg=input('Írjon be egy szöveget.')
# print(szoveg.lower())
# print(szoveg.upper())


# 4/10 feladat

# szo=input('Írj be egy szót!  ')
# print(szo.capitalize())


# 4/11/12 feladat

# szo=input('Adj meg egy szót!  ')
# if 'j' in szo.lower(): print('Van benne j betű.')
# else: print('Nincs benne j betű.')
# ------------------------------------
# if 'ly' in sszo.lower(): print('Van benne ly')
# else: print('Nincs benne ly')


# 4/13 feladat

# ertek='aáeéiíoóöőuúüű'
# darab=0
# szo=input('Adj meg egy szót!  ')
# for c in szo:
#     if c in ertek:
#         darab+=1
# print(f'A szóban {darab} magánhangzó van.')


# 4/14 feladat

# ekezetes='áéíóöőúüűÁÉÍÓÖŐÚÜŰ'
# ekezet_nelkuli='aeiooouuuAEIOOOUUU'
# szoveg=input('Adj meg egy szöveget!  ')
# uj_szoveg=''
# for c in szoveg:
#     if c not in ekezetes:
#         uj_szoveg+=c
#     else:
#         i=ekezetes.index(c)
#         uj_szoveg+=ekezet_nelkuli[i]
# print(uj_szoveg)


# 4/15 feladat

# szoveg=input('Adj meg egy szöveget!  ')
# for c in szoveg:
#     if c==' ': print('')
#     else: print(c,end='')


# 4/16 feladat

# szo=input('Adj meg egy szót!  ')
# lista= []
# for c in szo:
#     lista.append(c)
# lista.sort()
# print(''.join(lista))


# 4/17 feladat

# szo1=input('Adj meg egy szót!   ')
# szo2=input('Adj meg egy másik szót!   ')
# lista1=[]
# lista2=[]
# for c in szo1.lower(): lista1.append(c)
# for c in szo2.lower(): lista2.append(c)
# lista1.sort()
# lista2.sort()
# if lista1==lista2: print('Anagramma')
# else: print('Nem anagramma.')


# 4/18 feladat

# from random import randint

# karakterek='abcdefgh1234567890_!'
# jelszo=''
# for x in range(8):
#     jelszo += karakterek[randint(0,len(karakterek)-1)]
# print(jelszo)


# 4/19 feladat

# from random import randint

# vezeteknev=input('Adja meg a vezetéknevét!  ')
# keresztnev=input('Adja meg a keresztnevét!  ')
# felhasznalonev=vezeteknev[:2]+keresztnev[:2]
# print(felhasznalonev)
# felhasznalonev=vezeteknev[:2]+keresztnev[-2:]
# print(felhasznalonev)
# felhasznalonev=vezeteknev[:3]+str(randint(100,999))
# print(felhasznalonev)


# 4/20 feladat

# irszam=input('Adjon meg egy budapesti irányítószámot!  ')
# if irszam[0]!='1': print('Ez nem budapesti, vagy érvénytelen irányítószám!')
# else: print(f'Az irányítószám a {irszam[1:3]}. kerülethez tartozik.')


# 4/21 feladat

print('J, LY szavak gyakorlása.')
szavak=['bagoly','majom','folyó','király','máj','tej','fej','fáj','sirály','jel']
talalat=0
for szo in szavak:
    if 'j' in szo.lower():
        print(szo.replace('j', '_'))
        valasz=input('Szerinteg melyik j, ly hiányzik? Add meg a választ!   ')
        if valasz=='j':
            print('HELYES')
            talalat+=1
        else: print('HELYTELEN')
    if 'ly' in szo.lower():
        print(szo.replace('ly', '_'))
        valasz=input('Szerinted melyik j, ly hiányzik? Add meg a válaszod!   ')
        if valasz == 'ly':
            print('HELYES')
            talalat+=1
        else: print('HELYTELEN')
print(f'A találatok száma: {len(szavak)} / {talalat}')

# 4/22 feladat

# szoveg=input('Adj meg egy szöveget   ')
# lista=[]
# for c in szoveg:
#     if c not in lista: lista.append(c)
# print(f'A listában {len(lista)} külömböző karakter van.')
# print(','.join(lista))


# 4/23 feladat

# from time import sleep
# from os import system

# szo=input('Adj meg egy szót!')
# for x in range(len(szo)):
#     print(szo[x],end='')
#     sleep(1)
#     system('cls')


# 4/24 feladat

# Nem megoldható








