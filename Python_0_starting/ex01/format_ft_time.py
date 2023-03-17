import datetime as loko

timethen = loko.datetime(1970,1,1)
timenow = loko.datetime.now()
today =  loko.datetime.today()

timefinal = timenow - timethen
realfinaltime = '{:,}'.format(timefinal.total_seconds())
decimalrealfinaltime = '{:.2e}'.format(timefinal.total_seconds())
print("Seconds since January 1, 1970:", realfinaltime[:-2], "or",decimalrealfinaltime, "in scientific notation")
print (today.strftime("%b %d %Y"))
