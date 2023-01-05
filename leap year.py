def Julian_calendar_leap_year(year):
    #multiple of 4
    if year%4 == 0:
        print("Year : "+str(year)+"--> Leap Year" )
    else:
        print("Year : "+str(year)+"--> Not Leap Year" )

def  Gregorian_calendar_leap_year(year):
    #either Divisible of 400 
    #or divisible by 4 but not divisible by 100
    if year%400 == 0 or year%4 == 0 and year%100 != 0: 
        print("Year : "+str(year)+"--> Leap Year" )
    else:
        print("Year : "+str(year)+"--> Not Leap Year" )

Julian_calendar_leap_year(1912)
print("-"*25)
Gregorian_calendar_leap_year(2016)
