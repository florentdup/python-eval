import sys
from ruler import Ruler
 
try:#On verifie qu'on a bien des données à traiter
    argument1 = sys.argv[0]
    argument2 = sys.argv[1]
except IndexError:
    print("Pas de donées à traiter")
    exit()

liste=[]
with open(argument2) as txtfile:
    data = txtfile.read()
    data=data.split("\n")
    i,j=0,1
    while i <len(data):
        while i<len(data) and data[i]=="" :
            i+=1   #On cherche une chaine non vide pour la première chaîne
        j=i+1  
        while j<len(data) and data[j]=="" :#On cherche une chaîne non vide pour la deuxième chaîne
            j+=1

        if j<=len(data)-1 and data[j]!="": #Cette condition permet de verifier que deux chaînes non vide ont été trouvées
            liste.append([data[i],data[j]])
        i=j+1#On recommence juste après la dernière chaîne trouvée non vide

if liste==[]:#Si le fichier ne contenait pas deux chaines de caractère au moins:
    print("Moins de deux chaînes présentes")
    exit()
        
        


for index,k in enumerate(liste):
    ruler = Ruler(k[0],k[1])
    ruler.compute()
    print(f"________Exemple {index+1}________\n")
    top, bottom = ruler.report()
    print(top+"\n")
    print(bottom)

