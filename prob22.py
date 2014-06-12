text = sorted(raw_input().replace('"','').split(","))

def score( x ):
    ret = 0
    for i in x:
        ret += ord(i)-64
    return ( ret )
    
record = 0
total_score = 0

for i in text:
    record += 1
    total_score += ( score( i ) * record )
        
print "%d" % (total_score)