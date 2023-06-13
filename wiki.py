texteWiki ="La Fondation Wikimédia, organisation à but non lucratif américaine sise à San Francisco, est dépositaire de la marque Wikipedia. Elle finance l'hébergement web de l'encyclopédie. " 

print("type de la variable texteWiki :" ,type(texteWiki))


# Count number of words in message
# texteWiki.split return a list of words
num_words = len(texteWiki.split())

# Display number of words
print(f"Number of words: {num_words}")