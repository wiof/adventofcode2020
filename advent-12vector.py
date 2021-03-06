#sed 's/^\(.\)/("\1",/ ; s/$/),/' < advent-12.raw > advent-12a.py
# grep L\\\|R advent-12.raw | sort -u
# L180
# L270
# L90
# R180
# R270
# R90

m = [("R",180),
("S",1),
("F",44),
("R",90),
("E",5),
("N",3),
("E",5),
("S",4),
("W",1),
("F",68),
("E",2),
("L",90),
("F",40),
("W",3),
("N",2),
("L",180),
("S",3),
("R",90),
("R",90),
("W",5),
("F",45),
("L",90),
("F",9),
("W",5),
("N",1),
("E",1),
("F",39),
("R",90),
("F",6),
("E",3),
("N",1),
("E",2),
("N",3),
("L",180),
("N",5),
("L",90),
("L",90),
("S",2),
("F",72),
("L",90),
("E",5),
("L",90),
("S",2),
("F",79),
("N",3),
("R",90),
("F",25),
("R",90),
("F",16),
("W",2),
("L",90),
("F",81),
("W",5),
("L",90),
("E",5),
("S",3),
("W",5),
("N",1),
("L",180),
("F",73),
("N",1),
("F",60),
("S",3),
("E",1),
("F",65),
("W",1),
("R",90),
("F",36),
("S",4),
("W",1),
("R",90),
("S",2),
("F",33),
("S",5),
("L",90),
("E",3),
("F",11),
("S",4),
("W",2),
("L",90),
("F",57),
("W",4),
("N",1),
("R",180),
("S",2),
("F",87),
("N",2),
("E",2),
("S",2),
("F",89),
("L",90),
("W",1),
("N",3),
("F",63),
("R",270),
("W",4),
("N",1),
("R",90),
("F",67),
("L",90),
("F",74),
("N",5),
("W",5),
("S",3),
("L",90),
("N",1),
("L",180),
("W",4),
("S",4),
("E",1),
("L",90),
("S",1),
("E",4),
("S",3),
("F",95),
("S",4),
("F",32),
("L",90),
("F",9),
("R",180),
("N",4),
("W",3),
("R",90),
("W",4),
("F",10),
("W",5),
("F",21),
("L",180),
("F",17),
("S",4),
("L",90),
("F",24),
("R",90),
("F",1),
("E",5),
("R",180),
("F",63),
("N",5),
("N",4),
("E",1),
("F",73),
("S",2),
("S",5),
("W",1),
("N",1),
("R",90),
("F",77),
("W",4),
("N",4),
("F",74),
("W",5),
("F",82),
("W",4),
("F",8),
("E",4),
("N",2),
("R",90),
("R",90),
("E",3),
("F",44),
("F",42),
("L",90),
("W",5),
("R",90),
("W",5),
("F",45),
("W",5),
("F",35),
("W",1),
("L",90),
("S",1),
("L",90),
("N",5),
("R",90),
("F",4),
("R",180),
("F",19),
("R",180),
("F",16),
("W",5),
("S",1),
("R",90),
("S",2),
("W",3),
("F",44),
("S",4),
("W",4),
("F",95),
("R",180),
("F",1),
("R",90),
("F",36),
("N",4),
("F",12),
("R",90),
("F",26),
("F",14),
("R",90),
("E",5),
("N",1),
("W",2),
("F",88),
("N",5),
("R",180),
("S",2),
("E",4),
("R",90),
("N",4),
("E",4),
("S",2),
("F",9),
("N",2),
("E",3),
("N",5),
("F",28),
("N",4),
("E",3),
("N",3),
("W",3),
("F",93),
("N",2),
("R",180),
("E",2),
("F",9),
("W",1),
("F",28),
("R",90),
("S",1),
("F",82),
("W",4),
("S",1),
("F",59),
("S",2),
("F",7),
("E",2),
("R",180),
("E",5),
("F",19),
("S",3),
("E",4),
("F",53),
("L",270),
("E",1),
("L",90),
("W",3),
("F",2),
("S",3),
("F",40),
("E",3),
("S",1),
("F",94),
("W",3),
("L",90),
("F",87),
("W",3),
("F",37),
("S",5),
("E",2),
("N",2),
("R",270),
("F",55),
("R",90),
("S",1),
("W",2),
("N",1),
("L",90),
("F",21),
("W",5),
("N",4),
("L",90),
("N",3),
("F",50),
("F",18),
("N",2),
("F",3),
("W",5),
("F",68),
("N",5),
("L",90),
("R",270),
("F",31),
("L",90),
("F",90),
("R",90),
("E",3),
("N",3),
("L",90),
("F",97),
("S",1),
("W",2),
("N",2),
("F",10),
("E",1),
("W",3),
("S",4),
("F",56),
("R",270),
("F",70),
("S",1),
("L",90),
("E",1),
("F",89),
("W",2),
("F",94),
("L",180),
("F",94),
("R",90),
("N",4),
("F",89),
("R",180),
("W",5),
("F",81),
("R",90),
("N",3),
("F",61),
("W",3),
("W",5),
("W",2),
("F",90),
("F",66),
("N",5),
("R",90),
("E",2),
("F",31),
("L",90),
("E",4),
("E",1),
("R",180),
("W",5),
("F",8),
("W",3),
("R",90),
("F",92),
("R",90),
("E",1),
("R",90),
("E",2),
("F",66),
("E",5),
("R",90),
("S",2),
("R",90),
("W",5),
("R",90),
("F",52),
("S",5),
("E",2),
("N",1),
("F",57),
("W",1),
("F",30),
("W",5),
("F",51),
("N",3),
("F",82),
("L",90),
("S",1),
("W",4),
("R",90),
("W",5),
("N",5),
("E",5),
("N",5),
("F",41),
("N",3),
("R",90),
("S",3),
("E",1),
("R",90),
("W",2),
("N",5),
("W",5),
("F",45),
("L",270),
("F",93),
("E",4),
("R",270),
("F",95),
("S",3),
("W",2),
("N",3),
("R",90),
("W",2),
("E",2),
("F",56),
("R",90),
("N",4),
("E",3),
("R",90),
("W",3),
("N",4),
("F",54),
("R",90),
("E",5),
("F",86),
("E",3),
("R",90),
("F",8),
("N",1),
("F",79),
("S",3),
("E",1),
("N",2),
("F",90),
("L",90),
("E",2),
("R",90),
("W",2),
("F",95),
("E",2),
("L",90),
("E",1),
("F",47),
("W",3),
("L",90),
("F",78),
("L",90),
("W",3),
("R",90),
("N",1),
("F",34),
("W",2),
("L",90),
("W",4),
("R",90),
("W",2),
("R",180),
("E",3),
("S",5),
("W",2),
("F",61),
("W",3),
("R",90),
("E",5),
("F",30),
("S",3),
("F",11),
("W",4),
("S",2),
("F",33),
("R",270),
("F",94),
("L",270),
("S",3),
("L",90),
("F",48),
("R",180),
("S",4),
("F",17),
("N",4),
("F",64),
("L",90),
("N",5),
("R",90),
("S",3),
("N",4),
("F",53),
("S",5),
("W",5),
("L",180),
("E",3),
("F",96),
("R",90),
("F",48),
("R",180),
("F",84),
("E",4),
("R",270),
("F",48),
("F",32),
("R",90),
("F",79),
("S",2),
("R",90),
("E",5),
("S",4),
("L",90),
("S",5),
("F",5),
("W",4),
("F",30),
("R",180),
("S",2),
("E",3),
("N",4),
("F",80),
("E",1),
("F",75),
("E",5),
("L",90),
("S",2),
("W",3),
("F",87),
("L",90),
("F",57),
("S",5),
("F",78),
("N",5),
("E",2),
("E",2),
("F",53),
("N",5),
("F",58),
("E",4),
("R",90),
("N",3),
("E",1),
("S",4),
("W",2),
("N",3),
("R",180),
("W",4),
("S",1),
("F",17),
("R",90),
("N",4),
("W",4),
("S",3),
("W",1),
("R",90),
("S",4),
("R",90),
("N",1),
("W",4),
("N",2),
("F",17),
("R",90),
("N",1),
("L",90),
("S",3),
("E",4),
("S",3),
("R",90),
("F",66),
("E",2),
("N",4),
("W",4),
("S",1),
("L",90),
("F",56),
("R",180),
("S",5),
("F",43),
("E",5),
("F",44),
("E",5),
("S",2),
("E",2),
("R",180),
("F",64),
("N",4),
("W",5),
("L",180),
("E",2),
("L",90),
("N",4),
("E",5),
("F",75),
("L",90),
("E",3),
("L",90),
("F",79),
("R",180),
("E",2),
("L",90),
("F",88),
("S",4),
("W",3),
("R",90),
("E",3),
("F",43),
("E",3),
("F",43),
("N",1),
("W",4),
("S",3),
("F",55),
("N",4),
("F",52),
("E",3),
("L",180),
("E",2),
("N",2),
("F",80),
("R",180),
("S",5),
("F",92),
("N",3),
("W",2),
("R",90),
("E",2),
("L",90),
("W",3),
("S",4),
("L",90),
("N",5),
("E",1),
("L",180),
("F",25),
("W",4),
("F",65),
("E",1),
("S",5),
("R",90),
("N",4),
("F",4),
("E",4),
("F",70),
("F",26),
("N",2),
("N",4),
("W",2),
("F",3),
("R",90),
("N",5),
("F",84),
("W",1),
("R",90),
("N",4),
("W",4),
("F",43),
("R",270),
("S",2),
("F",2),
("S",4),
("L",90),
("F",59),
("L",90),
("F",59),
("R",90),
("S",5),
("F",88),
("L",90),
("N",5),
("E",2),
("F",7),
("S",2),
("W",5),
("L",90),
("S",4),
("R",270),
("F",5),
("L",90),
("E",1),
("F",25),
("E",1),
("S",5),
("F",84),
("L",180),
("F",10),
("W",3),
("L",180),
("S",4),
("F",51),
("N",1),
("W",2),
("L",90),
("F",23),
("W",4),
("N",1),
("E",2),
("F",40),
("W",5),
("N",3),
("F",93),
("R",180),
("E",5),
("S",1),
("E",5),
("F",11),
("S",1),
("E",2),
("L",90),
("E",2),
("F",11),
("R",270),
("W",4),
("L",180),
("N",3),
("R",90),
("F",5),
("L",90),
("R",90),
("N",2),
("F",50),
("R",180),
("S",1),
("E",2),
("S",4),
("E",3),
("N",4),
("W",2),
("F",69),
("E",1),
("N",1),
("W",4),
("R",90),
("F",68),
("W",3),
("S",2),
("F",5),
("W",2),
("S",2),
("S",4),
("R",180),
("W",1),
("R",90),
("F",14),
("E",5),
("S",3),
("W",2),
("F",84),
("E",1),
("L",90),
("F",99),
("S",4),
("S",4),
("W",1),
("F",31),
("E",4),
("F",77),
("S",4),
("F",75),
("R",90),
("W",3),
("R",90),
("L",90),
("E",5),
("N",4),
("W",3),
("L",90),
("E",2),
("L",90),
("W",1),
("F",91),
("L",90),
("E",2),
("L",90),
("N",1),
("E",1),
("R",180),
("S",1),
("L",90),
("F",72),
("W",2),
("R",270),
("F",18),
("N",5),
("F",7),
("E",3),
("F",83),
("W",5),
("E",1),
("S",3),
("E",3),
("F",76),
("S",5),
("L",90),
("S",4),
("E",2),
("S",1),
("R",270),
("F",52),
("R",270),
("F",51),
("N",2),
("F",41),
("N",1),
("E",5),
("S",3),
("R",90),
("W",4),
("F",53)]

