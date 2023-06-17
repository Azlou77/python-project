# goal of exercise
# Exercices à rendre :
 
# Exercice Lecture de Fichiers
# On prend un texte.
 
# Enregister le texte dans un fichier .txt.
# Lire le fichier et afficher le dictionnaire qui à chaque lettre associe la proportion de mots commenant par cette première lettre dans le texte.





# Lire le fichier texte avec pandas
f = open("text/text1.txt", "r")
texte1 = f.read()


# Define all the letters of the alphabet in list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

# Define a function to count the number of words starting with a letter
def count_words(letter, text):
    # Initialize counter
    counter = 0
    # Split text into list of words
    words = text.split()
    # Loop over words
    for word in words:
        # Check if word starts with letter
        if word[0] == letter:
            # Increment counter
            counter += 1
    # Return counter
    return counter

# Display result
for letter in alphabet:
    print(f"Letter: {letter}, number of words: {count_words(letter, texte1)}")




 
 




 
 
