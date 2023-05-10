A = [
['¿Qué club inglés es conocido como "Los Spurs"?', 'Tottenham', 'Manchester City', 'Arsenal', 'West Ham United'],
 
['¿Qué equipo italiano es conocido como "La Vecchia Signora"?', 'Juventus', 'Napoli', 'AC Milan', 'Roma'],

['¿Qué club inglés es conocido como "Los Gunners"?', 'Arsenal', 'Newcastle', 'Manchester United', 'Wolves'],

['¿A qué club español se le conoce como “Los Merengues”?', 'Real Madrid', 'Sevilla', 'Atlético de Madrid', 'Girona'],

['¿Qué club inglés es conocido como "Los Red Devils"?', 'Manchester United', 'Chealsea', 'Liverpool', 'Arsenal'],

['¿Qué equipo de argentina se apoda "Xeneize"?', 'Boca Juniors', 'Rivel Plate', 'Racing', 'Rosario central'],

['¿Qué equipo argentino es apodado "El Millonario"?', 'River Plate', 'Boca Juniors', 'Newlls', 'Independiente'],

['¿Qué equipo italiano es apodado "La Loba"?', 'Roma', 'Juventus', 'Inter de Milan', 'AC Milan'],

['¿Qué club de fútbol mexicano es conocido como "Las Águilas"?', 'Club América', 'Monterrey', 'Guadalajara', 'Club Toluca'],

['¿Qué equipo se apoda "Los Blues"?', 'Chelsea', 'Manchester City' , 'Newcastle', 'Wolves'],

['¿Qué club tiene el apodo “Los Colchoneros”?', 'Atlético de Madrid', 'Real Betis','Rayo Vallecano', 'FC Barcelona'],

['¿Qué equipo es apodado “El Submarino Amarillo”?', 'Villareal', 'Real Sociedad', 'Sevilla', 'Celta de Vigo'],

['¿Qué equipo es conocido como “Las Chivas”?', 'CD Guadalajara', 'Atlas', 'Morelia', 'Tigres'],

['¿Qué equipo español se apoda "Los Leones"?', 'Athletic Club', 'Levante', 'Granada', 'Celta de Vigo'],

['¿Qué equipo es conocido como “Culés”?', 'FC Barcelona', 'Espanyol', 'Girona', 'Eibar'],

['¿Qué club italiano es apodado “Diavoli”?', 'AC Milan', 'Inter de Milan', 'Sassuolo', 'Napoli'],

['¿Cuál club es apodado “Citezens”?', 'Manchester City', 'Arsenal', 'Leicester City', 'Chelsea'],

['¿Qué equipo español se apoda “Palanganas”?', 'Sevilla FC', 'Real Betis', 'Granada', 'Espanyol'], 

['¿Qué equipo mexicano es apodado “Pumas”?', 'Universidad Nacional (UNAM)', 'Guadalajara', 'Monterrey', 'Club América'],

['¿Qué equipo de España se apoda "Pericos"?', 'RCD Espanyol', 'FC Barcelona', 'UD Las Palmas', 'Sevilla'],

['¿Qué club inglés es conocido como "Los Reds"?', 'Liverpool', 'Manchester United', 'Tottenham Hotspur', 'Everton'],

['¿Qué equipo alemán es conocido como "Die Roten"?', 'Bayern Munich', 'Borussia Dortmund', 'RB Leipzig', 'Bayer Leverkusen'],

['¿Qué club francés es conocido como "Les Parisiens"?', 'Paris Saint-Germain', 'Olympique Lyonnais', 'AS Monaco', 'Stade Rennais'],

['¿Qué equipo portugués es conocido como "Águias"?', 'SL Benfica', 'Sporting CP', 'FC Porto', 'Vitória de Guimarães'],

['¿Qué club brasileño es conocido como "Tricolor Paulista"?', 'São Paulo', 'Flamengo', 'Palmeiras', 'Santos'],

['¿Qué equipo holandés es conocido como "Los Granjeros"?', 'PSV Eindhoven', 'Ajax', 'Feyenoord', 'FC Utrecht'],

['¿Qué club italiano es conocido como "Nerazzurri"?', 'Inter de Milan', 'Juventus', 'AC Milan', 'Lazio'],

['¿Qué club alemán es conocido como "Die Schwarzgelben (Los negriamarillos)"?', 'Borussia Dortmund', 'Bayern Munich', 'Schalke 04', 'VfB Stuttgart'],

['¿Qué equipo portugués es conocido como "Os Dragões"?', 'FC Porto', 'Sporting CP', 'SL Benfica', 'SC Braga'],

['¿Qué equipo alemán es conocido como "Los Toros Rojos"?','RB Leipzig', 'Borussia Dortmund', 'Bayern Munich', 'Eintracht Frankfurt'],
['¿Qué club turco es conocido como "Las Águilas Negras"?', 'Beşiktaş', 'Fenerbahçe', 'Galatasaray', 'Trabzonspor'],
['¿Qué equipo colombiano es conocido como "Los Embajadores"?', 'Millonarios', 'Atlético Nacional', 'Deportivo Cali', 'Independiente Santa Fe'],
['¿Qué equipo colombiano es conocido como "Los Verdolagas"?', 'Atlético Nacional', 'Millonarios', 'Deportivo Cali', 'Independiente Santa Fe']
]

