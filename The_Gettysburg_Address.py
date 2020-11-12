import string
import requests

text = requests.get("https://markfoley.info/pa1/gettysburg.txt")
body = str(text.content.decode('utf-8'))

stop_words_source = requests.get('https://markfoley.info/pa1/stopwords.txt')
stop_words = list(stop_words_source.content.decode('utf-8').split(','))

punctuation = list(string.punctuation)

count_words = 0
list_words = []
words_dict = {}

for word in body.split():

    if word[-1] in punctuation:
        word = word[:-1]

    if word not in stop_words:
        count_words += 1

        if word not in list_words:
            list_words.append(word)

        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

print(count_words)
print(list_words)
print(words_dict)

