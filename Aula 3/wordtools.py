def cleanword(word):
    clean = ""
    for i in range(len(word)):
        c = word[i:i+1]
        c = c.lower()
        if c.isalpha():
            clean += c
    return clean

def has_dashdash(word):
    for i in range(len(word) - 1):
        if word[i] == "-" and word[i+1] == '-':
            return True
    return False

def extract_words(phrase):
    last = 0
    words = []
    for i in range(len(phrase)):
        if not phrase[i].isalpha():
            new_word = cleanword(phrase[last:i])
            if len(new_word) > 0:
                words.append(new_word)
            last = i
    if last != len(phrase)-1:
        new_word = cleanword(phrase[last:len(phrase)])
        if len(new_word) > 0:
            words.append(new_word)
    return words

def wordcount(word, list):
    count = 0
    for i in range(len(list)):
        if word == list[i]:
            count += 1
    return count

def wordset(list):
    set = []
    for i in range(len(list)):
        if wordcount(list[i], set) == 0:
            set.append(list[i])
    set.sort()
    return set

def longestword(list):
    sz = 0
    for i in range(len(list)):
        if len(list[i]) > sz:
            sz = len(list[i])
    return sz
