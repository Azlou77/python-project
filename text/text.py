# Solution
def comparaison_corpus(* textes):
# où a et b sont des textes
    return (a,b)

# objet set()

text1 = "Bonjour, je suis un texte"
text1 = text1.replace (",", "")
liste1 = text1.split()
print(liste1)

text2 = "Bonsoir , j'étais bien un texte"
text2 = text2.replace (",", "")
liste2 = text2.split()
print(liste2)

text3 = "Bonjour, je suis un texte"
text3 = text3.replace (",", "")
liste3 = text3.split()

set_text1 = set(liste1)
set_text2 = set(liste2) 
set_text1, set_text2

# intersection
set_text1.intersection(set_text2)
print(set_text1.intersection(set_text2))


# union
set_text1.union(set_text2)
print(set_text1.union(set_text2))

