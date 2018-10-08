import fuzzy 
soundex = fuzzy.Soundex(4) 
X =  soundex('ankit')
Y =  soundex('aunkit')
print X
print Y
print "done"
