import nltk,re
word_data = "The Sky is blue also the ocean is blue also Rainbow has a blue colour."
nltk_tokens = nltk.word_tokenize(word_data)
no_order = list(set(nltk_tokens))
print(no_order)

ordered_tokens = set()
result = []
for word in nltk_tokens:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        result.append(word)
print(result)

text = "Please contact us at contact@qq.com for further information."+\
        " You can also give feedbacl at feedback@yiibai.com"
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]",text)
print(emails)

text="""Now a days you can learn almost anything by just visiting http://www.google.com. But if you are completely new to computers or internet then first you need to leanr those fundamentals. Next
you can visit a good e-learning site like - https://www.yiibai.com to learn further on a variety of subjects."""

urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',text)
print(urls)

sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
nltk_tokens = nltk.sent_tokenize(sentence_data)
print (nltk_tokens)
print("________________________1____________________________")
german_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens=german_tokenizer.tokenize('Wie geht es Ihnen?  Gut, danke.')
print(german_tokens)
print("_________________________2___________________________")
word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms."
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)
print("_________________________3___________________________")
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))

all_words = ['There', 'is', 'a', 'tree','near','the','river']
for word in all_words: 
    if word not in en_stops:
        print(word)