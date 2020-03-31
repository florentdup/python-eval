
symboles=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",\
    "W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",\
    "u","v","w","x","y","z"," ",".",",",";","'"]


def table_occurence(text:str):
    dictio=dict()
    for char in symboles:
        dictio[char]=0 #On créer directement toutes les clés pour ne pas avoir à vérifier qu'elles existent
    for char in text:
            dictio[char]+=1
    return sorted(dictio.items(), key=lambda x: x[1]) #On classe les caractères par fréquence d'apparition dans le texte


def fusion_nodes(node1,node2): #fonction qui s'occupe de fusionner deux noeuds en un
        return Node(node1.key+node2.key,node1.value+node2.value,node1,node2)

class Node():
    """Node permet de coder la strucure d'un arbre (récursivement)"""
    def __init__(self,key=None,value=None,left_node=None,right_node=None):
        self.key=key
        self.value=value
        self.left_node=left_node
        self.right_node=right_node

class TreeBuilder():
    """Classe qui s'occupe de construire l'arbre binaire"""
    def __init__(self,text:str):
        self.pile=table_occurence(text)

        i=0
        while self.pile[i][1]==0:
            i+=1
        self.pile=self.pile[i:] #On inclue pas dans l'arbre qu'on va créer \
        #les caractères qui n'apparaissent pas dans le texte (pour avoir un arbre un peu plus petit)


    def build_tree(self,tree,pile):
        if len(pile)>0:
            if len(pile)>1 and pile[1][1]<tree.value: 
                tmp=fusion_nodes(Node(pile[0][0],pile[0][1]),Node(pile[1][0],pile[1][1]))
                return self.build_tree(fusion_nodes(tmp,tree),pile[2:])
            else:
                return self.build_tree(fusion_nodes(tree,Node(pile[0][0],pile[0][1]) ),pile[1:])           

        else:
            return tree

    def tree(self):
        return self.build_tree(Node("",0),self.pile) #Avec pour base Node("",0) la première itération de build_tree 
        #creera simplement la permière Node
 


class Codec():
    """Classe qui permet de coder et de décoder un message une fois l'arbre binaire donné"""
    def __init__(self,binary_tree):
        self.tree=binary_tree

    def find_code(self,code,binary_tree,letter): #fonction récursive qui parcourt binary tree pour trouver le code d'une lettre
        if binary_tree.key==letter:
            return code
        
        if binary_tree.left_node!=None and letter in binary_tree.left_node.key:
            code+="0"
            return self.find_code(code,binary_tree.left_node,letter)
        elif binary_tree.right_node!=None and letter in binary_tree.right_node.key:
            code+="1"
            return self.find_code(code,binary_tree.right_node,letter)
        
            
    def encode(self,text):
        res=""
        for letter in text:
            res+=self.find_code("",self.tree,letter)#On appelle la fonction récursive find_code 
            #qui retourne le code associé à la lettre "letter",pour chaque lettre
        return res
        
    def decode(self,code):
        current_node=self.tree
        index=0
        res=""
        while index<len(code):
            while len(current_node.key)!=1:  #Tant qu'on est pas à une extrémité de l'abre,
                # on continue de le parcourir  (on effectue une seule comparaison au lieu de deux 
                # si on cherchait à verifier qu'il n'y a pas de sous noeud après celui-ci)
                if code[index]=="1":
                    current_node=current_node.right_node
                else:
                    current_node=current_node.left_node
                index+=1
            res+=current_node.key #On a fini de parcourir l'arbre et la longueur de la clé est de 1: 
                                #c'est la lettre que l'on cherche.
            current_node=self.tree #On repart en haut de l'arbe pour la prochaine lettre
        return res
            
