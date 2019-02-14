from textwrap3 import wrap
import textwrap3,nltk
filename = "E:/Eclipse/workspace/py27/temp111.txt"
filename2 = ("E:/Eclipse/workspace/py27/temp2.txt")
#data = file(filename).read() #print by letters
#data.sort()#AttributeError: 'str' object has no attribute 'sort'
data = file(filename).readlines()#<type 'list'>
#file(filename).close()
for i in range(len(data)):
    print data[i]

text = "".join(data)
x = wrap(text,60)
for i in range(len(x)):
    print(x[i])
print ("--------------------1-------------------------")
for i in range(len(data)):
    dedented_text = textwrap3.dedent(data[i]).strip()
    print dedented_text
print ("---------------------2------------------------")
with open(filename2,'r') as file1:
    lines_in_file = file1.read()
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print nltk_tokens
    print ("\n")
    print ("Number of words:", len(nltk_tokens))