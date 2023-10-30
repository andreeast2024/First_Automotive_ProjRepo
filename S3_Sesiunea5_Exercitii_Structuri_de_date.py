# Structuri de date
#
# Exerciții - studiu în workshopul de weekend
#
# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.
#
# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
#    Găsește 2 variante să le unești într-o singură listă.
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

# Varianta 1
lista3 = lista1 + lista2 # am creat inca o variabila si am adunat cele 2 liste
print(lista3)

# Varianta 2
lista1.extend(lista2) # am extins prima lista cu a 2-a
print(lista1)

# 4.
# Sortează și afișează lista generată la exercițiul anterior.
# Sortează numărul 0 folosind o funcție.
# Afișaza iar lista.
lista3.sort() # .sort are rolul de a ordona elementele din lista
print(lista3)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# Lista este goală.
# Lista nu este goală.
if len(lista3) == 0: # cu functia len am intrebat daca este egal cu 0
    print('Lista este goală') # daca avem continut in lista va printa
else:
    print('Lista nu este goală')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista3.clear() # functia .clear are rolul de a sterge continutul
print(lista3)

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
#Acum ar trebui să se afișeze că lista e goală.
if len(lista3) == 0: # cu functia len am intrebat daca este egal cu 0
    print('Lista este goală') # daca avem continut in lista va printa
else:
    print('Lista nu este goală')

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys()) # functia .keys() are rolul de a afisa doar cheile dintr-un dict

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

# Varianta 1
print(f'Ana a luat nota {dict1["Ana"]}') # putem afla valoarea print numele dict['cheia']
print(f'Gigel a luat nota {dict1["Gigel"]}')
print(f'Dorel a luat nota {dict1["Dorel"]}')

# Varianta 2
print(f'Ana a luat nota {dict1.get("Ana")}') # putem afla valoarea print numele dict.get('cheia')
print(f'Gigel a luat nota {dict1.get("Gigel")}')
print(f'Dorel a luat nota {dict1.get("Dorel")}')

# 10. Dorel a făcut contestație și a primit 6
# Modifică nota lui Dorel în 6
# Printează nota după modificare
dict1['Dorel'] = 6 # numele dict['cheia'] = cu noua valoare ( # adaugam / suprascriem un element din dict )
print(dict1)

# 11. Gigel se transferă din clasă
# Căuta o funcție care să îl șteargă
# Vine un coleg nou. Adaugă Ionică, cu nota 9
# Printează noii elevi
dict1.pop('Gigel') # scoatem un element din dict
dict1['Ionică'] = 9 # adaugam / suprascriem un element din dict
print(dict1)

# 13.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# Adaugă în zilele_sapt ‘luni’
# Afișează zile_sapt

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

zile_sapt.add('luni') # cu functia .add() adaugam elemente ( NU PUTEM AVEA DUPLICATE INTR-UN SET !!! )
print(zile_sapt)

# 14.Folosește un if și verifică dacă:
# Weekend este un subset al zilelor din săptămânii.
# Weekend nu este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt): # cu functia issubset() aflam daca set-ul weekend este un subset al zilelor din sapt
    print('Weekend este un subset al zilelor din săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')

# 15. Afișează diferențele dintre aceste 2 seturi.
diferente = zile_sapt.difference(weekend) # cu functia .difference() aflam diferentele dintre cele doua set-uri
print(diferente)

# 16. Afișează intersecția elementelor din aceste 2 seturi.
diferente = zile_sapt.intersection(weekend) # cu functia .intersection() aflam valorile care se afla in ambele set-uri
print(diferente)