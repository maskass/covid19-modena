import sys, glob
import pandas as pd

comuni = glob.glob('giornaliero/*.txt')

daylist=[pd.to_datetime(file.split('_')[-1].split('.')[0], format='%d-%m-%Y').replace(hour=0) for file in comuni] 
daylist.sort()

tutti = set(pd.date_range(daylist[0], daylist[-1]))
presenti = set(daylist)

mancanti = list(tutti - presenti)
mancanti.sort()

print('Giorni mancanti:\n')
for i,d in enumerate(mancanti):
    print(f'{i+1}) {d:%d-%m-%Y}')