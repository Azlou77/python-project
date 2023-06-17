# On prend trois textes
# Ecrire un programme qui à partir d'un corpus de trois textes renvoie les deux textes qui ont le plus de mots en communs.

# Read the three texts
f = open("text/text1.txt", "r")
text1 = f.read()
f = open("text/text2.txt", "r")
text2 = f.read()
f = open("text/text3.txt", "r")
text3 = f.read()


# Count and compare the number of words in common between text1 and text2
def count_words_in_common(text1, text2):
    # Initialize counter
    counter = 0
    # Split text1 into list of words
    words1 = text1.split()
    # Split text2 into list of words
    words2 = text2.split()
    # Loop over words1
    for word1 in words1:
        # Loop over words2
        for word2 in words2:
            # Check if words are identical
            if word1 == word2:
                # Increment counter
                counter += 1
    # Return counter
    return counter

# Display result
print(f"Number of words in common between text1 and text2: {count_words_in_common(text1, text2)}")

# Count and compare the number of words in common between text1 and text3
def count_words_in_common(text1, text3):
    # Initialize counter
    counter = 0
    # Split text1 into list of words
    words1 = text1.split()
    # Split text3 into list of words
    words3 = text3.split()
    # Loop over words1
    for word1 in words1:
        # Loop over words3
        for word3 in words3:
            # Check if words are identical
            if word1 == word3:
                # Increment counter
                counter += 1
    # Return counter
    return counter

# Display result
print(f"Number of words in common between text1 and text3: {count_words_in_common(text1, text3)}")

# Count and compare the number of words in common between text2 and text3
def count_words_in_common(text2, text3):
    # Initialize counter
    counter = 0
    # Split text2 into list of words
    words2 = text2.split()
    # Split text3 into list of words
    words3 = text3.split()
    # Loop over words2
    for word2 in words2:
        # Loop over words3
        for word3 in words3:
            # Check if words are identical
            if word2 == word3:
                # Increment counter
                counter += 1
    # Return counter
    return counter
    

# Display result   
print(f"Number of words in common between text2 and text3: {count_words_in_common(text2, text3)}")

# Compare the number of words in common between text1 and text2, text1 and text3, text2 and text3
if count_words_in_common(text1, text2) > count_words_in_common(text1, text3) and count_words_in_common(text1, text2) > count_words_in_common(text2, text3):
    print("text1 and text2 have the most words in common")

elif count_words_in_common(text1, text3) > count_words_in_common(text1, text2) and count_words_in_common(text1, text3) > count_words_in_common(text2, text3):
    print("text1 and text3 have the most words in common")

elif count_words_in_common(text2, text3) > count_words_in_common(text1, text2) and count_words_in_common(text2, text3) > count_words_in_common(text1, text3):
    print("text2 and text3 have the most words in common")

else:
    print("There is no text with the most words in common")

