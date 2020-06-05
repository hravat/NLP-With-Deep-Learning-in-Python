import string
import re

regex = re.compile('[%s]' % re.escape(string.punctuation))
out = regex.sub(' ', "there?")
print(out)