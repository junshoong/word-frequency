import re
import collections

pattern="!\n@#$%^\s+&*()_+-=:\";'<>,./?|"
ew = open("except_words.txt")
except_word = list()
while True:
    line = ew.readline().replace('\n','')
    if len(line) == 0:
        break
    except_word.append(line)

def read_file(text):
    f = open(text)
    r = f.read()
    return r

def word_hist(article):
    words = re.sub(pattern,'',article)
    words = words.lower().split(' ')
    d = dict()
    for a in words:
        if a not in d:
            d[a] = 1
        else:
            d[a] += 1
    return d

def histogram(word):
    d = dict()
    for a in word:
        if a not in d:
            d[a] = 1
        else:
            d[a] += 1
    return d

def print_hist(h):
    for k, v in od.items():
        if k not in except_word and v > 1:
            print(k, v)
        else:
            pass

text = read_file("article.txt")
h = word_hist(text)
od = collections.OrderedDict(sorted(h.items(),key=lambda t: t[1]))
print_hist(od)