P=[]
T=[]
I1=[]
I2=[]
I3=[]
a=0
for i in A:
    P.append(i[0])
    T.append(i[1])
    I1.append(i[2])
    I2.append(i[3])
    I3.append(i[4])
    a+=1

#for i in T:
#    print(i)
#print(P)
#print(T)
#print(I1)
#print(I2)
#print(I3)
#print(a)

a=['tottenham.png','juventus.png', 'arsenal.png', 'r-madrid.png','manunited.png','boca.png','river.png','roma.png','america.png','chelsea.png','a-madrid.png','villareal.png','chivas.png','bilbao.png','barcelona.png','milan.png','mancity.png','sevilla.png','pumas.png','esapnyoñ.png',    'liverpool.png', 'bayern.png','psg.png','benfica.png','sanpablo.png','psv.png','inter.png', 'dortmund.png', 'porto.png', 'leipzig.png','besiktas.png', 'millonarios.png','nacional.png']
aa=[] 
bb=[]
cc=[]
dd=[]
ee=[]
ff=[]
b = ['¿Qué club inglés es conocido como "Los Spurs"?', '¿Qué equipo italiano es conocido como "La Vecchia Signora"?', '¿Qué club inglés es conocido como "Los Gunners"?', '¿A qué club español se le conoce como “Los Merengues”?', '¿Qué club inglés es conocido como "Los Red Devils"?', '¿Qué equipo de Argentina se apoda "Xeneize"?', '¿Qué equipo argentino es apodado "El Millonario"?', '¿Qué equipo italiano es apodado "La Loba"?', '¿Qué club de fútbol mexicano es conocido como "Las Águilas"?', '¿A qué equipo se le apoda "Los Blues"?', '¿Qué club tiene el apodo “Los Colchoneros”?', '¿Qué equipo es apodado “El Submarino Amarillo”?', '¿Qué equipo es conocido como “Las Chivas”?', '¿Qué equipo español se apoda "Los Leones"?', '¿Qué equipo es conocido como “Culés”?', '¿Qué club italiano es apodado “Diavoli”?', '¿Qué club es apodado “Citezens”?', '¿Qué equipo español se apoda “Palanganas”?', '¿Qué equipo mexicano es apodado “Pumas”?', '¿Qué equipo de España se apoda "Pericos"?', '¿Qué club inglés es conocido como "Los Reds"?', '¿Qué equipo alemán es conocido como "Die Roten"?', '¿Qué club francés es conocido como "Les Parisiens"?', '¿Qué equipo portugués es conocido como "Águias"?', '¿Qué club brasileño es conocido como "Tricolor Paulista"?', '¿A qué equipo holandés se le conoce como "Los Granjeros"?', '¿Qué club italiano es conocido como "Nerazzurri"?', '¿Qué club alemán es conocido como "Die Schwarzgelben (Los negriamarillos)"?', '¿Qué equipo portugués es conocido como "Os Dragões"?', '¿Qué equipo alemán es conocido como "Los Toros Rojos"?', '¿Qué club turco es conocido como "Las Águilas Negras"?', '¿Qué equipo colombiano es conocido como "Los Embajadores"?', '¿Qué equipo colombiano es conocido como "Los Verdolagas"?'];

