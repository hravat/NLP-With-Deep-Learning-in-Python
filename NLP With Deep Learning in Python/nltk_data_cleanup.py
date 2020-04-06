from nltk.corpus import stopwords
import re
import string

nltk_stop_words =stopwords.words('english')
pattern = re.compile('^[a-zA-Z]*$')
regex = re.compile('[%s]' % re.escape(string.punctuation))



def nltk_cleanup(word):
    word = word.lower()
    word = regex.sub('', word)
    if (word in nltk_stop_words) or not pattern.search(word):
       return word,'N'
    else:
        return word,'Y'
