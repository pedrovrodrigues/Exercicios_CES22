import urllib.request

def cleanword(word):
    clean = ""
    for i in range(len(word)):
        c = word[i:i+1]
        c = c.lower()
        if c.isalpha():
            clean += c
    return clean

my_socket = urllib.request.urlopen("http://www.gutenberg.org/files/11/11-0.txt")
dta = str(my_socket.readall())
my_socket.close()
listing = dta.split()
for w in listing
    w = cleanword(w)
listing.sort()
ranking = {}
max = 0
for w in listing
    ranking[w] = listing.count(w)
    if len(w) > max:
        max = len(w)

g = open("alice_words.txt", "w")

g.write("Word")
for i in range(max):
    g.write(" ")
g.write("Count\n")
for i in range(max+9):
    g.write("=")
g.write("\n")

for (w,n) in ranking:
    g.write(w)
    for i in range(max + 4 - len(w)):
        g.write(" ")
    g.write(n)
    g.write("\n")

g.close()

print "The word Alice appears {0} times.".format(ranking["alice"])