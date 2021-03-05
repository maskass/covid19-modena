import glob
import pandas as pd
from miscellanea import importa_abitanti, importa_dati_giornalieri

# Fonte dei dati comune per comune
comuni = glob.glob('giornaliero/*.txt')
dfcomuni = importa_dati_giornalieri(comuni)

# Dati abitanti
abitanti = importa_abitanti('abitanti_provincia_di_Modena.txt')

# Incidenza 7gg. - finestra centrata su ultimo giorno 
# con center=True è invece al centro
roll = dfcomuni.rolling(7, center=False).sum()

# 2 Report generali

## 1 tutti i comuni, nuovi positivi
dfcomuni.to_excel('report_vari/nuovi_positivi_comuni_MO.xlsx')
roll.to_excel('report_vari/nuovi_positivi_rolling7gg_comuni_MO.xlsx')

## 2 tutti i comuni, incidenza7gg
dfcomuni.to_csv('report_vari/nuovi_positivi_comuni_MO.csv')
roll.to_csv('report_vari/nuovi_positivi_rolling7gg_comuni_MO.csv')

# Report di tutti i comuni

lista_output = [ comune for comune in dfcomuni.columns if (comune!='Fuori provincia')&(comune!='TOTALE') ]

for comune in lista_output :
    nome_file = comune.replace(' ','').replace('.','').replace('/','') # crea nomi di file semplici
    temp_df = pd.concat((dfcomuni[comune], roll[comune], roll[comune]/abitanti[comune]*100000), axis=1)
    temp_df.columns = ['nuovi pos.', 'somma mobile 7gg.', 'somma mobile 7gg. per 100mila abitanti']
    temp_df.to_excel('report_vari/comuni/' + nome_file + '.xlsx')
    temp_df.to_csv('report_vari/comuni/' + nome_file + '.csv')