
with open("labirynt0.txt", "r") as f_in:
    lines = filter(None, (line.rstrip() for line in f_in))
        

# print labirynt

start = '@'
end = '$'

# print lines
# print lines[0]
height,width= lines[0].split(' ')

# print height,width

for line in lines:
    for c in line:
        if c == start:
             'start'
    print line




