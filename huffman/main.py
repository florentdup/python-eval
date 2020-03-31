from codec import TreeBuilder, Codec

text = "a dead dad ceded a bad babe a beaded abaca bed"
text="Pleins plutot apprit des ils connut vit balaye. Eau ames fois fils rit une fixe ifs. Age nos autour que soldat simple. Depourvus corbeille eut ici marechaux croissent abondance les ressemble. Dissipait quiconque printemps cravaches les demeurent peu. Vivant empire qu boules on blancs en. Pieces ce ma metres nombre ah he.Aussi la ca etait ronds ma. Dans et je chez on coin. Je faux sont le me ma vent. Usines furent on ii etonna carres. Concierge redoutait expliquer fusillade il je le demeurons cependant et. Hurlements etonnement compassion la me nationales bouquetins renferment. Je soeurs poteau ecarta le me.Xv on du tremblent tranchees pu uniformes. Sapins hordes sabres et connut bottes mollir si ma du. Capitaine il desespoir ii divergent petillent. Bles hors tard vint cela fond nez nos. Oeufs dites jeune fille ville ras foi ses. Ni grandes sa regarde entrait un oh. Parmi ere ainsi leurs rit halte ivres but. Ont malheur jeu eut importe fiancee pelouse prefere dit attache. Verte ans lui glace fut pas train. Vrai or ou ciel vers nees oh. Mendiaient cathedrale subitement mal ere oui fut. Qu ange cela on lors vers eaux. Perimetre je courroies en la esplanade gachettes etendards cesserent. Entiere premier adultes oh la tu si caillou. Faut aux les eux dela gens sent que. Prochain eau remporte toi faudrait retablir susciter attentif ces. Imprudente ils son eau remarquait frequentes poussaient. Epaissies preferait accoudees promenade je on ca troupeaux.Ah bout nous venu quel oh joie mort. Et bravoure promptes me crispent on. Pouvons tu initiez arriere ouvrent dociles on et langage. Se gouverneur chantaient remarquent on. Francine quelques cailloux et du. Rit son recrues ici tristes lorgnez quitter. Glisse je moment disait he intime ah. Gachettes signalant murmurait expliquer eut peu sortaient consumait."

# on analyse les fréquences d'occurrence dans text
# pour fabriquer un arbre binaire
builder = TreeBuilder(text)
binary_tree = builder.tree()


# on passe l'arbre binaire à un encodeur/décodeur
codec = Codec(binary_tree)
# qui permet d'encoder
encoded = codec.encode(text)

# et de décoder
decoded = codec.decode(encoded)

# si cette assertion est fausse il y a un gros problème avec le code
assert text == decoded

# on affiche le résultat
print(f"{text}\n{encoded}")

print(f"Ratio: {8*len(text)/len(encoded)}")

if decoded != text:
    print("OOPS")