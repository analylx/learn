from nltk.corpus import wordnet
print (wordnet.synsets("big"))
print("________________1__________________")
synonyms =[]
for syn in wordnet.synsets("Soil"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print (set(synonyms))

print("_______________21__________________")
antonyms = []
for syn in wordnet.synsets("ahead"):
    for lm in syn.lemmas():
        if lm.antonyms():
            antonyms.append(lm.antonyms()[0].name())
print(set(antonyms))