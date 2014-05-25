def leap_year( x ):
    return ( (x % 4 == 0) and ( x % 100 != 0 or x % 400 == 0) )

days = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ['mon','tsu','wed','thu','fri','sat','sun']

day = 6
month = 0
year = 1901

ans = 0

while 1:

    day += 7
       
    if day > days[ month ]:
        day -= days[ month ]
        month += 1
        if month > 11:
            month = 0
            year += 1
            if leap_year( year ):
                days[1] = 29
            else:
                days[1] = 28        
    
    if year > 2000:
        break
                
    if day == 1:
        #print "%d %d %d" % ( day, month, year )
        ans += 1

print "%d" % ( ans )