import calendar
import os
for a in range(1,13):
    ts = calendar.monthrange(2019, a)[1]
    for xx in range(1, ts+1):
        if calendar.weekday(2019, a, xx) in [5, 6]:
            if len(str(xx)) == 1:
                print('20190'+str(a)+"0"+str(xx)+",")
            else:
                print('20190'+str(a)+str(xx)+",")
os.system('pause')