class Labirynt:
    
    def __init__(self):
        with open("labirynt0.txt", "r") as f_in:
            self.lines =filter(None, (line.rstrip() for line in f_in))
        self.done = False
        self.start = "@"
        self.end = "$"
        self.height,self.width = self.lines[0].split(' ')
        self.height = int(self.height)
        self.width = int(self.width)
        
    def findStart(self):
        for y in xrange(1,self.height+1):
    #     print len(lines[x])
            for x in xrange(len(self.lines[y])):
    #            print lines[x][y]
                if self.lines[y][x]==self.start:
    #             print 'znaleziono poczatek'
                    xP, yP = x, y
        cord= [yP,xP]
        return cord
    
    def printuj(self):
        for c in self.lines[1:] :
            print c
            
    def value(self,x,y):
        return self.lines[y][x]
        
        
    def findEnd(self,cordinates=[],way=[]):
        print 'tu', cordinates
        if self.value(cordinates[1],cordinates[0])==self.end:
            print "Znalazlem"
            self.done=True
            self.printuj()
            print way
            return ' '
            
        if self.value(cordinates[1], cordinates[0]) != self.start:
            self.lines[cordinates[1]][cordinates[0]]= 'X'
            
        if (self.value(cordinates[1], cordinates[0]+1) != '' or self.value(cordinates[1], cordinates[0]+1) != '$') and (self.value(cordinates[1], cordinates[0]+1) != self.start) and (self.value(cordinates[1], cordinates[0]+1) != self.end) and (self.done == False):
            print '1',cordinates
            way.append([cordinates[0]+1,cordinates[1]])
            self.findEnd([cordinates[0]+1,cordinates[1]])
            
        if (self.value(cordinates[1]+1, cordinates[0]) != '' or self.value(cordinates[1]+1, cordinates[0]) != '$') and (self.value(cordinates[1]+1, cordinates[0]) != self.start) and (self.value(cordinates[1]+1, cordinates[0]) != self.end) and (self.done == False):
            print '2',cordinates
            way.append([[cordinates[1]+1,[cordinates[0]]]])
            self.findEnd([[cordinates[1]+1,[cordinates[0]]]])
            
            
        if (self.value(cordinates[1], cordinates[0]-1) != '' or self.value(cordinates[1], cordinates[0]-1) != '$') and (self.value(cordinates[1], cordinates[0]-1) != self.start) and (self.value(cordinates[1], cordinates[0]-1) != self.end) and (self.done == False):
            print '3',cordinates
            way.append([cordinates[1],[cordinates[0]-1]])
            self.findEnd([[cordinates[1],[cordinates[0]-1]]])
        
        if (self.value(cordinates[1]-1, cordinates[0]) != '' or self.value(cordinates[1]-1, cordinates[0]) != '$') and (self.value(cordinates[1]-1, cordinates[0]) != self.start) and (self.value(cordinates[1]-1, cordinates[0]) != self.end) and (self.done == False):
            print '4',cordinates
            way.append([[cordinates[1]-1],[cordinates[0]]])
            self.findEnd([[cordinates[1]-1],[cordinates[0]]])
            
        return 1
            
        
        
            
            
        
  
        
labi = Labirynt()
startuje = labi.findStart()
print startuje
labi.printuj()
print labi.findStart()
labi.findEnd(startuje)
        
        

# with open("labirynt0.txt", "r") as f_in:
#     lines = filter(None, (line.rstrip() for line in f_in))
#   
# 
# 
# start = '@'
# end = '$'
# 
# height,width = lines[0].split(' ')
# height = int(height)
# width = int(width)
# for c in lines[1:] :
#     print c
#     
# kierunek = "rdlt"
# 
# def wspolrzedne_pkt():
#     for y in xrange(1,height+1):
#     #     print len(lines[x])
#         for x in xrange(len(lines[y])):
#     #         print lines[x][y]
#             if lines[y][x]==start:
#     #             print 'znaleziono poczatek'
#                 xP, yP = x, y
#             if lines[y][x]==end:
#                 xE, yE = x, y
#     return [xP,yP,xE,yE]
# 
# print wspolrzedne_pkt()
# 
# def wartosc_pkt(x,y):
#     return lines[y][x]
# 
# def znajdz_droge(xP,yP,xE,yE):
#     kierunek = "rdlt"
#     kierunek = "gdlp"
#     tab=[]
#     print wartosc_pkt(xP,yP)
#     while wartosc_pkt(xP,yP)!= '$':   
#         for i in kierunek:
#             if i == 'p' and wartosc_pkt(xP+1,yP)!='#' :
#                 print 'if1'
#                 if [xP,yP] is not in tab:
#                     tab.append([xP,yP])
#                     xP+=1
#                 print xP,yP,tab
#                 break
#             
#             elif i == 'd' and wartosc_pkt(xP,yP+1)!='#' :
#                 print 'if2'
#                 tab.append([xP,yP])
#                 yP+=1
#                 print xP,yP,tab
#                 break
#             elif i == 'l' and wartosc_pkt(xP-1,yP)!='#' :
#                 print 'if3'
#                 tab.append([xP,yP])
#                 xP-=1
#                 print xP,yP,tab
#                 break
#             elif i == 'g' and wartosc_pkt(xP,yP-1)!='#' :
#                 print 'if4'
#                 tab.append([xP,yP])
#                 yP-=1
#                 print xP,yP,tab
#                 break
#     return 'znalazlem', xP, yP, tab
#     
# start = '@'
# end = '$'
# 
# # print xP, yP  #12(13) i 7
# # print xE, yE  # 7(8) i 2
# print wartosc_pkt(12,7)
# print wartosc_pkt(7,2)
# print znajdz_droge(12, 7, 7, 2)
# 
# def idz(x,y,'r')
# 
# 
# 
#        
#     