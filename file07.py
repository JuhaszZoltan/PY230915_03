# listak: öszetett adatszerkezetek
# olyan érték-kollekciók, aminek több eleme is lehet

# a pythonban a listák heterogének
# viszont mi CSAK homogén listákkal fogunk foglalkozni

# jelölés
halak:list[str] = ['keszeg', 'harcsa', 'ponty']

# üres lista:
ures_lista:list[int] = []

# listák bejárhatóak for ciklussal (ezen már túlvagyunk)

# lista bizonyos elemére az indexével hivatkozunk
print(halak[1])

# a programozásban mindig (általában...) ún. 
# "zero based indexig"van, 
# vagyis amikor az elemeknek van sorrendje 
# és az indexével tudk rájuk hivatkozni
# akkor az első elem indexe mindig nulla
#                      0         1        2
halak:list[str] = ['keszeg', 'harcsa', 'ponty']

# ha a listát bűvíteni szeretném,
# akkor van rá példány szintű metódus:

halak.append('hering')
# az 'append' a paraméterként átadott elemt 
# a lista végére teszi hozzá

# a lista neve atadva a print-nek:
# összes jelenlegi elemet kiirja:
print(halak)

halak.insert(2, 'bohóchal')
print(halak)

halak[2] = 'cápa'
print(halak)

# elemek cseréja:
seged:str = halak[0]
halak[0] = halak[4]
halak[4] = seged
print(halak)

# pythonban így is lehet cserélni
halak[1], halak[2] = halak[2], halak[1]
print(halak)
