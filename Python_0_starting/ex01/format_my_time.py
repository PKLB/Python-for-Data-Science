import datetime as loko

timethen = loko.datetime(1970,1,1)
timenow = loko.datetime.now()
today =  loko.datetime.today()

timefinal = timenow - timethen
realfinaltime = '{:,}'.format(timefinal.total_seconds())
decimalrealfinaltime = '{:.2e}'.format(timefinal.total_seconds())
print("Seconds since January 1, 1970:", realfinaltime[:-2], "or",decimalrealfinaltime, "in scientific notation")
print (today.strftime("%b %d %Y"))

# Write a script that formats the dates this way, of course your date will not be mine
# as in the example but it must be formatted the same.
# Expected output:
# $>python format_my_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
# $>