import numpy as np

from colorama import Fore, Style

def redtext(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"



class Ruler():
    """Classe qui s'occupe de calculer la distance entre deux chaînes de caractère"""
    def __init__ (self,str_1,str_2):
        self._A=str_1
        self._B=str_2

    def compute(self):
        dist_increase_no_match=1 #On fixe les pénalités 
        dist_increase_del_ins=1

        n,p=len(self._A)+1,len(self._B)+1
        self.F=np.zeros((n,p))

        #On rempli la matrice F qui va nous permettre de calculer la distance entre deux chaînes de caractère
        
        for i in range(n):
            self.F[i, 0] = dist_increase_del_ins*i
        for j in range(p):
            self.F[0,j] = dist_increase_del_ins*j
        for i in range(1,n):
            for j in range(1,p):
                c1 = self.F[i-1,j-1] + dist_increase_no_match*(self._A[i-1]!=self._B[j-1])
                c2 = self.F[i-1, j] + dist_increase_del_ins
                c3 = self.F[i, j-1] + dist_increase_del_ins
                self.F[i, j] = min(c1, c2, c3)
        
        self.distance=self.F[n-1,p-1]

    def report(self):
        d=1
        chaine1,chaine2 = "",""
        tiret_rouge=redtext("-")
        i,j = len(self._A),len(self._B) 
        while (i > 0 and j > 0):#On determine le chemin qui a été pris dans F, en partant d'en bas à droite
            distance = self.F[i, j]
            distanceDiag = self.F[i - 1, j - 1]
            distanceHaut = self.F[i, j - 1]
            distanceGauche = self.F[i - 1, j]

            #En effectuant une disjonction de cas, on peut savoir quelle a été la cause 
            #de l'augmentation de la distance entre les deux chaînes en entrée_A et _B#

            if distance == distanceDiag + 1*(self._A[i-1]!=self._B[j-1]): #Cas ou les caractères diffèrent
                if self._A[i-1]!=self._B[j-1]:
                    chaine1 = redtext(self._A[i-1]) + chaine1
                    chaine2 = redtext(self._B[j-1]) + chaine2
                else:
                    chaine1 = self._A[i-1] + chaine1
                    chaine2 = self._B[j-1] + chaine2
                i -=1
                j -=1
            elif distance == distanceGauche + d: #Cas ou la chaîne B a un caractère manquant
                chaine1 = self._A[i-1] + chaine1
                chaine2 = tiret_rouge + chaine2
                i-=1
            elif distance == distanceHaut + d: #Cas ou la chaîne A a un caractère manquant
                chaine1 = tiret_rouge + chaine1
                chaine2 = self._B[j-1] + chaine2
                j-=1
        while (i > 0): #On complete la chaîne chaine1(chaîne A) avec les parties qui ne se trouvent pas dans B
            chaine1 = self._A[i-1] + chaine1
            i -=1
  
        while (j > 0):  #On complete la chaîne chaine2(chaîne B) avec les parties qui ne se trouvent pas dans A 
            chaine1 = redtext("-") + chaine1
            chaine2 = self._B[j-1] + chaine2
            j -=1

        return chaine1,chaine2
