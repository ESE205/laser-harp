
##import pygame
##
##s1= pygame.mixer.music.load('/home/pi/laserharp-sounds/1.wav')
##s2= pygame.mixer.music.load('/home/pi/laserharp-sounds/2.wav')
##s3= pygame.mixer.music.load('/home/pi/laserharp-sounds/3.wav')
##s4= pygame.mixer.music.load('/home/pi/laserharp-sounds/4.wav')
##s5= pygame.mixer.music.load('/home/pi/laserharp-sounds/5.wav')
##s6= pygame.mixer.music.load('/home/pi/laserharp-sounds/6.wav')

s1 = wave.open('/home/pi/laserharp-sounds/1.wav')
s2 = wave.open('/home/pi/laserharp-sounds/2.wav')
s3 = wave.open('/home/pi/laserharp-sounds/3.wav')
s4 = wave.open('/home/pi/laserharp-sounds/4.wav')
s5 = wave.open('/home/pi/laserharp-sounds/5.wav')
s6 = wave.open('/home/pi/laserharp-sounds/6.wav')

s = [s1, s2, s3, s4, s5, s6]
match2 = [ [],[] ]
match3 = [ [],[],[] ]
match4 = [ [],[],[],[] ]
match5 = [ [],[],[],[],[] ]
match6 = [ [],[],[],[],[],[] ]

for a in range (1,6)
    for b in range (1,6)
	if (b !=a)
	    couple = s(a)+s(b)
	    match2.append(couple)
for a in range (1,6)
    for b in range (1,6)
	for c in range (1,6)
	    if (a != b and b!=c and c! = a)
                triple = s(a)+s(b)+s(c)
		match3.append(triple)
for a in range (1,6)
    for b in range (1,6)
	for c in range (1,6)
            for d in range (1,6)
                if (a != b and b!=c and c! = a and a!=d and b!=d and c!=d)
                    quad = s(a)+s(b)+s(c)+s(d)
                    match4[a][b][c][d]=quad
for a in range (1,6)
    for b in range (1,6)
	for c in range (1,6)
            for d in range (1,6)
                for e in range (1,6)
                    if(a != b and b!=c and c! = a and a!=d and
                       b!=d and c!=d and a!=e and b!=e and c!=e and d!=e)
                        fifth = s(a)+s(b)+s(c)+s(d)+s(e)
                        match5[a][b][c][d][e] = fifth
for a in range (1,6)
    for b in range (1,6)
	for c in range (1,6)
            for d in range (1,6)
                for e in range (1,6)
                    for f in range (1,6)
                        if (a != b and b!=c and c! = a and a!=d and
                       b!=d and c!=d and a!=e and b!=e and c!=e and d!=e
                            and a!=f and b!=f and c!=f and d!=f and e!=f)
                        sixth = s(a)+s(b)+s(c)+s(d)+s(e)+s(f)
                        match6[a][b][c][d][e][f] = sixth
                    
