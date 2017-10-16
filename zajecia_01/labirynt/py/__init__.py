
with open("labirynt0.txt", "r") as f_in:
    lines = filter(None, (line.rstrip() for line in f_in))
        


start = '@'
end = '$'

# print lines
# print lines[0]
height,width= lines[0].split(' ')

# print height,width
for x in range(1,len(lines)):
    print lines[x]




