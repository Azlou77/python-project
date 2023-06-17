# Generalize the code for an indeterminate number of variables, therefore of texts.
# The function should return the two texts (among the n inputs) that are the most similar.

# Read x texts
def read_x_texts(x):
    # Initialize list of texts
    texts = []
    # Loop over x
    for i in range(x):
        # Open text
        f = open(f"text/text{i+1}.txt", "r")
        # Read text
        text = f.read()
        # Append text to list of texts
        texts.append(text)
    # Return list of texts
    return texts



# Count and compare the number of words in common between text1 and text2
def count_words_in_common(texts):
    # Initialize counter
    counter = 0
    # Split text1 into list of words
    words1 = texts[0].split()
    # Split text2 into list of words
    words2 = texts[1].split()
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
print(f"Number of words in common between text1 and text2: {count_words_in_common(read_x_texts(2))}")

# Count and compare the number of words in common between text1 and text3
def count_words_in_common(texts):
    # Initialize counter
    counter = 0
    # Split text1 into list of words
    words1 = texts[0].split()
    # Split text3 into list of words
    words3 = texts[2].split()
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
print(f"Number of words in common between text1 and text3: {count_words_in_common(read_x_texts(3))}")

# Count and compare the number of words in common between text2 and text3
def count_words_in_common(texts):
    # Initialize counter
    counter = 0
    # Split text2 into list of words
    words2 = texts[1].split()
    # Split text3 into list of words
    words3 = texts[2].split()
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
print(f"Number of words in common between text2 and text3: {count_words_in_common(read_x_texts(3))}")


# Compare the number of words in common between text1 and text2, text1 and text3, text2 and text
def compare_texts(x):
    # Initialize list of texts
    texts = read_x_texts(x)
    # Initialize list of counters
    counters = []
    # Loop over texts
    for i in range(x):
        # Loop over texts
        for j in range(x):
            # Check if texts are different
            if i != j:
                # Initialize counter
                counter = 0
                # Split text1 into list of words
                words1 = texts[i].split()
                # Split text2 into list of words
                words2 = texts[j].split()
                # Loop over words1
                for word1 in words1:
                    # Loop over words2
                    for word2 in words2:
                        # Check if words are identical
                        if word1 == word2:
                            # Increment counter
                            counter += 1
                # Append counter to list of counters
                counters.append(counter)
    # Return list of counters
    return counters

# Display result
print(f"Number of words in common between text1 and text2, text1 and text3, text2 and text3: {compare_texts(3)}")





