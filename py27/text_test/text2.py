import nltk

filename2 = ("E:/Eclipse/workspace/py27/temp2.txt")

with open(filename2,'r') as file1:
    lines_in_file = file1.read()
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print nltk_tokens
    print ("Number of words:", len(nltk_tokens))
    print ("***************************************")
    print (lines_in_file.split())
    print ("Number of words:", len(lines_in_file.split()))# split by space by default