nsew = {
    "N": ( 1, 0),
    "S": (-1, 0),
    "E": ( 0, 1),
    "W": ( 0,-1)
}
headings= "ESWN"
HEADINGCHUNK = 90 #degrees, granularity given

def vector_sum(a,b):
    return(list(map(sum, zip(a,b))))

def vector_mul(a,b):
    return(x * b for x in a)

headingidx = 0
pos = (0, 0)
for move in m:
    if move[0] in "LR":
        sign = 1 if move[0]=="R" else -1
        headingidx = ( headingidx + (sign * (move[1] // HEADINGCHUNK))) % len(headings)
    else:
        effective_heading = headings[headingidx] if move[0] == "F" else move[0]
        pos = vector_sum(pos, vector_mul( nsew[effective_heading], move[1]))
    print(move,pos)
print(sum(abs(x) for x in pos))

# B
pos = (0, 0)
wp = (1, 10)
trans = {
    0  : lambda v: [ v[0],  v[1]], #for completeness
    90 : lambda v: [-v[1],  v[0]],
    180: lambda v: [-v[0], -v[1]],
    270: lambda v: [ v[1], -v[0]]
}
for move in m:
    if move[0] in "LR":
        right_degrees = 360 - move[1] if move[0] == "L" else move[1]
        wp = trans[right_degrees](wp)
    elif move[0] == "F":
        pos = vector_sum(pos, vector_mul( wp, move[1]))
    else:
        wp = vector_sum(wp, vector_mul(nsew[move[0]], move[1]))
    print(move,pos, wp)
print(sum(abs(x) for x in pos))

