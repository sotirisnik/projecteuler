import math

F1 = 1;
F2 = 1;
i = 2;

while math.log(F2,10)+1 < 1000:
    Fnext = F1 + F2;
    F1 = F2;
    F2 = Fnext;
    i = i + 1;
    
print "%d" % (i);