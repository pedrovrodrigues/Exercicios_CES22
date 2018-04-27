f = open("phrases.txt", 'r')
content = f.readlines()
content.reverse()
if content[0][-1] != '\n':
    content[0] += "\n"

g = open("reverse.txt", 'w')
for ln in content:
    g.write(ln)