c = ['Tottenham', 'Juventus', 'Arsenal', 'Real Madrid', 'Manchester United', 'Boca Juniors', 'River Plate', 'Roma', 'Club América', 'Chelsea', 'Atlético de Madrid', 'Villareal', 'CD Guadalajara', 'Athletic Club', 'FC Barcelona', 'AC Milan', 'Manchester City', 'Sevilla FC', 'Universidad Nacional (UNAM)', 'RCD Espanyol', 'Liverpool', 'Bayern Munich', 'Paris Saint-Germain', 'SL Benfica', 'São Paulo', 'PSV Eindhoven', 'Inter de Milan', 'Borussia Dortmund', 'FC Porto', 'RB Leipzig', 'Beşiktaş', 'Millonarios', 'Atlético Nacional'];
d = ['Manchester City', 'Napoli', 'Newcastle', 'Sevilla', 'Chealsea', 'Rivel Plate', 'Boca Juniors', 'Juventus', 'Monterrey', 'Manchester City', 'Real Betis', 'Real Sociedad', 'Atlas', 'Levante', 'Espanyol', 'Inter de Milan', 'Arsenal', 'Real Betis', 'Guadalajara', 'FC Barcelona', 'Manchester United', 'Borussia Dortmund', 'Olympique Lyonnais', 'Sporting CP', 'Flamengo', 'Ajax', 'Juventus', 'Bayern Munich', 'Sporting CP', 'Borussia Dortmund', 'Fenerbahçe', 'Atlético Nacional', 'Millonarios'];
e = ['Arsenal', 'AC Milan', 'Manchester United', 'Atlético de Madrid', 'Liverpool', 'Racing', 'Newlls', 'Inter de Milan', 'Guadalajara', 'Newcastle', 'Rayo Vallecano', 'Sevilla', 'Morelia', 'Granada', 'Girona', 'Sassuolo', 'Leicester City', 'Granada', 'Monterrey', 'UD Las Palmas', 'Tottenham Hotspur', 'RB Leipzig', 'AS Monaco', 'FC Porto', 'Palmeiras', 'Feyenoord', 'AC Milan', 'Schalke 04', 'SL Benfica', 'Bayern Munich', 'Galatasaray', 'Deportivo Cali', 'Deportivo Cali'];
f = ['West Ham United', 'Roma', 'Wolves', 'Girona', 'Arsenal', 'Rosario central', 'Independiente', 'AC Milan', 'Club Toluca', 'Wolves', 'FC Barcelona', 'Celta de Vigo', 'Tigres', 'Celta de Vigo', 'Eibar', 'Napoli', 'Chelsea', 'Espanyol', 'Club América', 'Sevilla', 'Everton', 'Bayer Leverkusen', 'Stade Rennais', 'Vitória de Guimarães', 'Santos', 'FC Utrecht', 'Lazio', 'VfB Stuttgart', 'SC Braga', 'Eintracht Frankfurt', 'Trabzonspor', 'Independiente Santa Fe', 'Independiente Santa Fe'];

z=0
for x in a,b,c,d,e,f:
    aa.append(a[z])
    bb.append(b[z])
    cc.append(c[z])
    dd.append(d[z])
    ee.append(e[z])
    ff.append(f[z])
    z+=1
    if z==3:
        break
        
print(aa, bb, cc, dd, ee, ff)